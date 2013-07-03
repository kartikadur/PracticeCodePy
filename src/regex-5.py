'''
Created on Jul 3, 2013

@author: zeroshiiro
'''
import re

def findInTweet():
    count = 0
    for i in range(0, int(input())):
        if re.search(r"hackerrank", input(), re.I) : count+=1
    print(count)

findInTweet()