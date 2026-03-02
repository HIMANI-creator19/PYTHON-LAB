def Positive_Negative_Zero(n):         # Function definition to check whether a number is Positive, Negative, or Zero
 if(n>0):                              # Check if the number is greater than 0
    return "Positive"
 elif(n<0):                            # Check if the number is less than 0
    return "Negative"
 else:                                 # If the number is neither greater nor less than 0 then it must be equal to 0
    return "Zero"
                                       # Calling the function with different values
print(Positive_Negative_Zero(4))       # Positive number
print(Positive_Negative_Zero(-8))      # Negative number
print(Positive_Negative_Zero(0))       # Zero