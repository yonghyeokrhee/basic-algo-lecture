# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:50:09 2023

@author: joshu
"""

# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# alphabet_list = list()
# ps = 'aaazzz'

    
# for i in range(ord('a'), ord('z') + 1):
    letter = chr(i)
#     cnt = 0
#     for p in ps:
#         if alphabet[i] == p:
#             cnt += 1
        
#     alphabet_list.append(cnt)

# print(' '.join(str(x) for x in alphabet_list))

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_list = [0]*26
ps=input()
for p in ps:
    alphabet_list[ord(p)-ord('a')] += 1
print(' '.join(str(x) for x in alphabet_list))
