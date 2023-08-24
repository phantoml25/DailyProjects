# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:47:16 2022

@author: kadam

Implement a queue using two stacks. 
Recall that a queue is a FIFO (first-in, first-out) data structure with 
the following methods: 
    enqueue, which inserts an element into the queue, 
    and dequeue, which removes it.
"""

Stack1 = []
Stack2 = []
length =0

def enqueue(item):
    global length
    Stack1.append(item)
    length +=1
    
    
def dequeue():
    global length
    for x in range(length):
        Stack2.append(Stack1.pop())
    front = Stack2.pop()
    length -=1
    for x in range(length):
        Stack1.append(Stack2.pop())
    return front


enqueue(5)
enqueue(6)
enqueue(8)
enqueue(7)
enqueue(9)


print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())