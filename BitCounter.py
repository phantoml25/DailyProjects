# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 13:12:11 2023

@author: Kevin Adams

Quick script for DailyCodingProblem

Write an algorithm that finds the total number of set bits in all integers between 1 and N.
"""

def bit_count(maximum_number):
    i = 1
    total = 0
    while i<= maximum_number :
        bit = 1
        while bit <=i:
            if (i | bit) == i: #This flips any unset bits which changes i
                total +=1
            bit = bit *2
        i+=1
    return total
    




print(bit_count(5))