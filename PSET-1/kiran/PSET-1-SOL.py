#assessment PSET-1

user_input=input()
find_pin=user_input.find("pin")    #this code to find the pin
output_result=user_input[find_pin:find_pin+(len("pin"))] #gives the ouput
print(output_result)

