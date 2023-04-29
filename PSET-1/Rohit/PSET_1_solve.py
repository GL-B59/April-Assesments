# PSET-1
''''
Consider the following words:

- 'spinach'
- 'unpinch'
- 'hoping'
- 'pink'
- 'ping'
- 'respin'
- 'legspin'

Write a line of code such that it returns `'pin'` when each of thsese are stored in a variable. (A single line of code has to work for all.)
'''
# Solution

word = "spinach"
print(word[word.find("pin"):word.find("pin")+3])


    

