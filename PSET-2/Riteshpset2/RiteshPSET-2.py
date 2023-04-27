mainstring = input("please enter string:")
substring = input("Please enter string: ")
a = mainstring.find(substring)
print(a)
output = mainstring[a:a+len(substring)] # if a is true then it will print substring or else it will stop in above line
print(output)
