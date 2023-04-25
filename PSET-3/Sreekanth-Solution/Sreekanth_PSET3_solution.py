<<<<<<< HEAD
import re

name = input("Enter a name: ")

# Define a regular expression pattern to match the first name and last name
pattern = re.compile(r'^(\S+)\s(\S+)$')

# Use the pattern to match the first name and last name in the name string
match = pattern.match(name)

# If there is a match, assign the first name and last name to variables without whitespace
if match:
    first_name = match.group(1)
    last_name = match.group(2)
    # Print the first name and last name
    print("First Name:", first_name)
    print("Last Name:", last_name)
else:
    print("Invalid name format")
=======
import re

name = input("Enter a name: ")

# Define a regular expression pattern to match the first name and last name
pattern = re.compile(r'^(\S+)\s(\S+)$')

# Use the pattern to match the first name and last name in the name string
match = pattern.match(name)

# If there is a match, assign the first name and last name to variables without whitespace
if match:
    first_name = match.group(1)
    last_name = match.group(2)
    # Print the first name and last name
    print("First Name:", first_name)
    print("Last Name:", last_name)
else:
    print("Invalid name format")
>>>>>>> a529a38a1254c14bfd2c085543dc42c6765638d1
