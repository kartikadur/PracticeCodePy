'''
Created on Jul 3, 2013

@author: zeroshiiro
'''
import re

for i in range(0, int(input())) :
#    print(input())
    if re.match(r'[A-Z]{5}[0-9]{4}[A-Z]', input()) : print("YES")
    else : print("NO")
    