# Take mass and velocity input from user and convert it into float
mass = float(input("Enter mass of object in kg : "))
velocity = float(input("Enter velocity in m/s : "))

# Calculate momentum using formula
momentum = mass * velocity

# Print momentum in normal format
print("Momentum of the object : ",momentum,"kgm/s")

# Print momentum using formatted string (f-string) with fixed decimal format
print(f"{momentum:2f}","kgm/s")