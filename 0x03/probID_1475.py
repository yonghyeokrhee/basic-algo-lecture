# -*- coding: utf-8 -*-
"""
Created on Tue May 23 18:20:38 2023

@author: joshu
"""

a = '69696'
myList = [0] * 10
for i in a:
    myList[int(i)] +=1
myList[6] = (myList[6] + myList[9])//2 +  (myList[6] + myList[9])%2
del myList[9]
print(myList)
print(int(max(myList)))