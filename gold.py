import random

number = int(input("Enter a number between 2 and 12: "))


if number >= 2 and number <= 12:

    
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("Dice 1:", dice1)
    print("Dice 2:", dice2)
    print("Your score is:", dice1 + dice2)

    
    print("Possible combinations:")

    for dice1 in range(1, 7):
        for dice2 in range(1, 7):

            if dice1 + dice2 == number:
                print(dice1, "+", dice2, "=", number)

else:
    print("Invalid number! Enter between 2 and 12.")