
import pymysql

#fetch the parameter
import sys

# Open database connection
db = pymysql.connect("localhost", "root", "user123", "papercrawler", charset = 'utf8' )

# prepare a cursor object using cursor() method
cursor = db.cursor()

"""
导入数据到paperList
"""
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
citeNumber = 200
# citeNumber = collectPaperInf(title)[0]
# citingPapersTitles = collectPaperInf(title)[1]
month = date[6:] #时间格式为****-**-**，获取日期
year = date[0:4]
print(month)
print('IF_'+ year)

# 将命令行数据插入paperlist数据库
sql='''insert into paperlist
(title, author, corAuthor, firstAuthor, author_chs, corAuthor_chs, firstAuthor_chs, journal, data, institution, citeNumber) 
values
('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')'''%(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], citeNumber)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# 获取正确的影响因子，更新impactFactor字段
if month >= '07-01':
    year = str(int(year)+1)
    print(year)
    print('beyond')
else:
    year = year
    print('below')
print(type(year))

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
    print(impactFactor)
    if impactFactor:
        sql = "UPDATE paperList SET impactFactor='" + str(impactFactor[0]) + "' WHERE title='" + journal + "'" 
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
        sql = "UPDATE paperList SET impactFactor = -1 WHERE title='" + journal + "'"
        cursor.execute(sql)
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
    sql = "UPDATE paperList SET impactFactor = -2 WHERE title='" + journal + "'"
    cursor.execute(sql)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback() 

db.close()

