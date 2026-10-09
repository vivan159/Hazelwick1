import random

secret = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 and 100. You have 10 attempts.")

while attempts < 10:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret:
        print("You win! ")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

if guess != secret:
    print(f"You lose! The number was {secret}.")