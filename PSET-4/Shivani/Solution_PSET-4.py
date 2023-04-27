total_apple = 10
apple_eaten = 4
print('There are ' + total_apple - apple_eaten + ' left in the basket.' )
# Yes there is a bug in the above code (TypeError: can only concatenate str (not "int") to str)

# First we have to convert integer to string then print the statement.
# To generate code again :
total_apple = 10
apple_eaten = 4
print('There are ' + str(total_apple - apple_eaten) + ' left in the basket.' )

# Answer: There are 6 left in the basket.
