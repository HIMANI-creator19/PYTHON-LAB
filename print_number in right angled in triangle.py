n=int(input("Enter the value of n: "))   # Taking input from the user and converting it into an integer
for i in range(1,n+1):                   # Outer loop runs from 1 to n and It controls the number of rows
    for j in range (1,i+1):              # Inner loop runs from 1 to i and It prints numbers from 1 up to the current row number
        print(j,end=" ")                 # Print the value of j with space, stay on same line
    print( )                             # After printing one row, move to the next line