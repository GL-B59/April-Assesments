user_input=input()
find_pin=user_input.find("pin")
#The above line of code finds whether pin present or not


output_result=user_input[find_pin:find_pin+(len("pin"))] 
print(output_result)
