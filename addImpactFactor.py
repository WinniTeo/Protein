
import pymysql

import xlrd  
import xlwt 

# Open database connection
db = pymysql.connect("localhost", "root", "user123", "papercrawler", charset = 'utf8' )

# prepare a cursor object using cursor() method
cursor = db.cursor()

"""
导入2007-2015影响因子到impactFactor
"""
path = 'C:\\Users\\WinniTeo\\Desktop\\shixi\\doc\\impactFactor\\2007-2015.xlsx'
# 打开文件  
workbook = xlrd.open_workbook(path)  
# 根据sheet索引或者名称获取sheet内容  
sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始  
sheet1 = workbook.sheet_by_name('sheet1')  
#获得sheet的行数
nrows = sheet1.nrows

"""
导入xxxx年影响因子到impactFactor表中
"""
path = 'C:\\Users\\WinniTeo\\Desktop\\shixi\\doc\\impactFactor\\2017-2018.xlsx'
# 打开文件  
workbook = xlrd.open_workbook(path)  
# 根据sheet索引或者名称获取sheet内容  
sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始  
sheet1 = workbook.sheet_by_name('sheet1')  
#获得sheet的行数
nrows = sheet1.nrows

for i in range(1,nrows):
    row_data = sheet1.row_values(i)
    journal = row_data[0]
    IF_2018 = row_data[1]
    # 判断impactFactor数据表中是否已存在此杂志
    isExistSql = "SELECT journal FROM impactFactor WHERE journal='" + journal + "'"
    try:
        # Execute the SQL command
        cursor.execute(isExistSql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    callback = cursor.fetchone()
    print(callback)
    # 如果存在，更新相应年份的影响因子
    if callback:
        sql = '''UPDATE impactfactor SET IF_2018 = '%s' 
        WHERE journal = '%s'
        ''' %(IF_2018, journal)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()  
    # 如果不存在，插入新的杂志和相应年份的影响因子
    else:
        sql='''insert ignore into impactfactor
        (journal, IF_2018)
        values
        ('%s', '%s')'''%(journal, IF_2018)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback() 

db.close()