"""
crawl Google Scholar
"""

# parse docx
import docx
import re

# crawl page
import requests
from urllib import parse

# utils
from utils import delay, repChar


# request headers
head={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language':'zh,en-US;q=0.7,en;q=0.3',
    'Connection':'keep-alive',
    'cookie': 'NID=134=JNk5_z1gbwUI3Jxzn8d4tEaJGzwe-4ykbk7GAMw-H-DS8PjmjldzW9nVLNyBWwQnHclW08x3-QNg8M8Ys4T9yFVLog8ZJQGvXTZ7UkjnKVFERuUqVeZnJbm8JWcwF_T0VywVxdvYNuS1hggU-HKX; 1P_JAR=2018-7-16-7; GSP=A=mlDb0Q:CPTS=1531726211:LM=1531726211:S=gdmmbmbj1A_04IvV',
    'DNT':'1',
    'Host':'scholar.google.com',
    'Referer':'https://scholar.google.com/',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


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
    delay()
    for perPaperTitle in paperTitles:
        keyword = parse.quote(perPaperTitle)
        req_url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='+keyword+'&btnG='
        # print(req_url)
        html = requests.get(req_url, headers = head).text

        filePath = 'C:\\Users\\WinniTeo\\Desktop\\shixi\\doc\\html'
        perPaperTitle = repChar(perPaperTitle)
        fullFileName = filePath + perPaperTitle + '.html'
        with open(fullFileName, 'w', encoding='utf-8') as f:
            f.write(html)

"""
Extract useful information
"""
def extractUsefulInformation(html):


    

if __name__ == '__main__':
    paperTitles = parseDocx("C:\\Users\\WinniTeo\\Desktop\\shixi\\doc\\Doc_Catalog.docx")
    crawlGoogleScholar(paperTitles)