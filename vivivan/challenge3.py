items = int(input("How many items do you want to buy? "))
total = 0


for i in range(items):
    price = float(input("Enter the price of the item: £"))
    total = total + price


print("The total price is: £" + str(total))


if total > 20:
    discount = total * 0.20
    final_total = total - discount
print("You get a 20% discount!")
print("Your final discounted price is: £" + str(final_total))