str = input()
N = len(str)
     
str1 =""
     
for i in range(N):
    if (str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u'):
            c = (str[i]).upper()
            str1 += c
    else:
            str1 += str[i]
 
print(str1)