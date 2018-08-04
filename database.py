#!/usr/bin/python3
#coding=utf-8

import pymysql

#fetch the parameter
import sys

# Open database connection
db = pymysql.connect("localhost","root","user123","crawlGoogleScholar" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
# cursor.execute("DROP TABLE IF EXISTS employee")

# Create table as per requirement
sql = """CREATE TABLE if not EXISTS `paperList` (
  `ID` int primary key not null auto_increment,
  `title` varchar(1000) DEFAULT NULL,
  `author` varchar(200) DEFAULT NULL,
  `corAuthor` varchar(50) DEFAULT NULL,
  `firstAuthor` varchar(50) DEFAULT NULL,
  `author_chs` varchar(200) DEFAULT NULL,
  `corAuthor_chs` varchar(50) DEFAULT NULL,
  `firstAuthor_chs` varchar(50) DEFAULT NULL,
  `journal` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `institution` varchar(100) DEFAULT NULL,
  `citeNumber` int DEFAULT NULL,
  `checkDate` datetime DEFAULT NULL,
  `impactFactor` DECIMAL(6,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
cursor.execute(sql)

sql = """CREATE TABLE if not EXISTS `citepaper` (
  `id` int primary key auto_increment,
  `title` varchar(1000) DEFAULT NULL,
  `author` varchar(200) DEFAULT NULL,
  `originalPaperID` int,
  foreign key(originalPaperID)　references paperList(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
cursor.execute(sql)

sql = """CREATE TABLE if not EXISTS `impactFactor` (
  `journal` varchar(200) DEFAULT NULL,
  `abbreviation_1` varchar(20) DEFAULT NULL,
  `abbreviation_2` varchar(20) DEFAULT NULL,
  `1995` DECIMAL(6,3) DEFAULT NULL,
  `1996` DECIMAL(6,3) DEFAULT NULL,
  `1997` DECIMAL(6,3) DEFAULT NULL,
  `1998` DECIMAL(6,3) DEFAULT NULL,
  `1999` DECIMAL(6,3) DEFAULT NULL,
  `2000` DECIMAL(6,3) DEFAULT NULL,
  `2001` DECIMAL(6,3) DEFAULT NULL,
  `2002` DECIMAL(6,3) DEFAULT NULL,
  `2003` DECIMAL(6,3) DEFAULT NULL,
  `2004` DECIMAL(6,3) DEFAULT NULL,
  `2005` DECIMAL(6,3) DEFAULT NULL,
  `2006` DECIMAL(6,3) DEFAULT NULL,
  `2007` DECIMAL(6,3) DEFAULT NULL,
  `2008` DECIMAL(6,3) DEFAULT NULL,
  `2009` DECIMAL(6,3) DEFAULT NULL,
  `2010` DECIMAL(6,3) DEFAULT NULL,
  `2011` DECIMAL(6,3) DEFAULT NULL,
  `2012` DECIMAL(6,3) DEFAULT NULL,
  `2013` DECIMAL(6,3) DEFAULT NULL,
  `2014` DECIMAL(6,3) DEFAULT NULL,
  `2015` DECIMAL(6,3) DEFAULT NULL,
  `2016` DECIMAL(6,3) DEFAULT NULL,
  `2017` DECIMAL(6,3) DEFAULT NULL,
  `2018` DECIMAL(6,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
cursor.execute(sql)

#存入键盘输入的论文信息
# sql='''insert into user
# (title,author,c-author,f-author,author-c,c-author-c,f-author-c,journal,data,institution) 
# values
# (sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9],sys.argv[10],sys.argv[11])'''
# cursor.execute(sql)
print("Created table Successfull.")
# # disconnect from server
