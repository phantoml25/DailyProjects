# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:51:22 2023

@author: Kevin M. Adams Arredondo
Given integers M and N, write a program that counts how many positive integer pairs
    (a, b) satisfy the following conditions:

    a + b = M
    a XOR b = N
"""
import random

def xor(a, b):
    return a^b

def PairCount(m:int,n:int):
    count = 0
    i = 1
    while i<(m/2)+1:
        j = m-i
        print(i," XOR ",j," = ",xor(i, j))
        if xor(i,j)==n:
            count+=1
        i+=1
    return count

def mnGen():
    random.Random().seed()
    m = random.randint(10,100)
    n = random.randint(1, m)
    return m,n


m,n = mnGen()
print("a+b =",m," and a XOR b = ",n)
print("Number of positive integer pairs: ",PairCount(m,n))