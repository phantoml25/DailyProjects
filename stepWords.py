"""
By: Kevin Adams
A step word is formed by taking a given word, adding a letter, and anagramming the result. 
For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".

Given a dictionary of words and an input word, create a function that returns all valid step words.
"""

stepdict = ["appeal","appels","apples","applet","appley","dapple","lapped","lapper","lappet","apple","app","applest"]

def stepWords(word,dictionary):
    stepWords = []
    originWord = word.lower()
    for i in dictionary:
        current_word = i.lower()
        letter_count = 0
        for j in str(i):
            if j not in originWord:
                letter_count += 1
        if letter_count == 1:
            stepWords.append(i)
                
    
    return stepWords

print(stepWords("Apple",stepdict))