allowed_count = 0

while allowed_count < 8:
    height = int(input("Enter rider height in cm: "))
    
    if height >= 140:
        print("Allowed to ride.")
        allowed_count = allowed_count + 1
    elif height >= 120 and input("Are you riding with an adult? (yes/no): ").lower() == "yes":
        print("Allowed to ride.")
        allowed_count = allowed_count + 1
    else:
        print("Not allowed to ride.")

print("Ride is full!")



