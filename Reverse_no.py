# Take a number as input from the user and convert it into integer
num = int (input("Enter the number : "))

# Convert the number into string so that we can reverse it using slicing
str_num = str(num)

# Reverse the string using slicing method [start:stop:step]
# Here step = -1 means it will read the string from end to start
print("Reversed number : ",str_num[::-1])