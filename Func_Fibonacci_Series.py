# Recursive function to return Fibonacci number
def fibonacci(n):
    
    # Base condition
    if n <= 1:
        return n
    
    # Recursive call
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Take input
num = int(input("Enter number of terms: "))

print("Fibonacci series:")
for i in range(num):
    print(fibonacci(i), end=" ")
