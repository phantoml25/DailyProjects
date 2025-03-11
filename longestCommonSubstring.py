"""
Write a program that computes the length of the longest common subsequence of three given strings. 

A subsequence is not a consecutive substring, it is all of the letters that appear in the same order, removing any that don't

For example, given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious", 
it should return 5, since the longest common subsequence is "eieio".
"""

def longestCommon(string1,string2,string3,len1,len2,len3):
    if len1 ==0 or len2 ==0 or len3 ==0:
        print("ended a string")
        return 0
    elif string1[len1-1] == string2[len2-1] == string3[len3-1]:
        print("found a common letter, popping")
        return 1 + longestCommon(string1,string2,string3,len1-1,len2-1,len3-1)
    else:
        print("removing letters")
        return max(max(
            longestCommon(string1,string2,string3,len1-1,len2,len3),
            longestCommon(string1,string2,string3,len1,len2-1,len3)),
            longestCommon(string1,string2,string3,len1,len2,len3-1)
        )  

st1 = "jealouslly"
st2 = "sully"
st3 = "sally"

print(longestCommon(st1, st2, st3,len(st1),len(st2),len(st3)))