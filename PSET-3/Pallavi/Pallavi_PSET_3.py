#PSET-3
first_name=input("Enter the first_name")
last_name=input("Enter the last_name")
x = first_name.replace(' ', '')
y = last_name.replace(' ', '')

first_character_of_last_name=x[-1]
print(first_character_of_last_name)
last_character_of_the_first_name=y[0]
print(last_character_of_the_first_name)
