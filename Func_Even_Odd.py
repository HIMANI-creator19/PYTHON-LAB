def EvenOdd(n):              # Function definition to check whether a number is Even or Odd
    if(n%2==0):              # Check if the number is divisible by 2
        return "Even"        # If remainder is 0, the number is Even
    else:
        return "Odd"         # If remainder is not 0, the number is Odd
print(EvenOdd(16))           # Calling the function with value 16 and printing the result
print(EvenOdd(7))            # Calling the function with value 7 and printing the result