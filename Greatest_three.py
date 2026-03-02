# Take three numbers as input from the user in a single line
# split() separates the input values and map(int, ...) converts them into integers
num1, num2, num3 = map(int, input("Enter three numbers: ").split())

# Check if num1 is greater than both num2 and num3
if num1 > num2 and num1 > num3:
    print("Greatest number : ",num1)

# Check if num2 is greater than both num1 and num3
elif num2 > num1 and num2 >num3:
    print("Greatest number : ",num2) 

# Check if num3 is greater than both num1 and num2
elif num3 > num1 and num3 >num2:
    print("Greatest number : ",num3)

# If none of the above conditions are true,
# it means either all numbers are equal or two numbers are equal and greatest
else:
    print("All are equal")
