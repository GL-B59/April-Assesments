string_one=input()
whitespace=string_one.find(" ")
first_name=string_one[:whitespace]
last_name=string_one[whitespace+1:]
index_last_name=whitespace+1
index_first_name=whitespace-1
print(index_last_name)
print(index_first_name)
