# Import datetime module to get current date and year
from datetime import datetime  
# Take date of birth input from user in format dd-mm-yyyy
# split('-') breaks the input into [dd, mm, yyyy]
# [-1] takes the last part i.e., year                                        
birth_date = int (input("Enter your date of birth : ").split('-')[-1]) #
# Function to calculate age
def age(birthdate):
    current_year = datetime.now().year  # Get current year from system
    return current_year - birth_date    # Age = current year - birth year
# Function to convert salary from INR to USD
def sal(salary):
    dollar = 0.012           # Conversion rate (1 INR = 0.012 USD)
    return dollar * ind_rup  # Convert INR to USD
# Take salary input from user in Indian Rupees
ind_rup = float(input("Enter your salary in Indian Rupees : "))

# Call age function and print result
print(f"Your age : {age(birth_date)}")

# Call salary conversion function and print result
print(f"Your salary in USD : {sal(ind_rup)}")