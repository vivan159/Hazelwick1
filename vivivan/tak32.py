# 1. Ask the user for a whole number
number = int(input("Enter a number: "))


divisors = [3, 5, 7]


divisible_by = []


for d in divisors:
    if number % d == 0:
        divisible_by.append(str(d)) 


if len(divisible_by) == 0:
    print("The number is not divisible by 3, 5, or 7.")
else:
    results = ", ".join(divisible_by)
    print("The number is divisible by: " + results)