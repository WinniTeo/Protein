
import pymysql

import datetime

import xlrd  
import xlwt 

from collectPaperInf import collectPaperInf

# Open database connection
db = pymysql.connect("localhost", "root", "user123", "papercrawler", charset = 'utf8' )

# prepare a cursor object using cursor() method
cursor = db.cursor()

"""
导入数据到paperList
"""
# 获取论文数据
path = 'C:\\Users\\WinniTeo\\Desktop\\shixi\\doc\\input\\input.xlsx'
# 打开文件  
workbook = xlrd.open_workbook(path)  
# 根据sheet索引或者名称获取sheet内容  
sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始  
sheet1 = workbook.sheet_by_name('sheet1')
# 获取第二数行据  
row_data = sheet1.row_values(2)
title = row_data[1]
author = row_data[2]
corAuthor = row_data[3]
firstAuthor = row_data[4]
author_chs = row_data[5]
corAuthor_chs = row_data[6]
firstAuthor_chs = row_data[7]
journal = row_data[8]
date = row_data[9]
institution = row_data[10]

# 调用爬虫获取论文引用次数，引用论文标题
crawlResult = collectPaperInf(title)
citeNumber = str(crawlResult[0])
citingPapersTitles = crawlResult[1]
# 分割字符串，获取年份月份
year = date[0:4]
year = str(int(year)+1)
month = date[6:] #时间格式为****-**-**

# 获取当前时间
dt =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 将excel中数据插入paperlist数据库
sql='''insert ignore into paperlist
(title, author, corAuthor, firstAuthor, author_chs, corAuthor_chs, firstAuthor_chs, journal, date, institution, checkDate) 
values
('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')'''%(title, author, corAuthor, firstAuthor, author_chs, corAuthor_chs, firstAuthor_chs, journal, date, institution, dt)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# 当爬取的引用数不为空时，更新paperList中的citeNumber字段
if citeNumber:
    updateSql = "UPDATE paperList SET citeNumber='" + citeNumber + "' WHERE title='" + title + "'"
    try:
        # Execute the SQL command
        cursor.execute(updateSql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

# 检测impactFactor表中是否存有此年份的影响因子
# 如果有获取影响因子
if (year == '2007' or year == '2008' or year == '2009' or year == '2010' or year == '2011' or year == '2012' or year == '2013' or year == '2014' or year == '2015' or year == '2017'):

    sql = "SELECT IF_" + year + " FROM impactFactor WHERE journal='" + journal + "' or abbreviation='" + journal + "'"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    impactFactor = cursor.fetchone()
    impactFactor = str(impactFactor[0])
    # 当影响因子不为空时，更新paperlist中当前论文的impactFactor字段
    if impactFactor: 
        sql = "UPDATE paperList SET impactFactor='" + impactFactor + "',currentState='T' WHERE title='" + title + "'"
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()   
    # 当影响因子为空，设impactFactor为0               
    else:
        sql = "UPDATE paperList SET impactFactor = 0 WHERE title='" + title + "'"
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback() 

# 当时间大于2017年时，论文影响因子为2017年影响因子            
elif year > '2017':
    sql = "SELECT IF_2017 FROM impactFactor WHERE journal='" + journal + "' or abbreviation='" + journal + "'"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    impactFactor = cursor.fetchone()
    impactFactor = str(impactFactor[0])
    # 当影响因子不为空时，更新paperlist中当前论文的impactFactor字段
    if impactFactor: 
        sql = "UPDATE paperList SET impactFactor='" + impactFactor + "',currentState='T' WHERE title='" + title + "'"
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()   
    # 当影响因子为空，设impactFactor为0               
    else:
        sql = "UPDATE paperList SET impactFactor = 0 WHERE title='" + title + "'"
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback() 
                
# 当年份不存在，设impactFactor为0
else:
    sql = "UPDATE paperList SET impactFactor = 0 WHERE title='" + title + "'"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback() 

"""
导入数据到citePaper
"""
# 获取当前论文的编号
selectSql = "SELECT ID FROM paperlist WHERE title='" + title + "'"
try:
    # Execute the SQL command
    cursor.execute(selectSql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()
ID = cursor.fetchone()
ID = str(ID[0])

# 将全部引用论文存入citepaper数据表中
# 判断爬取的论文标题是否为空
if citingPapersTitles:
    for citingPapersTitle in citingPapersTitles:
        insertSql = "insert into citepaper(title, originalPaperID)values('" + citingPapersTitle + "','" + ID + "')"
        try:
            # Execute the SQL command
            cursor.execute(insertSql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

db.close()

