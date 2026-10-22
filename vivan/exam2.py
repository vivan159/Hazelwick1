hours = -1

while hours != 0:
    hours = int(input("Enter the number of hours parked (or 0 to quit): "))
    
    if hours > 0:
        is_electric = input("Is the car electric? (yes/no): ").lower()
        
        if is_electric == "yes":
            total_price = hours * 2
        else:
            total_price = hours * 4
            
        print("Total price: £" + str(total_price))