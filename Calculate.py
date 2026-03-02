# Take two numbers as input from the user in one line
# input().split() separates the values by space
# map(float, ...) converts both inputs into float (decimal numbers)
num1, num2 = map(float, input("Enter two numbers: ").split())

# Print the addition of the two numbers
print("Addition : ",num1 + num2)

# Print the subtraction of the two numbers
print("Subtraction : ",num1 - num2)

# Print the remainder when num1 is divided by num2 (modulus operation)
print("Reminder : ",num1 % num2)

# Print the multiplication of the two numbers
print("Multiplication : ",num1 * num2)

# Print the multiplication of the two numbers
print("Division : ",num1 / num2)