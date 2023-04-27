# Solution for PSET-2
print("Enter any string:")
main_string=input()
print("Enter sub string:")
sub_string=input()
a=main_string.find(sub_string)
output=main_string[a:a+(len(sub_string))]
print(f"substring  is {output} from string {main_string}")


#Another Solution for PSET-2 in one step
main_string=input()
sub_string=input()
print(main_string[main_string.find(sub_string):main_string.find(sub_string)+(len(sub_string))])