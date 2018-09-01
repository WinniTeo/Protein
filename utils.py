import re

# Random delay
import time
import random

# requests
import requests
from lxml import etree

# requests headers
from headers_class import Headers
   
"""
Random delay
"""

def delay():
    delayTime = random.uniform(1, 3)
    time.sleep(delayTime)

def requestsPage(req_url):
    delay()
    head = Headers()
    html = requests.get(req_url, headers = head.getHeader())
    return html

