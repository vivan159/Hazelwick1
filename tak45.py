import random


secret_number = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100. You have 10 attempts!")


for attempt in range(1, 11):
    guess = int(input(f"Attempt {attempt}/10 - Enter your guess: "))
    
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct!")
        break  


if guess == secret_number:
    print("You won!")
else:
    print(f"You lost! The correct number was {secret_number}.")