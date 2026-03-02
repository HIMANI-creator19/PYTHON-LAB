n=int(input("Enter the value of n : "))  # Taking input from the user and converting it into an integer
for i in range (1,n+1):                  # Loop runs from 1 to n (n+1 because range excludes the last number)
    print('*'*i)                         # It prints a right-angle triangle pattern