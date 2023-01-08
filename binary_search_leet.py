# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:19:06 2023

@author: user
"""

class Solution:
    def search(self, nums: list, target: int) -> int:
        for i,j in enumerate(nums):
            if j==target:
                return i
            else:
                k=[]
                k.append(0)
        if k:
            return -1
        
        
k=Solution()
m=k.search([0,2,4,5,7],4)
print(m)