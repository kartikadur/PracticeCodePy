'''
Created on Jul 3, 2013

@author: zeroshiiro
'''
import re
 
line = []
for i in range(0, int(input())):
    line.append(input())

for i in range(0,int(input())):
    w = "(?!\W)" + input() + "(?=\W)"
    count = 0
    for j in line:
        m = re.findall(w, j)
#        print(m)
        count += len(m)
    print(count)