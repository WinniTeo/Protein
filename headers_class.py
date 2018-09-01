import random
import requests
import json

class Headers(object):
    def __init__(self):
        self.cookies, self.userAgent = self.getCookie()
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language':'zh,en-US;q=0.7,en;q=0.3',
            'Connection':'keep-alive',
            'cookie': self.cookies,
            'DNT':'1',
            'Host':'scholar.google.com',
            'Referer':'https://scholar.google.com/',
            'upgrade-insecure-requests':'1',
            'User-Agent': self.userAgent,
            'x-client-data' : 'CI22yQEIprbJAQjBtskBCKmdygEI2J3KAQiln8oBCKijygE='
        }

    def getHeader(self):
        self.randromNum = random.random()  # random number from 0 to 1
        if self.randromNum > 0.8:
            self.cookies, self.userAgent = self.getCookie()
            
            self.headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language':'zh,en-US;q=0.7,en;q=0.3',
                'Connection':'keep-alive',
                'cookie': self.cookies,
                'DNT':'1',
                'Host':'scholar.google.com',
                'Referer':'https://scholar.google.com/',
                'upgrade-insecure-requests':'1',
                'User-Agent': self.userAgent,
                'x-client-data' : 'CI22yQEIprbJAQjBtskBCKmdygEI2J3KAQiln8oBCKijygE='
            }
        return self.headers

        
    def getUA(self):
        self.first_num = random.randint(55, 68)
        self.third_num = random.randint(0, 3440)
        self.fourth_num = random.randint(0, 140)

        self.os_type = [
                    '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
                    '(Macintosh; Intel Mac OS X 10_12_6)'
                ]

        self.chrome_version = 'Chrome/{}.0.{}.{}'.format(self.first_num, self.third_num, self.fourth_num)

        self.userAgent = ' '.join(['Mozilla/5.0', random.choice(self.os_type), 'AppleWebKit/537.36',
                            '(KHTML, like Gecko)', self.chrome_version, 'Safari/537.36']
                        )
        return self.userAgent


    def getCookie(self):
        self.userAgent = self.getUA()
        self.firstHeaders = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language':'zh,en-US;q=0.7,en;q=0.3',
            'upgrade-insecure-requests':'1',
            'User-Agent': self.userAgent
        }
        self.homePage = "https://scholar.google.com/"
        # self.proxies = Proxies()
        # , proxies = self.proxies.getProxies()
        self.response = requests.get(self.homePage, headers=self.firstHeaders)
        self.cookiesDict = self.response.cookies.get_dict()
        self.cookies = json.dumps(self.cookiesDict)
        return self.cookies, self.userAgent

