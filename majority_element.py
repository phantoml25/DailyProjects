"""
Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""

def majority_element(elist):
    count = {}
    majority = len(elist)/2
    for i in elist:
        if i in count:
            count[i] = count[i]+1
            if count[i] >  majority:
                return i
        else:
            count[i] = 1
    print(count,"len: ",len(elist))
    return "Error: No element is a majority element"
            
            
print(majority_element([5,5,5,3,3,2,2,5]))