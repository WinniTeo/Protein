
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
print(type(month))
print('IF_'+ year)

# sql='''insert into paperlist
# (title, author, corAuthor, firstAuthor, author_chs, corAuthor_chs, firstAuthor_chs, journal, data, institution, citeNumber) 
# values
# ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')'''%(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], citeNumber)
# try:
#     # Execute the SQL command
#     cursor.execute(sql)
#     # Commit your changes in the database
#     db.commit()
# except:
#     # Rollback in case there is any error
#     db.rollback()

sql = "SELECT IF_" + year + " FROM impactFactor WHERE journal='" + journal + "' or abbreviation='" + journal + "'"
# try:
#     # Execute the SQL command
#     cursor.execute(sql)
#     # Commit your changes in the database
#     db.commit()
# except:
#     # Rollback in case there is any error
#     db.rollback()

# if month >= '07-01':
#     #获取杂志对应年份的影响因子
#     sql = "SELECT %s FROM impactFactor \
#                         WHERE journal = %s or abbreviation = %s " % ('IF_'+ year, journal, journal)
#     try:
#         # Execute the SQL command
#         cursor.execute(sql)
#         # Commit your changes in the database
#         db.commit()
#     except:
#         # Rollback in case there is any error
#         db.rollback()
#     impactFactor = cursor.fetchone()
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


db.close()