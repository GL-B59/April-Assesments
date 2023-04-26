<<<<<<< HEAD
# Prompt the user for input
text = input("Enter some text: ")

# Convert the text to leetspeak
text = text.replace('A', '4').replace('B', 'I3').replace('E', '3').replace('H', '#').replace('O', '0').replace('S', '5').replace('T', '7').replace('U', '(_)').replace('M', '/\/\')

# Print the leetspeak text
print(text)
=======
#We write a script that accepts the user for the input and converts all the vowels ('a','e','i','o','u') into uppercase.This is the continuation of PSET4. 

#Teaking the string input from user
user_input = input("Enter a string: ")
#Stroring the the vowel table which need to check anf which need to replace
vowel_table = str.maketrans('aeiou', 'AEIOU')
#This change the lower case vowels to upper care vowel
result = user_input.translate(vowel_table)
#printing the final result
print("Result:", result)

#In this code, we first prompt the user to enter a string using the input function. We then create a translation table using the str.maketrans method that maps each lowercase vowel to its uppercase equivalent. We apply this table to the input string using the translate method and assign the result to the result variable. Finally, we print the result using the print function
>>>>>>> a529a38a1254c14bfd2c085543dc42c6765638d1
