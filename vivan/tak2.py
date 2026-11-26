total = 0
highest = -100
frosty_days = 0

days = int(input("How many days? "))

for day in range(days):
    temperature = float(input("Enter temperature for day " + str(day + 1) + ": "))

    total = total + temperature

    if temperature > highest:
        highest = temperature

    if temperature < 0:
        frosty_days = frosty_days + 1

average = total / days

print("Average temperature:", average)
print("Highest temperature:", highest)
print("Number of frosty days:", frosty_days)