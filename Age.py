# Take age as input from the user and convert it into integer
n = int(input("Enter the Age : "))

# Check if age is 5 or below
if n <= 5:
    print("Toddler")   # Age group: 0–5 years

# If age is greater than 5 but 12 or below
elif n<=12:
    print("Child")     # Age group: 6–12 years

# If age is greater than 12 but 18 or below
elif n<=18:
    print("Teenage")   # Age group: 13–18 years

# If age is above 18
else:
    print("Adult")     # Age group: 19 years and above