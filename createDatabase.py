
#coding=utf-8


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
  `date` char(10) DEFAULT NULL,
  `institution` varchar(100) DEFAULT NULL,
  `citeNumber` int DEFAULT 0 NOT NULL,
  `checkDate` datetime DEFAULT NULL,
  `impactFactor` decimal(6,3) DEFAULT NULL
  `currentState` char(1) DEFAULT 'F'
)""" 


sql = """CREATE TABLE if not EXISTS `citePaper` (
  `ID` int primary key auto_increment,
  `title` varchar(1000) DEFAULT NULL,
  `originalPaperID` int,
  foreign key(originalPaperID) references paperList(ID)
)"""

sql = """CREATE TABLE if not EXISTS `impactFactor` (
  `ID` int primary key not null auto_increment,
  `journal` varchar(200) DEFAULT NULL,
  `abbreviation` varchar(20) DEFAULT NULL,
  `IF_2007` decimal(6,3)  DEFAULT NULL,
  `IF_2008` decimal(6,3)  DEFAULT NULL,
  `IF_2009` decimal(6,3)  DEFAULT NULL,
  `IF_2010` decimal(6,3)  DEFAULT NULL,
  `IF_2011` decimal(6,3)  DEFAULT NULL,
  `IF_2012` decimal(6,3)  DEFAULT NULL,
  `IF_2013` decimal(6,3)  DEFAULT NULL,
  `IF_2014` decimal(6,3)  DEFAULT NULL,
  `IF_2015` decimal(6,3)  DEFAULT NULL,
  `IF_2017` decimal(6,3)  DEFAULT NULL，

  `IF_2018` decimal(6,3)  DEFAULT -1,
  `IF_2019` decimal(6,3)  DEFAULT -1,
  `IF_2020` decimal(6,3)  DEFAULT -1  
)"""
