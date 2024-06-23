# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:39:58 2023

@author: Kevin

You are given a histogram consisting of rectangles of different heights. 
These heights are represented in an input list,
    such that [1, 3, 2, 5] corresponds to the following diagram:

      x
      x  
  x   x
  x x x
x x x x

Determine the area of the largest rectangle that can be formed only from 
    the bars of the histogram. 
For the diagram above, for example, this would be six, 
    representing the 2 x 3 area at the bottom right.
"""

import random

def printHistogram(histogram:[int]):
    mHeight = max(histogram)
    for i in range(mHeight,0,-1):
        string = ""
        for j in range(len(histogram)):
            if histogram[j] >= i:
                string += "x"
            else:
                string += " "
        print(string)

def rectangleFromHistorgram(histogram: [int]):
    area = 0
    mHeight = max(histogram)
    cHeight = 1
    while cHeight<=mHeight:
        start = -1
        end = -1
        for i in range(len(histogram)):
            if start == -1:
                if histogram[i] >= cHeight:
                    start = i
            else:
                if histogram[i] < cHeight:
                    end = i
                    cArea = (end-start)*cHeight
                    if cArea>area:
                        area = cArea
                        print("start = ",start)
                        print("end = ",end)
                        print("height = ",cHeight)
                        print("area = ",area)
                        print(" ")
                    start = -1
                    end = -1
        if start != -1:
            end = len(histogram)
            cArea = (end-start)*cHeight
            if cArea>area:
                area = cArea
                print("start = ",start)
                print("end = ",end)
                print("height = ",cHeight)
                print("area = ",area)
                print(" ")
            start = -1
            end = -1
        cHeight +=1
    return area


def genHistogram(length,maximum):
    histogram = []
    for i in range(length):
        random.seed()
        histogram.append(random.randint(1, maximum))
    
    return histogram

histogram = genHistogram(10, 5)
print(histogram)
printHistogram(histogram)
print(rectangleFromHistorgram(histogram))