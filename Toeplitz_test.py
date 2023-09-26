# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 08:59:51 2023

@author: Kevin
Write a program to determine whether a given input is a Toeplitz matrix.

In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal
    from top left to bottom right are identical.
"""
import random


input_array = [[1, 2, 3, 4, 8],
[5, 1, 2, 3, 4],
[4, 5 ,1 ,2, 3],
[7 ,4 ,5 ,1 ,2]]

test_array = [0,0,0,0,0]

def Toeplitz_test(arr)-> bool:
    for i in range(len(arr)-1):
        for j in range(len(arr[i])-1):
            if(arr[i][j] != arr[i+1][j+1]):
                return False
    return True

def Toeplitz_generate(arr_length,num_arrays): 
    ret_arr = []
    rand_gen = random.Random()
    rand_gen.seed()
    for i in range(num_arrays):
        inner_arr = []
        for j in range(arr_length):
            inner_arr.append(rand_gen.randint(1, 9))
        ret_arr.append(inner_arr)
    return ret_arr
    
input_array = Toeplitz_generate(3, 3)
while not(Toeplitz_test(input_array)):
    print(input_array)
    print("False")
    input_array = Toeplitz_generate(3, 3)
print(input_array)
print("True")
