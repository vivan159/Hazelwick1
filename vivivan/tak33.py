import random

score = 0


for i in range(5):
    
    secret = random.randint(0, 100)
    
    
    guess = int(input("Guess the number (0-100): "))
    
    
    if guess > secret:
        diff = guess - secret
    else:
        diff = secret - guess
        
   
    if diff == 0:
        print("Bang-on!")
        score = score + 10
    elif diff <= 5:
        print("Close!")
        score = score + 5
    elif diff <= 10:
        print("Okay.")
        score = score + 2
    else:
        print("Way off!")
        score = score + 0



print("Final score:")
print(score)