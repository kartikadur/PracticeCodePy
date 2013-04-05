'''
Created on Apr 5, 2013

@author: zeroshiiro
'''

N = [int(i) for i in input().strip().split()]
Arr = [int(i) for i in input().strip().split()]

Arr.sort()
count = 0
i = 0
j = 1
while(j < len(Arr)):
    if(Arr[j] - Arr[i] == N[1]):
        count += 1
        j += 1
        i += 1
    elif(Arr[j] - Arr[i] < N[1]):
        j += 1
    else: i += 1
print(count)