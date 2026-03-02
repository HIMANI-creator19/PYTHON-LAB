def is_prime(num):                      # Function to check whether a number is prime or not
    if num <= 1:                        # Prime numbers are greater than 1
        return False                    
    for i in range(2, num):             # Loop from 2 to num-1 to check divisibility
        if num % i == 0:                # If num is divisible by any number in this range, then it is not a prime number
            return False
    return True                         # If no divisors are found, the number is prime

number = int(input("Enter number: "))   # Taking input from the user

if is_prime(number):                    # Checking and printing the result
    print("Prime number")
else:
    print("Not a prime number")