main_string = input()
sub_string = input()
a = main_string.find(sub_string)
output = main_string[a:a+(len(sub_string))]
print(output)
