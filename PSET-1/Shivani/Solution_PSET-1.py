user_input = input()
find_pin = user_input.find("pin") #Pin is present or not
output_result = user_input[find_pin:find_pin+(len("pin"))] # It will show the output
print(output_result)
