#pset3
str1= input(" Please enter your fullname with space: ")
b = str1.find(" ") # find whitespaces
first_name = str1[:b]
last_name = str1[b:]
print(f" the first name is {first_name}")
print(f" the last name is {last_name}")
a = first_name.rindex(first_name[-1])
print(f" the index of last character of the first name is {a}")
b = last_name.index(first_name[0:0])
print(f" the index of first character of the last name is {b}")
