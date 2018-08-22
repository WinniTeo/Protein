
import pymysql
# fetch the parameter
import sys
import datetime
from collectPaperInf import collectPaperInf
# Open database connection
db = pymysql.connect("localhost", "root", "user123", "papercrawler", charset = 'utf8' )

# prepare a cursor object using cursor() method
cursor = db.cursor()

"""
导入数据到paperList
"""
# 获取键盘数据
title = sys.argv[1]
author = sys.argv[2]
corAuthor = sys.argv[3]
firstAuthor = sys.argv[4]
author_chs = sys.argv[5]
corAuthor_chs = sys.argv[6]
firstAuthor_chs = sys.argv[7]
journal = sys.argv[8]
date = sys.argv[9]
institution = sys.argv[10]

# 调用爬虫获取论文引用次数，引用论文标题
crawlResult = collectPaperInf(title)
citeNumber = str(crawlResult[0])
citingPapersTitles = crawlResult[1]
# 分割字符串，获取年份月份
year = date[0:4]
month = date[6:] #时间格式为****-**-**

# 获取当前时间
dt =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 将命令行数据插入paperlist数据库
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

# 获取正确的影响因子，更新impactFactor字段
if month >= '07-01':
    year = str(int(year)+1)
else:
    year = year

# 检测数据库是否存有此年份的影响因子
# 如果有获取影响因子
if (year == '2007' or year == '2008' or year == '2009' or year == '2010' or year == '2011' or year == '2012' or year == '2013' or year == '2014' or year == '2015' or year == '2016' or year == '2018'):

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
        sql = "UPDATE paperList SET impactFactor='" + impactFactor + "' WHERE title='" + title + "'"
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()   
    # 当影响因子为空，设impactFactor为-1               
    else:
        sql = "UPDATE paperList SET impactFactor = -1 WHERE title='" + title + "'"
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback() 
# 当年份不存在，设impactFactor为-2
else:
    sql = "UPDATE paperList SET impactFactor = -2 WHERE title='" + title + "'"
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

