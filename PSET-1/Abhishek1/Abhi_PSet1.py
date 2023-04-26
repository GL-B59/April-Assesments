user_input=input()
find_pin=user_input.find("pin") 
output_result=user_input[find_pin:find_pin+(len("pin"))]
print(output_result)
