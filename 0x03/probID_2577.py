# -*- coding: utf-8 -*-
"""
Created on Tue May 23 18:01:13 2023

@author: joshu
"""

# a = int(input())
# b = int(input())
# c = int(input()) 
a=150
b=266
c=427
prod = str(a*b*c)
nums = [0]*10
for i in prod:
    nums[int(i)] +=1
for n in nums:
    print(n)