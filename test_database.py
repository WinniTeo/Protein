#!/usr/bin/python3

import pymysql

#fetch the parameter
import sys

#from collectPaperInf import collectPaperInf

# Open database connection
db = pymysql.connect("localhost","root","user123","crawlGoogleScholar" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

"""
导入数据到paperList
"""
paperTitle = sys.argv[1]
# citeNumber = collectPaperInf(paperTitle)[0]
citeNumber = 200
# citingPapersTitles = collectPaperInf(paperTitle)[1]
journal = sys.argv[8]
month = sys.argv[9][6:] #时间格式为****-**-**，获取日期
year = sys.argv[9][0:4]
print(sys.argv[1])
print(sys.argv[10])
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

# if month >= '07-01':
#     #获取杂志对应年份的影响因子
#     sql = "SELECT %s FROM impactFactor \
#                         WHERE journal = %s or abbreviation = %s " % ('IF_'+ year, journal,journal)
#     try:
#         # Execute the SQL command
#         cursor.execute(sql)
#         # Commit your changes in the database
#         db.commit()
#     except:
#         # Rollback in case there is any error
#         db.rollback()
#     impactFactor = cursor.fetchall()
#     #当影响因子不为空，更新此杂志的影响因子
#     if impactFactor:
#         sql = "UPDATE paperList SET impactFactor = '%s' \
#                                  WHERE title = '%s'" % (impactFactor, journal)
#         try:
#             # Execute the SQL command
#             cursor.execute(sql)
#             # Commit your changes in the database
#             db.commit()
#         except:
#             # Rollback in case there is any error
#             db.rollback()   
#     #当影响因子为空，设其为'Not Available'                   
#     else:
#         sql = "UPDATE paperList SET impactFactor = 'Not Available' \
#                                 WHERE title = %s" % (journal)
#         cursor.execute(sql)
#         try:
#             # Execute the SQL command
#             cursor.execute(sql)
#             # Commit your changes in the database
#             db.commit()
#         except:
#             # Rollback in case there is any error
#             db.rollback()  
# else:
#     #获取杂志对应年份的影响因子
#     year = str(int(year)+1)
#     sql = "SELECT %s FROM impactFactor \
#                     WHERE title = %s" % ('IF_'+ year, journal)
#     try:
#         # Execute the SQL command
#         cursor.execute(sql)
#         # Commit your changes in the database
#         db.commit()
#     except:
#         # Rollback in case there is any error
#         db.rollback()
#     impactFactor = cursor.fetchall()
#     #当影响因子不为空，更新此杂志的影响因子
#     if impactFactor:
#         sql = "UPDATE paperList SET impactFactor = '%s' \
#                                  WHERE title = '%s'" % (impactFactor, journal)
#         try:
#             # Execute the SQL command
#             cursor.execute(sql)
#             # Commit your changes in the database
#             db.commit()
#         except:
#             # Rollback in case there is any error
#             db.rollback()   
#     #当影响因子为空，设其为'Not Available'                   
#     else:
#         sql = "UPDATE paperList SET impactFactor = 'Not Available' \
#                                 WHERE title = %s" % (journal)
#         cursor.execute(sql)
#         try:
#             # Execute the SQL command
#             cursor.execute(sql)
#             # Commit your changes in the database
#             db.commit()
#         except:
#             # Rollback in case there is any error
#             db.rollback() 


