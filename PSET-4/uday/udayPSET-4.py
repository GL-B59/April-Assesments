#Solution for PSET-4
#total_apple = 10
#apple_eaten = 4
#print('There are ' + total_apple - apple_eaten + ' left in the basket.' )
#In the above code bug is present I mean its a TypeError: can only concatenate str (not "int") to str
#Hence we are converting int to string and the correct code is given below:

#Error is fixed and below code will gives us output.
total_apple = 10
apple_eaten = 4
print('There are ' +str(total_apple - apple_eaten) + ' left in the basket.' )
