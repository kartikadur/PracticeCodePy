'''
Created on Jul 5, 2013

@author: zeroshiiro
'''
from collections import *
import re

lineCollection = defaultdict(int)

def getLines(N):
    for i in range(0, N):
        for word in input().split(" "):
            lineCollection[word]+=1

def findSubString(N):
    for i in range(0,N):
        word = input()
        count = 0
        for key, value in lineCollection.items():
            m = re.search(r"(?<=\w)" + word + "(?=\w)", key)
            if m != None :
                if m.start() > 0 and m.end() < len(key) :
                    count += lineCollection[key]
        print(count)

getLines(int(input()))
findSubString(int(input()))