
import pymysql

import xlrd  
import xlwt 

# Open database connection
db = pymysql.connect("localhost", "root", "user123", "papercrawler", charset = 'utf8' )

# prepare a cursor object using cursor() method
cursor = db.cursor()

"""
导入2007-2016影响因子到impactFactor
"""
path = 'C:\\Users\\WinniTeo\\Desktop\\shixi\\doc\\impactFactor\\2007-2016.xlsx'
# 打开文件  
workbook = xlrd.open_workbook(path)  
# 根据sheet索引或者名称获取sheet内容  
sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始  
sheet1 = workbook.sheet_by_name('sheet1')  
#获得sheet的行数
nrows = sheet1.nrows
print(nrows)
for i in range(1,nrows):
    row_data = sheet1.row_values(i)
    journal = row_data[0]
    abbreviation = row_data[1]
    IF_2016 = row_data[2]
    IF_2015 = row_data[3]
    IF_2014 = row_data[4]
    IF_2013 = row_data[5]
    IF_2012 = row_data[6]
    IF_2011 = row_data[7]
    IF_2010 = row_data[8]
    IF_2009 = row_data[9]
    IF_2008 = row_data[10]

    sql='''insert ignore into impactfactor
    (journal, abbreviation, IF_2008, IF_2009, IF_2010, IF_2011, IF_2012, IF_2013, IF_2014, IF_2015, IF_2016)
    values
    ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')'''%(journal, abbreviation, IF_2008, IF_2009, IF_2010, IF_2011, IF_2012, IF_2013, IF_2014, IF_2015, IF_2016)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

"""
导入2017-2018影响因子到impactFactor
"""
path = 'C:\\Users\\WinniTeo\\Desktop\\shixi\\doc\\impactFactor\\2017-2018.xlsx'
# 打开文件  
workbook = xlrd.open_workbook(path)  
# 根据sheet索引或者名称获取sheet内容  
sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始  
sheet1 = workbook.sheet_by_name('sheet1')  
#获得sheet的行数
nrows = sheet1.nrows
print(nrows)
for i in range(1,nrows):
    row_data = sheet1.row_values(i)
    journal = row_data[0]
    IF_2018 = row_data[1]
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