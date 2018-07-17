"""
Extract useful information
"""

import re
import requests
from lxml import etree

NumberOfQuotes=[]
html='C:\\Users\\WinniTeo\\Desktop\\shixi\\doc\\html\\html_Protein_Probabilities_in_Shotgun_Proteomics__Evaluating_Different_Estimation_Methods_Using_a_Semi-Random_Sampling_Model.html'
selector=etree.HTML(html)
#Number Of Quotes
NumberOfQuotes = selector.xpath(' //*[@id="gs_res_ccl_mid"]/div/div[2]/div[3]/a[3]/text()')
print(NumberOfQuotes)