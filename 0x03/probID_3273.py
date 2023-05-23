# -*- coding: utf-8 -*-
"""
Created on Tue May 23 18:49:14 2023

@author: joshu
"""

length = '10'
myList = '5 12 7 10 9 1 2 3 6 11'
x = '20'

# memory를 전부다 사용하면
answer = 0
nums= [0]*1000000
for i in myList.split():
    nums[int(i)] += 1
    if int(x)-int(i)==int(i):
        continue
    elif nums[int(x)-int(i)]:
        answer+=1
print(answer)