# Take a number as input from the user and convert it into integer
num = int(input("Enter the number : "))

# Check if the number is divisible by 2 or remainder is 0, the number is even
if(num % 2 == 0):
    print("Even")  # Executed when the number is even

# If the remainder is not 0, the number is odd
else:
    print("Odd")   # Executed when the number is odd