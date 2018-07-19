"""
crawl Google Scholar
"""

# crawl page
from urllib import parse

# utils
from utils import repChar, requestsScholar

from lxml import etree

def crawlGoogleScholar(paperTitle):
    #for perPaperTitle in paperTitles:
    keyword = parse.quote(paperTitle)
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
            print('citingPapersTitles:'+ citingPapersTitles)
        else:
            print('I am loading a new page,please be patient')
            for pagingUrl in pagingUrls:
                fullpagingUrl = 'https://scholar.google.com.hk' + str(pagingUrl)
                html = requestsScholar(fullpagingUrl).text
                selector = etree.HTML(html)
                addCitingPapersTitles = selector.xpath('//*[@id="gs_res_ccl_mid"]/div[1]/div[2]/h3/a/text()')
                citingPapersTitles.append(addCitingPapersTitles)
            print('Add CitingPapersTitles successfully')
            print('citingPapersTitles:' + citingPapersTitles + '\\n\\n')





if __name__ == '__main__':
    crawlGoogleScholar('Relationship between Sample Loading Amount and Peptides Identification and Its Effect on Quantitative Proteomics')