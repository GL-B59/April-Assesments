# Solution for PSET-2
main_string=input()
sub_string=input()
a=main_string.find(sub_string)
output=main_string[a:a+(len(sub_string))]
print(output)


#Another Solution for PSET-2
main_string=input()
sub_string=input()
print(main_string[main_string.find(sub_string):main_string.find(sub_string)+(len(sub_string))])
