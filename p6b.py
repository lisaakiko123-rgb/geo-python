#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:06:17 2024

@author: lisaiizuka
"""

import random

def select_r(lis, k):
    #base case: if the list only has one element
    if len(lis) == 1:
        return lis[0]
    #choose a random index as the splitter
    n = len(lis)
    i = random.randint(0,n-1) 
    splitter = lis[i]
    #partition into 2 groups
    little_vals = []
    big_vals = [] 
    for j in range(n):
        if lis[j]<lis[i]:
            little_vals.append(lis[j])
        elif lis[j]>=lis[i] and j!=i:
            big_vals.append(lis[j])
    #decide where thekth small value lies
    if k<len(little_vals):
        #recurse on little_vals
        return select_r(little_vals, k)
    elif k == len(little_vals):
        #the spliter is the kth smallest
        return splitter
    else:
        return select_r(big_vals, k-len(little_vals)-1)
    
def my_median(lis):
    if len(lis)%2 != 0:
        median = select_r(lis, (len(lis)/2)-1)
    else:
        median = (select_r(lis, len(lis) // 2 - 1) + select_r(lis, len(lis) // 2)) / 2
    return median
              

def select_m(lis, k):
    if len(lis) == 1:
        return lis[0]
    #set middle splitter
    n = len(lis)
    mid = n//2
    middle_splitter = lis[mid]
    little_vals = []
    big_vals = [] 
    for j in range(n):
        if lis[j]<middle_splitter:
            little_vals.append(lis[j])
        elif lis[j]>=lis[mid] and j!=mid:
            big_vals.append(lis[j])
    if k<len(little_vals):
        return select_m(little_vals, k)
    elif len(little_vals) == k:
        return middle_splitter
    else:
        return select_m(big_vals, k-len(little_vals)-1)
    

    
    
    