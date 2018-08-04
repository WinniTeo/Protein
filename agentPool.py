import random

class Proxies(object):
    def __init__(self):
        self.ipPool =['118.31.220.3:8080','180.101.205.253:8888','113.200.56.13:8010','1.71.188.37:3128']
    def getProxies(self):
        self.proxies = random.choice(self.ipPool)

