def cal(total_courses,marks):                                      # Function to calculate result classification

    if any (mark<40 for mark in marks):                            # Check if any subject mark is less than 40 and If yes, student is Fail
        return "Fail"
    total_marks=sum(marks)                                         # Calculate total marks obtained
    agreegated_percentage=(total_marks/(total_courses*100))*100    # Calculate aggregated percentage
    print(f"Agregated Percentage:{agreegated_percentage:.2f}")     # Print the calculated percentage up to 2 decimal places
    if agreegated_percentage>=75:                                  # Decide class based on percentage
        return "Distinction"
    elif agreegated_percentage>=60:
        return "First Class"
    elif agreegated_percentage>=50:
        return "Second Class"
    else: 
        return "Third Class"
    
n=int(input("Enter the number of courses: "))                      # Taking number of courses as input
marks=list(map(int,input().split()))                               # Taking marks input in one line separated by space
print(cal(n,marks))                                                # Calling the function and printing the result