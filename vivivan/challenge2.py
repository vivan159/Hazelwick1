import random

print("--- 20 QUESTION MATHS CHALLENGE ---")
score = 0

for i in range(1, 21):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op = random.choice(['+', '-', '*', '/'])
    
    
    if op == '/':
        num1 = num1 * num2   
        correct = num1 // num2
    elif op == '+':
        correct = num1 + num2
    elif op == '-':
        
        if num1 < num2:
            num1, num2 = num2, num1
        correct = num1 - num2
    elif op == '*':
        correct = num1 * num2

    
    ans = input(f"Q{i}: {num1} {op} {num2} = ")
    
    
    if int(ans) == correct:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The answer was {correct}")
        print(f"Game Over! Your final score is {score} out of 20.")