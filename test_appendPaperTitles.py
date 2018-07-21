"""
append Papers Titles
"""

from utils import requestsPage
from lxml import etree


def appendPapersTitles(pagingUrls,citingPapersTitles):
    fullpagingUrl = 'https://scholar.google.com.hk' + pagingUrl
    html = requestsPage(fullpagingUrl).text
    selector = etree.HTML(html)
    print('successfully..................')          
    addCitingPapersTitles = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div/h3/a/text()')
    citingPapersTitles = citingPapersTitles + addCitingPapersTitles
    print('Add CitingPapersTitles successfully')
    return citingPapersTitles


if __name__ == '__main__':
    citingPapersTitles = []
    pagingUrls=['/scholar?start=10&hl=zh-CN&as_sdt=2005&sciodt=0,5&cites=5700566640779965299&scipsc=', '/scholar?start=20&hl=zh-CN&as_sdt=2005&sciodt=0,5&cites=5700566640779965299&scipsc=', '/scholar?start=30&hl=zh-CN&as_sdt=2005&sciodt=0,5&cites=5700566640779965299&scipsc=', '/scholar?start=40&hl=zh-CN&as_sdt=2005&sciodt=0,5&cites=5700566640779965299&scipsc=']
    for pagingUrl in pagingUrls:
        citingPapersTitles = appendPapersTitles(pagingUrl,citingPapersTitles)
    print(citingPapersTitles)
    print(len(citingPapersTitles))