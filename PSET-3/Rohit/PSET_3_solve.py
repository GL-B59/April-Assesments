'''# PSET-3

Given a string that contains the name of a person along with whitespaces.

## Tasks

Write a code such that it splits the first name and last name and assigns them to variables `first_name` and `last_name` without any whitespace. Don't use `.split` and `.partition` methods.

**Steps**

- Remove the whitespaces.
- Find index of first character of last name and last character of the first name.
'''

#  solution

name = "     Narendra Modi               "
name = name.strip()
first_name = name[ : 8]
last_name = name[9 : ]

print(f'First Name= {first_name}')
print(f'Last Name= {last_name}')
