'''
Created on Jul 3, 2013

@author: zeroshiiro
'''
import re

for i in range(0, int(input())) :
    line = input()
    if re.match(r'[hH][iI]\s[^dD]+', line) : print(line)