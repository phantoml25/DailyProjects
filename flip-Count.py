# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:03:49 2023

@author: Kevin
You are given a string consisting of the letters x and y, such as xyxxxyxyy. 
In addition, you have an operation called flip, 
    which changes a single x to y or vice versa.

Determine how many times you would need to apply this operation to ensure that 
    all x's come before all y's. In the preceding example, 
    it suffices to flip the second and sixth characters, so you should return 2.
"""
import random

def flip(arr:[],pos:int):
    if arr[pos] == 'x':
        arr[pos] = 'y'
    else:
        arr[pos] = 'x'
    return arr

def flipCount(arr:[]):
    xCount = str.count(arr, 'x')
    yCount = len(arr)-xCount
    print("number of X's: ",xCount)
    print("number of Y's: ",yCount)
    
    if xCount < (len(arr)/2):
        return xCount
    else:
        return yCount
    
def xyGen():
    random.Random().seed()
    s = ""
    for i in range(random.randint(2, 20)):
        if random.randint(0, 1) == 0:
            s = s+"x"
        else:
            s = s+"y"
    return s

s = xyGen()
print(s)
print(flipCount(s))