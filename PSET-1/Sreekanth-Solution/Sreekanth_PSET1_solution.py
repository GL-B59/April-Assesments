#Here, we need to join all the words into a single string using join(), and then check if the substring 'pin' is present in the resulting string using the in operator.
#If it is, we set result to 'pin', otherwise we set it to None. Finally, we print the value of result.
print("We found substring 'pin' found in the input string." if "pin" in input("Enter a string: ") else f"Substring 'pin' not found in the input string try again.")


