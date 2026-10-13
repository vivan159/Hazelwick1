items = int(input("Enter how many items you want to buy"))
total = 0
for i in range(items):
    price = float(input("Price of items"))
    total += price
    if total > 20:
        total * 0.20