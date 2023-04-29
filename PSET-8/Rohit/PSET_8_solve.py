# PSET-8
'''
Write a script that accepts the user for the input and converts all the vowels `('a','e','i','o','u')` into uppercase.
'''

#  Solution

text  = input("Enter any word: ")

while text.find("a") >=0:
    A = text.find("a")
    text = text[ : A] + text[A].upper() + text[A +1 : ]

while text.find("e") >=0:
    E = text.find("e")
    text = text[ : E] + text[E].upper() + text[E +1 : ]

while text.find("i") >=0:
    I = text.find("i")
    text = text[ : I] + text[I].upper() + text[I +1 : ]

while text.find("o") >=0:
    O = text.find("o")
    text = text[ : O] + text[O].upper() + text[O +1 : ]

while text.find("u") >=0:
    U = text.find("u")
    text = text[ : U] + text[U].upper() + text[U +1 : ]

print(text)


