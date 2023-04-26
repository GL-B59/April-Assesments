full_name = input("Enter your full name: ")
first_name = full_name[:full_name.index(" ")].strip()
last_name = full_name[full_name.index(" ")+1:].strip()
# Print the first name and last name
print("First Name:", first_name)
print("Last Name:", last_name)

