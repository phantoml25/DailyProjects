# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 15:15:53 2023

@author: Kevin

Write a program to merge two binary trees. 
Each node in the new tree should hold a value equal to the sum of the values of
    the corresponding nodes of the input trees.

If only one input tree has a node in a given position, 
the corresponding node in the new tree should match that input node.
"""

import binarytree

left = binarytree.tree()
right = binarytree.tree()

left.pprint()
right.pprint()

merged = [left[0].value+right[0].value]

i = 1

while i<len(left.values) or i<len(right.values):
    j = 0
    if i<len(left.values):
        if left.values[i] != None:
            j = j + left[i].value
    if i<len(right.values):
        if right.values[i] != None:
            j = j + right[i].value
    if j == 0:
        j = None
    merged.append(j)
    i = i+1

binarytree.build(merged).pprint()