'''# PSET-2

This is a spin-off of [PSET-1](../PSET-1/). As a continuation fetch two strings from user such that the second string is the substring of the first.

## Example

- 'pin' is a substring of 'spin'.
- 'Heal' is a substring of 'Health'.

## Tasks

- First check whether the substring is present inside the string. (Please try this without using `in` operator).
- Write a line of code such that it returns the substring from string. '''

#Solution

string = input("Enter any word: ")     #1
substring = input(" Enter any substring of entered word: ")
check = string.find(substring)
while check>=0 :
    print(f'{substring} is present inside the word {string} ')
    
    substring_1 = string[ check: check+len(substring)]      # 2
    print(f'substring = {substring}')
    check = -1

