
total = 0

while True:
    
    number = int(input("Enter a number: "))
    
    
    total += number
    
    
    if total >= 100:
        break


print(f"Final total: {total}")