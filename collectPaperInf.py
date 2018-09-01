"""
crawl Google Scholar
"""

# crawl page
from urllib import parse

# utils
from utils import requestsPage

# parse html
from lxml import etree

"""
crawl Google Scholar
"""
def crawlGoogleScholar(paperTitle):
    """爬取论文标题、论文引用次数及其链接

    将论文标题进行html的url编码，生成完整的请求链接。对GoogleScholar进行请求，获
    取网页完整的html。使用etree.HTML对网页进行解析。通过xpath提取目标内容————论
    文标题、论文引用次数及其链接。谷歌学术的反爬虫做的很好，会出现爬取不到内容的情
    况和搜不到文章的情况，我们根据爬取的返回值确定返回值的内容。当获取的引用次数不
    为一或者为Related articles时就是无效的数据，返回为空，反之，返回爬取的论文标
    题、论文引用次数及其链接。

    Args:
        keyword: 
        req_url: 
        html: 
        selector: 
        perPaperTitle: 论文标题
        numQuotes: 引用次数
        citingPapersUrl: 引用次数的跳转链接

    Returns:
        类型：tuple
        值：论文引用次数、论文引用链接
        示例：(142, "https://example.com")
    """
    # 解析后的url的关键词
    keyword = parse.quote(paperTitle)
    # 网页请求的链接
    req_url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='+keyword+'&btnG='
    # 请求网页响应
    html = requestsPage(req_url).text
    # xpath解析网页
    selector = etree.HTML(html)
    citeNumber = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div[2]/div[3]/a[3]/text()')
    citingPapersUrl = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div[2]/div[3]/a[3]/@href')
    # 通过搜索结果条数和内容，判断获取结果是否正确
    if (len(citeNumber) != 1)or(citeNumber[0] == 'Related articles'):
        print('There is no the number of quote or there is no searching result...')
        return [],[]
    else:
        return citeNumber[0],citingPapersUrl[0]


"""
crawl Citing Papers Titles
"""
def crawlCitingPapersTitles(citingPapersUrl):
    """爬取引用文章的标题

    生成完整的请求链接，对GoogleScholar进行请求，获取网页完整的html，使用
    etree.HTML对网页进行解析。通过xpath提取目标内容————论文标题和翻页链接
    。当翻页链接不为空时，遍历翻页链接，调用appendPapersTitles()函数对论
    文标题列表进行追加，最后返回完整的论文标题列表。

    Args:
        citingPapersUrl: 引用数目的翻页链接

    Returns:
        类型：list
        值：引用论文的所有论文标题
        示例：['标题一','标题二','标题三']
    """
    citingPapersUrl = 'https://scholar.google.com.hk' + citingPapersUrl
    # 解析网页
    html = requestsPage(citingPapersUrl).text
    selector = etree.HTML(html)
    citingPapersTitles = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div/h3/a/text()')
    pageUrls = selector.xpath('//*[@id="gs_nml"]/a/@href')
    # 通过翻页链接是否存在，判断是否翻页
    if pageUrls:
        for pageUrl in pageUrls:
            citingPapersTitles = appendPapersTitles(pageUrl,citingPapersTitles)
    return citingPapersTitles


def appendPapersTitles(pagingUrl,citingPapersTitles):
    """追加引用文章的标题

    生成完整的请求链接，对GoogleScholar进行请求，获取网页完整的html，使用
    etree.HTML对网页进行解析。通过xpath提取目标内容————论文标题。将获得的
    论文标题追加到前一页的论文标题之后，返回结果

    Args:
        citingPapersUrl: 引用数目的翻页链接

    Returns:
        类型：list
        值：引用论文的所有标题
        示例：['标题一','标题二','标题三']
    """
    fullPageUrl = 'https://scholar.google.com.hk' + pagingUrl
    html = requestsPage(fullPageUrl).text
    selector = etree.HTML(html)        
    addCitingPapersTitles = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div/h3/a/text()')
    citingPapersTitles = citingPapersTitles + addCitingPapersTitles
    return citingPapersTitles


def collectPaperInf(paperTitle):
    """获取引用数和引用文章标题

    调用crawlGoogleScholar()函数获取论文引用次数和论文引用链接。当引用文
    章链接不为空，调用crawlCitingPapersTitles()函数获取全部引用论文标题，
    最后返回所需的论文引用次数和引用论文标题

    Args:
        citingPapersUrl: 引用数目的翻页链接

    Returns:
        类型：tuple
        值：论文引用次数，引用论文标题
        示例：(20,('标题一','标题二','标题三'))
    """
    data = crawlGoogleScholar(paperTitle)
    citeNumber = data[0]
    citingPapersUrl = data[1]
    if len(citingPapersUrl):
        citingPapersTitles = crawlCitingPapersTitles(citingPapersUrl)
        print('****************************————————————————————————————————————————————')
        print(citeNumber)
        print(citingPapersTitles)
        print(len(citingPapersTitles))
        print('————————————————————————————————————————————****************************')
        return citeNumber,citingPapersTitles
    else:
        return [],[]
