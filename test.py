"""
Extract useful information
"""

import re
import requests
from lxml import etree
from bs4 import BeautifulSoup

html = open(r"C:\\Users\\WinniTeo\\Desktop\\shixi\\doc\\html\\html_(2011)_A_Systems_Biology-Based_Classifier_for_Hepatocellular_Carcinoma_Diagnosis.html",'rb')
content = html.read()
NumberOfQuotes=[]
JumpLink=[]
selector=etree.HTML(content)
# Number Of Quotes
NumberOfQuotes = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div[2]/div[3]/a[3]/text()')
#print(NumberOfQuotes)

#JumpLink
JumpLink=selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div[2]/div[3]/a[3][@href]')
for each in JumpLink:
    print(each)

# Soup = BeautifulSoup(content, "lxml")
# data = Soup.find_all(id="gs_res_ccl_mid")
# print(data)