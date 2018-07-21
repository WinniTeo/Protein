import re

# Random delay
import time
import random

# requests
import requests
from lxml import etree

# headers
import headers
"""
Replace illegal characters
"""
def repChar(character):
    pattern = r'[\\s\\\\/:\\*\\?\\\"<>\\|]'
    prog = re.compile(pattern)
    newCharacter = prog.sub('_', character)
    return newCharacter


    
"""
Random delay

"""
def delay():
    delayTime = random.uniform(1, 3)
    time.sleep(delayTime)


def requestsPage(req_url):
    delay()
    html = requests.get(req_url, headers = headers.getHeader())
    return html


def appendPapersTitles(pagingUrl,citingPapersTitles):
    fullPageUrl = 'https://scholar.google.com.hk' + pagingUrl
    html = requestsPage(fullPageUrl).text
    selector = etree.HTML(html)        
    addCitingPapersTitles = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div/h3/a/text()')
    citingPapersTitles = citingPapersTitles + addCitingPapersTitles
    return citingPapersTitles

if __name__ == '__main__':
    page = requestsPage("https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=learn&oq=")
    with open('test.html', 'w', encoding = 'utf-8') as f:
        f.write(page.text)
