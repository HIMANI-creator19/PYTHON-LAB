from datetime import datetime                     # Importing the datetime class from the datetime module

birth_year=int(input("Enter the birth year: "))   # Taking birth year as input from the user and Converting the input (string) into integer

current_year=datetime.now().year                  # Getting the current year from the system date
age = current_year - birth_year                   # Calculating age by subtracting birth year from current year

print("Your Current Age : ",age)                  # Printing the calculated age