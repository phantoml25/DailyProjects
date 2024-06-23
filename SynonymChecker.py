# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:37:10 2023

@author: Kevin

You are given a set of synonyms, such as (big, large) and (eat, consume). 
Using this set, determine if two sentences with the same number of words are equivalent.

For example, the following two sentences are equivalent:

    "He wants to eat food."
    "He wants to consume food."

Note that the synonyms (a, b) and (a, c) do not necessarily imply (b, c): 
    consider the case of (coach, bus) and (coach, teacher).

Follow-up: what if we can assume that (a, b) and (a, c) do in fact imply (b, c)?
"""

synonyms = [("big","large"),("eat","consume"),("wants","desires")]

def sentenceCompare(sent1,sent2):
    sentList1 = sent1.split(" ")
    sentList2 = sent2.split(" ")
    
    for i in range(len(sentList1)):
        if sentList1[i] != sentList2[i]:
            syns = False
            for j in range(len(synonyms)):
                if sentList1[i] in synonyms[j]:
                    if sentList2[i] in synonyms[j]:
                        print("Found Synonyms")
                        syns = True
            if syns == False:
                print("Found incompatible words ",sentList1[i]," ",sentList2[i])
                return False
            
    
    return True

print(sentenceCompare("He wants to eat food.","He desires to consume food."))