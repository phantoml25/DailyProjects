"""
    You are given a starting state 'start', a list of transition probabilities for a Markov chain, and a number of steps 'num_steps'. 
    Run the Markov chain starting from 'start' for 'num_steps' and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]

One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
    
"""

import random

def MarkovChain(start,num_steps):
    results = {'a':0,'b':0,'c':0}
    current = start
    probs = {
        'a': [0.9,0.075,0.025],
        'b': [0.15,0.8,0.05],
        'c': [0.25,0.25,0.5]
    }
    states = ['a','b','c']
    i = 0
    while i<num_steps:
        current = random.choices(
            states,probs[current[0]],k=1
        )
        results[current[0]]+=1
        i+=1
    
    
    return results


print(MarkovChain('a',5000))