full_name = input("Enter your full name: ")
whitespace = full_name.find(" ")
first_name = full_name[:whitespace]
last_name = full_name[whitespace+1:]
index_last_name = whitespace+1
index_first_name = whitespace-1
print(index_last_name)
print(index_first_name)

#Answer: ( Enter your full name: Shivani Rana
# whitespace = full_name.find(" ")
# whitespace
# 7
# first_name = full_name[:whitespace]
# first_name
# 'Shivani'
# last_name = full_name[whitespace+1:]
# last_name
# 'Rana'
# index_last_name = whitespace+1
# index_first_name = whitespace-1
# print(index_last_name)
# 8
# print(index_first_name)
# 6 )
