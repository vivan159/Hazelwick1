# 1. Ask the user for a whole number
number = int(input("Enter a number: "))

# 2. Store the divisors we want to check in a list
divisors = [3, 5, 7]

# 3. Create an empty list to store the successful matches
divisible_by = []

# 4. ITERATION: Loop through each divisor in our list
for d in divisors:
    if number % d == 0:
        divisible_by.append(str(d)) # Add the number to our results if it fits perfectly

# 5. Output the final answer
if len(divisible_by) == 0:
    print("The number is not divisible by 3, 5, or 7.")
else:
    results = ", ".join(divisible_by)
    print("The number is divisible by: " + results)