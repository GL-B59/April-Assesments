#Write a script such that it replaces only the first occurence of a word.
#Taking first main string and storing to variable called string
string = input("Enter a sting: ")
#Taking first sub string that need to be replaced and storing to variable called old_string
old_word = input("Word to replace from string: ")
#Taking sub string that need to be used for replacing and storing to variable called new_string
new_word = input("Replacment to replace: ")
#checking the fist occurance and replacing the old_string with new_string
string = string.replace(old_word, new_word, 1)
print(string)
#Here, we taking the string input and taking the replacement word and the old word as input. and replacing the 1st offurance of the word with the word we given as as input. also pringting the same.
