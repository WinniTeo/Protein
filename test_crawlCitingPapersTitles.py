"""
crawl Google Scholar
"""

# crawl page
from urllib import parse

# utils
from utils import repChar, requestsScholar,requestsPage

from lxml import etree
    
def crawlCitingPapersTitles(perPaperTitle=[],numQuotes=[],paperUrl=[]):
    if paperUrl != []:
        citingPapersUrl = 'https://scholar.google.com.hk' + str(paperUrl[0])
        html = requestsPage(citingPapersUrl)
        print('Jump success')
        citingPapersTitles = html.xpath('//*[@id="gs_res_ccl_mid"]/div[1]/div[2]/h3/a/text()')
        #print(citingPapersTitles)
        pagingUrls = html.xpath('//*[@id="gs_nml"]/a[2]')
        if len(pagingUrls)==0:
            #print(citingPapersTitles)
            print('There is only one page of citingPapers')
            #print('citingPapersTitles:'+ str(citingPapersTitles))
        else:
            print('I am loading a new page,please be patient')
            for pagingUrl in pagingUrls:
                fullpagingUrl = 'https://scholar.google.com.hk' + str(pagingUrl)
                html = requestsPage(fullpagingUrl) 
                print('successfully..................')          
                addCitingPapersTitles = html.xpath('//*[@id="gs_res_ccl_mid"]/div[1]/div[2]/h3/a/text()')
                citingPapersTitles.append(addCitingPapersTitles)
            print('Add CitingPapersTitles successfully')
            print('citingPapersTitles:' + citingPapersTitles + '\\n\\n')





if __name__ == '__main__':
    #data = crawlGoogleScholar('A new insight into the impact of different proteases on SILAC quantitative proteome of the mouse liver')
    # perPaperTitle=data[0]
    # numQuotes=data[1]
    # paperUrl=data[2]
    paperUrl='https://scholar.google.com.hk/scholar?cites=8478936731913995607&as_sdt=2005&sciodt=0,5&hl=zh-CN'  
    crawlCitingPapersTitles(paperUrl = paperUrl)


