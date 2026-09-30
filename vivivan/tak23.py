print("Maths Quiz")

score = 0


print("What is 37 + 58?")
answer1 = int(input())
if answer1 == 95:
    print("Correct")
    score = score + 1
else:
    print("Wrong, it is 95")


print("What is 93 - 45?")
answer2 = int(input())
if answer2 == 48:
    print("Correct")
    score = score + 1
else:
    print("Wrong, it is 48")


print("What is 7 x 8?")
answer3 = int(input())
if answer3 == 56:
    print("Correct")
    score = score + 1
else:
    print("Wrong, it is 56")


print("What is 72 / 6?")
answer4 = int(input())
if answer4 == 12:
    print("Correct")
    score = score + 1
else:
    print("Wrong, it is 12")


print(score)
