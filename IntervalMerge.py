""" 
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

My Solution:
Implement an insertion sort that combines the merging of intervals during the sorting process
"""



def insertion_sort_and_merge(array):
    # start at the first index and iterate through to the end
    i = 1
    while(i < len(array)):
        currentIndex = i
        # Check:
        #      1. that currentIndex is at least 1
        #      2. that the first item in the tuple directly before the currentIndex is greater than the first item in the tuple at currentIndex
        #
        # If both conditions are met, swap the indexes
        
        while (currentIndex > 0 and array[currentIndex - 1][0] > array[currentIndex][0]):
            temp = array[currentIndex]
            array[currentIndex] = array[currentIndex - 1]
            array[currentIndex - 1] = temp
            currentIndex -= 1
        
        i += 1
    i = 0
    while (i<len(array)):
        j = 0
        # Check:
        #      1. that currentIndex is less than len-1
        #      2. that the second item in the tuple at currentIndex is greater than or equal to the first item in the tuple directly after currentIndex
        # If condition is met, merge the two tuples, keeping currentindex[0] and nextIndex[1], reducing list length
        # Finally, Check:
        #      1. that currentIndex is at least 1
        #      2. that the second item in the tuple directly before the currentIndex is greater than or equal to the first item in the tuple at currentIndex
        # If the condition is met, merge the two tuples, keeping prevIndex[0] and currentIndex[1], reducing list length

        #now Check merge current and next
        if i<len(array)-1 and array[i][1] >= array[i+1][0]:
            array[i] = (array[i][0],array[i+1][1])
            array.remove(array[i+1])
            j+=1
        
        #Now check merge prev and current
        if i>0 and array[i-1][1] >= array[i][0]:
            array[i-1] = (array[i-1][0],array[i][1])
            array.remove(array[i])
            j+=1
        i+=1-j
    return array
        
LT_data = [(1,3),(3,4),(5,7),(2,3),(6,10)]
expOut = [(1,4),(5,10)]
print(LT_data)
LT_OUT = insertion_sort_and_merge(LT_data)
print(LT_OUT)
print(expOut)