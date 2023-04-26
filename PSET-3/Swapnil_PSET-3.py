#Solution for PSET-3
print("Enter Name")
string_one=input()
whitespace=string_one.find(" ")
first_name=string_one[:whitespace]
last_name=string_one[whitespace+1:]
index_last_name=whitespace+1
index_first_name=whitespace-1
print(f"index of first character of last name is : {index_last_name}")
print(f"last character of the first name is {index_first_name}")