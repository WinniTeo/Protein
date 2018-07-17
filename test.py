"""
Extract useful information
"""

import re
import requests
from lxml import etree

NumberOfQuotes=[]
html='https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Dose+Definition+and+Physical+Dose+Evaluation+for+the+Human+Body+in+External+Radiation+Accidents&btnG='
selector=etree.HTML(html)
#Number Of Quotes
NumberOfQuotes = selector.xpath(' //*[@id="gs_res_ccl_mid"]/div/div[2]/div[3]/a[3]/text()')
print(NumberOfQuotes)