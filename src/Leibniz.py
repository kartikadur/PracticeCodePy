'''
Created on Mar 26, 2013

@author: zeroshiiro
'''

for i in range(int(input())):print('%.15f'%sum((-1.)**k/(2*k+1)for k in range(int(input()))))
