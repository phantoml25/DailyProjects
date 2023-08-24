# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 08:53:52 2022

@author: kadam

Implement integer exponentiation. That is, implement the pow(x, y) function, 
    where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""
import numpy as np

#return x^y
def pow(x: int, y: int) -> int:
    xy = 1
    while (y > 0):
        last_bit = (y & 1)
        # Check if current LSB
        # is set
        if (last_bit):
            xy = xy * x
        x = x * x
        
        # Right shift
        y = y >> 1
    
    return xy

x = np.random.randint(1,15)
y = np.random.randint(1,15)

print(x)
print(y)
print(pow(x, y))