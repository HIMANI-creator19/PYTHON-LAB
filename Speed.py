# Calculate the Speed of an object
Dist = int(input("Enter the Distance in meters : "))
Time = int(input("Enter the Time in seconds : "))

Speed = Dist/Time

print("The Speed : ",Speed,"m/s")

#Converting the speed from meter per sec to km per hr
Speed_kmhr = Speed * 3.6

print("The Speed : ",Speed_kmhr,"km/hr")