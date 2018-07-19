import re

# Random delay
import time
import random

# requests
import requests


"""
Replace illegal characters
"""
def repChar(character):
    pattern = u'[\\s\\\\/:\\*\\?\\\"<>\\|]'
    prog = re.compile(pattern)
    newCharacter = prog.sub('_', character)
    return newCharacter


    
"""
Random delay

"""
def delay():
    delayTime = random.uniform(1, 3)
    time.sleep(delayTime)


"""
requests package
"""
# request headers
head={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language':'zh,en-US;q=0.7,en;q=0.3',
    'Connection':'keep-alive',
    'cookie': 'GSP=LM=1531813864:S=z7n4LpZ1xXXaUaek; NID=134=BXqG0WlgnSghUf0uU3s8PsyLdqtdvyQMXmrAlAIt0UsJm0lf_xrwrEsFfTBuogYeBDKUENXYuBBj0fpNxerls8crZdznJFoXFaTHQKaX0Th9nbeDIH3hZNwebawGIINXEhF65bMGwFSGoA',
    'DNT':'1',
    'Host':'scholar.google.com',
    'Referer':'https://scholar.google.com/',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

def requestsScholar(req_url):
    delay()
    html = requests.get(req_url, headers = head)
    return html