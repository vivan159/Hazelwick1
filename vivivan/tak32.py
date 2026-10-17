# 1. Ask the user for a number
num = int(input("Enter a number to check: "))

# 2. Set up an empty piece of text to hold our answers
results = ""

# 3. Check each number one by one
if num % 3 == 0:
    results = results + "3 "

if num % 5 == 0:
    results = results + "5 "

if num % 7 == 0:
    results = results + "7 "

# 4. Print the final answer based on what we found
if results == "":
    print("Your number is not divisible by 3, 5, or 7.")
else:
    print("Your number is divisible by: " + results)