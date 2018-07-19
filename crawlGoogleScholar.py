"""
crawl Google Scholar
"""

# parse docx
import docx
import re

# crawl page
from urllib import parse

# utils
from utils import repChar, requestsScholar

from lxml import etree
"""
parse docx and extract title
"""
def parseDocx(fileName):
    # 获取文档对象
    docxFile = docx.Document(fileName)
    #提取标题
    paperTitles = []
    noSpot = []
    for perParagraph in docxFile.paragraphs:
        #每段文本的定义为text
        perParagraphText = perParagraph.text
        #提取后面带有数字的小数点
        rr = re.compile(r'\.\d')  #定义提取规则
        noSpot = rr.findall(perParagraphText)
        #print(none)
        #将小数点及后面的数替换为空
        for each in noSpot:
            perParagraphText = perParagraphText.replace(str(each), '')
        # 用'.'将每一个论文信息分割开，存为一个lists    
        perParagraphText = perParagraphText.split('.')
        # print(perParagraphText[1])
        paperTitles.append(perParagraphText[1])
        # print(paperTitles)
    return paperTitles




"""
crawl Google Scholar
"""
def crawlGoogleScholar(paperTitles):
    for perPaperTitle in paperTitles:
        keyword = parse.quote(perPaperTitle)
        req_url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='+keyword+'&btnG='
        html = requestsScholar(req_url).text

        selector = etree.HTML(html)
        perPaperTitle = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div[2]/h3/a/text()')
        print(perPaperTitle)
        numQuotes = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div[2]/div[3]/a[3]/text()')
        paperUrl = selector.xpath('//*[@id="gs_res_ccl_mid"]/div/div[2]/div[3]/a[3]/@href') 
        if (len(numQuotes) != 1)or(numQuotes[0] == 'Related articles'):
            print('There is no the number of quote or there is no searching result...')
        else:
            print(numQuotes)
            print(paperUrl)
            perPaperTitle = perPaperTitle
            numQuotes = numQuotes
            paperUrl = paperUrl
            citingPapersUrl = 'https://scholar.google.com.hk' + str(paperUrl[0])
            html = requestsScholar(citingPapersUrl).text
            selector = etree.HTML(html)
            citingPapersTitles = selector.xpath('//*[@id="gs_res_ccl_mid"]/div[1]/div[2]/h3/a/text()')
            pagingUrls = selector.xpath('//*[@id="gs_nml"]/a[2]')
            if len(pagingUrls)==0:
                #print(citingPapersTitles)
                print('There is only one page of citingPapers')
            else:
                print('I am loading a new page,please be patient')
                for pagingUrl in pagingUrls:
                    fullpagingUrl = 'https://scholar.google.com.hk' + str(pagingUrl)
                    html = requestsScholar(fullpagingUrl).text
                    selector = etree.HTML(html)
                    addCitingPapersTitles = selector.xpath('//*[@id="gs_res_ccl_mid"]/div[1]/div[2]/h3/a/text()')
                    citingPapersTitles.append(addCitingPapersTitles)
                print('Add CitingPapersTitles successfully')

           

            #return perPaperTitle,numQuotes,paperUrl




if __name__ == '__main__':
    paperTitles = parseDocx("C:\\Users\\WinniTeo\\Desktop\\shixi\\doc\\Doc_Catalog1.docx")
    crawlGoogleScholar(paperTitles)