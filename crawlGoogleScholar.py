"""
crawl Google Scholar
"""

# parse docx
import docx
import re

# crawl page
from urllib import parse

# utils
from utils import repChar,requestsPage, appendPapersTitles

# parse html
from lxml import etree


"""
parse docx and extract title
"""
def parseDocx(fileName):
    # 获取文档对象
    docxFile = docx.Document(fileName)
    # 提取标题
    paperTitles = []
    noSpot = []
    for perParagraph in docxFile.paragraphs:
        # 每段文本的定义为text
        perParagraphText = perParagraph.text
        # 提取后面带有数字的小数点
        rr = re.compile(r'\.\d')  #定义提取规则
        noSpot = rr.findall(perParagraphText)
        # 将小数点及后面的数替换为空
        for each in noSpot:
            perParagraphText = perParagraphText.replace(str(each), '')
        # 用'.'将每一个论文信息分割开，存为一个list    
        perParagraphText = perParagraphText.split('.')
        # list 中第二个元素即为所要获取的标题
        paperTitles.append(perParagraphText[1])
    return paperTitles


"""
crawl Google Scholar
"""
def crawlGoogleScholar(perPaperTitle):
    keyword = parse.quote(perPaperTitle)
    req_url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='+keyword+'&btnG='
    html = requestsPage(req_url).text
    selector = etree.HTML(html)
    # 文章标题
    perPaperTitle = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div[2]/h3/a/text()')
    # 引用次数
    numQuotes = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div[2]/div[3]/a[3]/text()')
    # 引用次数链接
    citingPapersUrl = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div[2]/div[3]/a[3]/@href')
    # 谷歌学术的反爬虫做的很好，会出现爬取不到内容的情况和搜不到文章的情况，我们根据爬取的返回值确定返回的是否是我们需要的内容 
    if (len(numQuotes) != 1)or(numQuotes[0] == 'Related articles'):
        print('There is no the number of quote or there is no searching result...')
        return [],[],[]
    else:
        return perPaperTitle[0],numQuotes[0],citingPapersUrl[0]


"""

crawl Citing Papers Titles
"""
def crawlCitingPapersTitles(citingPapersUrl):
    citingPapersUrl = 'https://scholar.google.com.hk' + citingPapersUrl
    html = requestsPage(citingPapersUrl).text
    selector = etree.HTML(html)
    # 提取第一页引用文章标题
    citingPapersTitles = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div/h3/a/text()')
    # 提取翻页链接
    pageUrls = selector.xpath('//*[@id="gs_nml"]/a/@href')
    # 判断有无翻页链接
    if len(pageUrls)==0:
        print('There is only one page of citingPapers')
    else:
        print('I am loading a new page,please be patient')
        for pageUrl in pageUrls:
            citingPapersTitles = appendPapersTitles(pageUrl,citingPapersTitles)
    return citingPapersTitles


if __name__ == '__main__':
    paperTitles = parseDocx("C:\\Users\\WinniTeo\\Desktop\\shixi\\doc\\Doc_Catalog1.docx")
    for perPaperTitle in paperTitles:
        data = crawlGoogleScholar(perPaperTitle)
        perPaperTitle = data[0]
        numQuotes = data[1]
        citingPapersUrl = data[2]
        if len(citingPapersUrl):
            citingPapersTitles = crawlCitingPapersTitles(citingPapersUrl)
            print('****************************————————————————————————————————————————————')
            print(data[0])
            print(data[1])
            print(citingPapersTitles)
            print(type(citingPapersTitles))
            print('————————————————————————————————————————————****************************\\n')
            
