#!/usr/bin/python3
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
  `date` date DEFAULT NULL,
  `institution` varchar(100) DEFAULT NULL,
  `citeNumber` int DEFAULT NULL,
  `checkDate` datetime DEFAULT NULL,
  `impactFactor` varchar(20) DEFAULT NULL
)"""


sql = """CREATE TABLE if not EXISTS `citePaper` (
  `ID` int primary key auto_increment,
  `title` varchar(1000) DEFAULT NULL,
  `originalPaperID` int,
  foreign key(originalPaperID) references paperList(ID)
)"""

sql = """CREATE TABLE if not EXISTS `impactFactor` (
  `journal` varchar(200) DEFAULT NULL,
  `abbreviation` varchar(20) DEFAULT NULL,
  `IF_2008` varchar(20)  DEFAULT NULL,
  `IF_2009` varchar(20)  DEFAULT NULL,
  `IF_2010` varchar(20)  DEFAULT NULL,
  `IF_2011` varchar(20)  DEFAULT NULL,
  `IF_2012` varchar(20)  DEFAULT NULL,
  `IF_2013` varchar(20)  DEFAULT NULL,
  `IF_2014` varchar(20)  DEFAULT NULL,
  `IF_2015` varchar(20)  DEFAULT NULL,
  `IF_2016` varchar(20)  DEFAULT NULL,
  `IF_2018` varchar(20)  DEFAULT NULL
)"""
