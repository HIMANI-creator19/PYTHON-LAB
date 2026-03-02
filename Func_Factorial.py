# Function to calculate factorial using for loop
def factorial(n):
    if n < 0:                                                    # Check if number is negative
        return "Factorial not defined for negative numbers"
    
    fact = 1                                                     # Initialize result variable

    for i in range(1, n + 1):                                    # Loop from 1 to n
        fact = fact * i                                          # Multiply result with current number
    
    return fact                                                  # Return final factorial value

num = int(input("Enter a number: "))                             # Take input from user
print("Factorial =", factorial(num))                             # Print factorial

# Function to calculate factorial using recursion

def factorial(n):
    if n < 0:                                                     # Check if number is negative
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:                                        # Base condition (stopping condition)
        return 1
    else:                                                         # Recursive call
        return n * factorial(n - 1)


num = int(input("Enter a number: "))                              # Take input from user
print("Factorial =", factorial(num))                              # Print factorial


