#Solution for PSET-1
user_input=input()
find_pin=user_input.find("pin")    #This line finds whether pin present or not
output_result=user_input[find_pin:find_pin+(len("pin"))]
print(output_result)



#Another Solution for PSET-1
user_input=input()
print(user_input[user_input.find("pin"):user_input.find("pin")+(len("pin"))])