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

#fetch the parameter
import sys


"""
parse docx and extract title
"""
def parseDocx(fileName):
    """抓取do

    获取文档中每段的论文信息。将影响分割结果的数字前的英文符号'.'去除。以英文字符
    '.'分割作者，论文题目以及其他信息。提取列表中的第个元素即为论文标题。

    Args:
        docxFile: 论文文档
        paperTitles: 保存论文标题的list
        noSpot: 需要在段落中去除的部分，即数字前面的小数点以
            及这一位数字
        perParagraph: 每一段的论文
        perParagraphText: 每一段的论文文本
        rr: 匹配需要删去的文本的规则

    Returns:
        一个包含文档中所有论文名称的list
    """
    docxFile = docx.Document(fileName)
    paperTitles = []
    noSpot = []
    for perParagraph in docxFile.paragraphs:
        perParagraphText = perParagraph.text
        rr = re.compile(r'\.\d') 
        noSpot = rr.findall(perParagraphText)
        for each in noSpot:
            perParagraphText = perParagraphText.replace(str(each), '') 
        perParagraphText = perParagraphText.split('.')
        paperTitles.append(perParagraphText[1])
    return paperTitles


"""
crawl Google Scholar
"""
def crawlGoogleScholar(perPaperTitle):
    """爬取论文标题、论文引用次数及其链接

    将论文标题进行html的url编码，生成完整的请求链接。对GoogleScholar进行请求，获
    取网页完整的html。使用etree.HTML对网页进行解析。通过xpath提取目标内容————论
    文标题、论文引用次数及其链接。谷歌学术的反爬虫做的很好，会出现爬取不到内容的情
    况和搜不到文章的情况，我们根据爬取的返回值确定返回值的内容。当获取的引用次数不
    为一或者为Related articles时就是无效的数据，返回为空，反之，返回爬取的论文标
    题、论文引用次数及其链接。

    Args:
        keyword: 解析后的url的关键词
        req_url: 网页请求的链接
        html: 请求成功的网页
        selector: 解析后的网页
        perPaperTitle: 论文标题
        numQuotes: 引用次数
        citingPapersUrl: 引用次数的跳转链接

    Returns:
        论文标题、论文引用次数及其链接，这是一个tuple
    """
    keyword = parse.quote(perPaperTitle)
    req_url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='+keyword+'&btnG='
    html = requestsPage(req_url).text
    selector = etree.HTML(html)
    perPaperTitle = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div[2]/h3/a/text()')
    numQuotes = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div[2]/div[3]/a[3]/text()')
    citingPapersUrl = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div[2]/div[3]/a[3]/@href')
    if (len(numQuotes) != 1)or(numQuotes[0] == 'Related articles'):
        print('There is no the number of quote or there is no searching result...')
        return [],[],[]
    else:
        return perPaperTitle[0],numQuotes[0],citingPapersUrl[0]


"""
crawl Citing Papers Titles
"""
def crawlCitingPapersTitles(citingPapersUrl):
    """爬取引用文章的标题

    生成完整的请求链接，对GoogleScholar进行请求，获取网页完整的html，使用
    etree.HTML对网页进行解析。通过xpath提取目标内容————论文标题和翻页链接。当翻
    页链接为空时，提示：There is only one page of citingPapers。当翻页链接不为
    空时，提示：I am loading a new page,please be patient。同时遍历翻页链接，
    对论文标题列表进行追加，最后返回完整的论文标题列表。

    Args:
        citingPapersUrl: 解析后的url的关键词
        html: 请求成功的网页
        selector: 解析后的网页
        citingPapersTitles: 
        pageUrls: 翻页链接列表
        pageUrl: 单个翻页链接
        perPaperTitle: 论文标题
        numQuotes: 引用次数
        citingPapersTitles: 引用论文的所有论文标题

    Returns:
        引用论文的所有论文标题，这是一个list
    """
    citingPapersUrl = 'https://scholar.google.com.hk' + citingPapersUrl
    html = requestsPage(citingPapersUrl).text
    selector = etree.HTML(html)
    citingPapersTitles = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div/h3/a/text()')
    pageUrls = selector.xpath('//*[@id="gs_nml"]/a/@href')
    if len(pageUrls)==0:
        print('There is only one page of citingPapers')
    else:
        print('I am loading a new page,please be patient')
        for pageUrl in pageUrls:
            citingPapersTitles = appendPapersTitles(pageUrl,citingPapersTitles)
    return citingPapersTitles



if __name__ == '__main__':
    absolutePathOfTheFile = sys.argv[1]
    paperTitles = parseDocx(absolutePathOfTheFile)
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
            print(len(citingPapersTitles))
            print('————————————————————————————————————————————****************************')
            
