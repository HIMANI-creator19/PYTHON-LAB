i=1;                                         # Initialize variable i with value 1
while i<=3:                                  # While loop will run as long as i is less than or equal to 3
    print(i)                                 # Print the current value of i
    i=i+1;                                   # Increase the value of i by 1 in each iteration

#for for loop

for i in range(1,5):                         # For loop runs from 1 to 4 (5 is excluded in range)
    print(i,end=' ')                         # Print value of i in the same line separated by space
else:                                        # The else block executes after the for loop
    print("for loop completely exhausted")   # when the loop finishes normally (not stopped by break)