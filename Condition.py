# Importing math module to use mathematical functions like square root
import math

# Taking an integer input from the user
n = int(input("Enter the number : "))

# Checking if the number is between 1 and 9
if 0 < n < 10:
    print(n**2)         # If true, print the square of the number

# Checking if the number is between 11 and 99
elif 10 < n <100:
    print(math.sqrt(n))  # If true, print the square root of the number

# If the number is not in the above ranges
else:
    print(n**3)          # Print the cube of the number