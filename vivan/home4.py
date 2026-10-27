ticket_price = 15.00
quantity = int(input("Enter how many tickets you wan to buy"))

fast_track = input("Do you want a fast track ticket?(yes/no)").lower().strip()
if fast_track == "yes":
    ticket_price += 3.00
    subtotal = quantity * ticket_price

    if quantity >= 4:
        discount = subtotal * 0.10
        total = subtotal - discount
    else:
        total = subtotal
print(f"Your final total is: £{total:.2f}")
