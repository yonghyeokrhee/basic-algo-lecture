# -*- coding: utf-8 -*-
"""
Created on Tue May 23 18:20:38 2023

@author: joshu
"""
from collections import Counter

myList = Counter('69696')
# todo: python 구현
myList[6] = (myList[6] + myList[9])//2 +  (myList[6] + myList[9])%2
del myList[9]
print(myList)
print(int(max(myList)))
