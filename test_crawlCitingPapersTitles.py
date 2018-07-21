"""
crawl Google Scholar
"""

# crawl page
from urllib import parse

# utils
from utils import repChar, requestsScholar,requestsPage,appendPapersTitles

from lxml import etree
    
def crawlCitingPapersTitles(citingPapersUrl):
    html = requestsPage(citingPapersUrl).text
    selector = etree.HTML(html)
    citingPapersTitles = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div/h3/a/text()')

    pagingUrls = selector.xpath('//*[@id="gs_nml"]/a/@href')
    if len(pagingUrls)==0:
        print('There is only one page of citingPapers')
    else:
        print('I am loading a new page,please be patient')
        for pagingUrl in pagingUrls:
            citingPapersTitles = appendPapersTitles(pagingUrl,citingPapersTitles)
    return citingPapersTitles,citingPapersUrl


if __name__ == "__main__":
    #当前论文名称：Quantitative proteome analysis of HCC cell lines with different metastatic potentials by SILAC
    citingPapersUrl='https://scholar.google.com.hk/scholar?cites=5700566640779965299&as_sdt=2005&sciodt=0,5&hl=zh-CN'  
    citingPapersTitles = crawlCitingPapersTitles(citingPapersUrl)
    print(type(citingPapersTitles))


