input_main_str = input("Enter a string: ")
input_sub_str = input("Enter a substring to search: ")
print(f"Substring '{input_sub_str}' found in the input string." if input_main_str.find(input_sub_str) != -1 else f"Substring '{input_sub_str}' not found in the input string.")

#First, it prompts the user to enter a string by calling the input() function and storing the result in the variable input_str.
#Then, it prompts the user to enter a substring to search for by calling input() again and storing the result in the variable sub_str.
#The expression inside the print() function uses a conditional statement to check whether sub_str is found in input_str using the find() method. If sub_str is found (i.e., find() returns a non-negative index), it prints a message indicating that the substring was found using an f-string. Otherwise, it prints a message indicating that the substring was not found.

