'''
Created on Jul 3, 2013

@author: zeroshiiro
'''
import re

N = int(input())
line = []
for i in range(0, N) :
    line.append(input())
T = int(input())
for i in range(0, T) :
    word = input()
    count = 0
    regx = word[0:-2] + "(ze|se)"
    for j in line:
        m = re.findall(regx, j)
        if m : count += len(m)
    print(count)