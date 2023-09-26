# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 09:02:25 2022

@author: kadam

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster 
    than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 
    (the index of 8 in the array).

You can assume all the integers in the array are unique.
"""

import numpy as np
from time import perf_counter

def gen_list(item_list,num = 1000):
    x = 0
    np.random.seed()
    for i in range(num):
        item_list.append(x)
        x += np.random.randint(1,3)
        if i%100 == 0:
            print("{:.4%} done generating list".format(i/num))
    return item_list

def item_finder(item_list,item):
    n = 0
    low = 0
    high = len(item_list)
    if item_list[n] == item:
        return n
    elif item_list[n] > item && item_list[low] < item:
        n = int(3*(len(item_list)/4))
        low = int(len(item_list)/2)
    elif item_list[n] < item :
        n = int(1*(len(item_list)/4))
        high = int(len(item_list)/2)
    
    if item_list[low] > item_list[high]: #checking if rotation has affected our split area
        if item_list[low] > item: #bottom end of rotated area not needed
            x = low    
            while item_list[x] > item_list[high]: #discard all rotated area
                x = int((x + high)/2)
    
    return n

def linear_find(item_list,item):
    x = 0
    while item_list[x] != item:
        x +=1
    return x

def rotate_list(item_list):
    np.random.seed()
    x = np.random.randint(1,len(item_list))
    item_list = item_list[x:] + item_list[:x]
    return item_list

item_list = []
item_list = gen_list(item_list,100000)
item = 7

item_list = rotate_list(item_list)

start = perf_counter()
print(item_finder(item_list, item))
print(perf_counter() - start)

start = perf_counter()
print(linear_find(item_list, item))
print(perf_counter() - start)