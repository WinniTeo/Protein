import random
import requests


def getHeader():
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language':'zh,en-US;q=0.7,en;q=0.3',
        'Connection':'keep-alive',
        'cookie': 'SID=PAZY1LC0agoj6YQeyMf4gwgni1B2kBU9my7pR892CLkzlPgijW-VCOOwuVn-PC2A2x2GXA.; HSID=At4_xrTEWMnLfUicD; SSID=AZHvahVXJO1ms71dl; APISID=xLV3jpb8eUKublkb/AxuxZqETNt4hZIc02; SAPISID=1GVEX7X46TZGApdS/AysMlEbE6_IUtX-CL; CONSENT=YES+US.zh-CN+20180701-00-0; GSP=LD=en:CR=0:LM=1531574103:S=-Ea2-lW8yXK9wWy2; SIDCC=AEfoLeZViTmkAFPPTzKQnjcm7eH8Jc-aR4eyqqVJluc-LKaSd1MZmiOu3vhIdb--M4gbMQCoOQ; 1P_JAR=2018-7-21-2; NID=135=gdnHgUgnGeaREybXVHt3mwOrdNacN2iGF1kDFMjrQ7Pn9556ZzyU2Zu3JZaKMxyB312VjL0n6b7qnVzJNPQIIdZK9OQMY3-K0wBJCIeZwGWa2cvR00QhhQIISxHhLlpYU2YIxO14vTeJEerwwgN3RGasHpeZC0qV0QTvDBqEs49enM8QFAWLdhLER9brdGRD0tnAZHKePrdNP_P_pp9JHDwXErMO',
        'DNT':'1',
        'Host':'scholar.google.com',
        'Referer':'https://scholar.google.com/',
        'upgrade-insecure-requests':'1',
        'User-Agent': getUA(),
        'x-client-data' : 'CI22yQEIprbJAQjBtskBCKmdygEI2J3KAQiln8oBCKijygE='
    }
    return headers


def getUA():
    first_num = random.randint(55, 62)
    third_num = random.randint(0, 3200)
    fourth_num = random.randint(0, 140)

    os_type = [
                '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
                '(Macintosh; Intel Mac OS X 10_12_6)'
               ]

    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

    return ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                        '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                    )


def getCookie():
    firstHeaders = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language':'zh,en-US;q=0.7,en;q=0.3',
        'upgrade-insecure-requests':'1',
        'User-Agent': getUA()
    }
    homePage = "https://scholar.google.com/"
    response = requests.get(homePage, headers=firstHeaders)
    cookies = response.cookies.get_dict()
    return cookies


if __name__ == '__main__':
    # head = getHeader()
    # print(head)
    cookie = getCookie()
    print(cookie)