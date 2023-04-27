#solution for PSET-7
user_input= input("Enter some text:")
leetspeak_code=user_input.replace('A' , '4').
replace('B', 'I3').
replace('E', '3').replace('I', '1').replace('H', '#').replace('M', '/\/\').
replace('O', '0').replace('S', '5').replace('T', '7').replace('U', '(_)')
print(leetspeak_code)
