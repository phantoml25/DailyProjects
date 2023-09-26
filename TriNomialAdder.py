# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:21:47 2023

@author: Kevin

Given an array of numbers and a number k, 
determine if there are three entries in the array which add up to the specified number k. 

For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.
Numbers are integers but can be negative
"""

import random

def arrayCheck(arr:[],k):
    filteredArray = []
    #these initializers ensure arrays with no 0's don't hit an edge case
    lowest = arr[0]
    secondLowest = arr[1] 
    #the next two loops give us our 2 lowest numbers, allowing negative numbers to be included
    #this makes it easy to check for positive numbers that are larger than k
    for i in range(len(arr)):
        if arr[i] < lowest:
            secondLowest = lowest
            lowest = arr[i]
    for i in range(len(arr)):
        if arr[i] + lowest + secondLowest ==k: #this will allows a+b+a/a+b+b edge cases through
            print(arr[i],"+",lowest,"+",secondLowest,"!=", k)
            return True #catch early success
        elif (arr[i] + lowest + secondLowest) <k:
            filteredArray.append(arr[i])
    #implement modified binary sort, sort 
    if len(filteredArray) <3:
        print("Not enough valid items")
        return False
    elif len(filteredArray) == 3:
        if filteredArray[0]+filteredArray[1]+filteredArray[2] == k:
            print(filteredArray[0],"+",filteredArray[1],"+",filteredArray[2],"=", k)
            return True
        else: 
            print(filteredArray[0],"+",filteredArray[1],"+",filteredArray[2],"!=", k)
            return False
    filteredArray = sorted(filteredArray)
    ai = 0
    bi = len(filteredArray)-1
    ci = 1
    a = filteredArray[ai]
    b = filteredArray[bi]
    c = filteredArray[ci]
    
    #count the top number down if nothing was hit
    while bi>ai+2:
        #run through the sorted list, moving a and c closer to B. 
        while ai < bi-2:
            while a + b + c < k & ci < bi-1:
                ci += 1
                c = filteredArray[ci]
                if a+b+c == k:
                    print(a,"+",b,"+",c,"=",k)
                    return True
                else:
                    print(a,"+",b,"+",c,"!=",k)
            ai +=1
            ci = ai+1
            a = filteredArray[ai]
            c = filteredArray[ci]
            if a+b+c == k:
                print(a,"+",b,"+",c,"=",k)
                return True
            else:
                print(a,"+",b,"+",c,"!=",k)
        #after first run, b=len, c=len-1,a=len-2, if these cannot make k no items can
        if a+b+c<k:
            print("Numbers in array cannot reach target ",k,", max 3 numbers are ",a,b,c)
            return False
        ai = 0
        bi -=1
        ci = ai+1
        a = filteredArray[ai]
        b = filteredArray[bi]
        c = filteredArray[ci]
        if a+b+c == k:
            print(a,"+",b,"+",c,"=",k)
            return True
        else:
            print(a,"+",b,"+",c,"!=",k)
    return False
    
def genList(length,minimum,maximum):
    random.seed()
    retList = []
    for i in range(length):
        retList.append(random.randint(minimum,maximum))
    return retList

generatedList = genList(100,-100,100)
print(generatedList)
print(arrayCheck(generatedList, -29))
    