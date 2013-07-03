'''
Created on Jul 3, 2013

@author: zeroshiiro
'''
import re

N = int(input())
for i in range (0, N):
    line = input()
    m = re.search(r'hackerrank',line)
#     print(m)
    if type(m) != None :
#         print(m.start(), m.end(), len(line))
        if m.start() == 0 and m.end() == len(line) :
            print(0)
        elif m.start() == 0 and m.end() < len(line) :
            print(1)
        elif m.start() > 0 and m.end() == len(line) :
            print(2)
        else :
            print(-1)
    else :
        print(-1)
#     start = line.startswith("hackerrank")
#     end = line.endswith("hackerrank")
#     contains = re.search(r'hackerrank', line)
#     if contains != None: 
#         if start == False and end == False :
#             print(-1)
#         elif start == True and end == False :
#             print(1)
#         elif start == False and end == True :
#             print(2)
#         elif start == True and end == True :
#             print(0)
#     else :
#         print(-1)