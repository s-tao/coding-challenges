"""
Given two strings, one is a subsequence if all of the elements of the first 
string occur in the same order within the second string. They do not have to be 
contiguous in the second string, but order must be maintained. For example, 
given the string 'I like cheese', the words ('I', 'cheese') are one possible 
subsequence of that string. Words are space delimited.

Given two strings, s and t, where t is a subsequence of s, report the words of 
s, missing in t (case sensitive), in the order they are missing.

Input: 'I like cheese', 'like'
Output: ['I', 'cheese']

Input: I am using HackerRank to improve programming → 
s = 'I am using HackerRank to improve programming'
t = 'am HackerRank to improve'

Output: 
I
using
programming
"""

def missing_word(s, t):
    s = s.split()
    t = t.split()
    
    set_sub = set(t)
    missing_list = []

    for word in s:
        if word not in set_sub:
            missing_list.append(word)
    return missing_list


print(missing_word('I like cheese', 'like')) # ['I', 'cheese']
print(missing_word('I am using HackerRank to improve programming', 'am HackerRank to improve')) # ['I', 'using', 'programming']
