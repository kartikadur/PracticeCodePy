'''
Created on Jul 3, 2013

@author: zeroshiiro
'''
import re
 
line = []
for i in range(0, int(input())):
    line.append(input())

for i in range(0,int(input())):
    count = 0
    w = input()
    for j in line:
        m = re.findall(r"(?<!\w)" + w + "(?!\w)", j)
        count += len(m)
    print(count)