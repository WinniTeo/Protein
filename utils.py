import re

# Random delay
import time
import random


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
