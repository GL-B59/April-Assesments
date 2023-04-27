#Solution for PSET-1
user_input=input()
find_pin=user_input.find("pin")    #This  line finds whether pin present or not
output_result=user_input[find_pin:find_pin+(len("pin"))], #gives the output
print(output_result)
