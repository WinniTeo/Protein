#!/usr/bin/python3

import pymysql

#fetch the parameter
import sys

# # Open database connection
# db = pymysql.connect("localhost","root","user123","crawlGoogleScholar" )

# # prepare a cursor object using cursor() method
# cursor = db.cursor()

"""
导入数据到paperList
"""
a_1 = sys.argv[1]
a_2 = sys.argv[2]
a_3 = sys.argv[3]
a_4 = sys.argv[4]
a_5 = sys.argv[5]
a_6 = sys.argv[6]
a_7 = sys.argv[7]
a_8 = sys.argv[8]
a_9 = sys.argv[9]
a_10 = sys.argv[10]

print(type(sys.argv[1]))
print(type(sys.argv[2]))
print(type(sys.argv[3]))
print(type(sys.argv[4]))
print(type(sys.argv[5]))
print(type(sys.argv[6]))
print(type(sys.argv[7]))
print(type(sys.argv[8]))
print(type(sys.argv[9]))
print(type(sys.argv[10]))
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv[4])
print(sys.argv[5])
print(sys.argv[6])
print(sys.argv[7])
print(sys.argv[8])
print(sys.argv[9])
print(sys.argv[10])
# sql='''insert ignore into paperlist
# (title, author, corAuthor, firstAuthor) 
# values
# ('%s', '%s', '%s', '%s', '%s')'''%(a_1, a_2, a_3, a_4, a_10)

# try:
#     # Execute the SQL command
#     cursor.execute(sql)
#     # Commit your changes in the database
#     db.commit()
# except:
#     # Rollback in case there is any error
#     db.rollback()