#Solution for PSET-7
user_input = input("Enter some text: ")
leetspeak_code=user_input.replace('A','4')
leetspeak_code=leetspeak_code.replace('B','I3')
leetspeak_code=leetspeak_code.replace('E','3')
leetspeak_code=leetspeak_code.replace('I','1')
leetspeak_code=leetspeak_code.replace('H','#')
leetspeak_code=leetspeak_code.replace('M','/\/\ ')
leetspeak_code=leetspeak_code.replace('O','0')
leetspeak_code=leetspeak_code.replace('S','5')
leetspeak_code=leetspeak_code.replace('T','7')
leetspeak_code=leetspeak_code.replace('U','(_)')
print(leetspeak_code)

#Another Solution for PSET-7
user_input = input("Enter some text: ")
leetspeak_code=user_input.replace('A','4').replace('B','I3').replace('E','3').replace('I','1').replace('H','#').replace('M','/\/\ ').replace('O','0').replace('S','5').replace('T','7').replace('U','(_)')
print(leetspeak_code)
