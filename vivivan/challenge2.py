import random

score = 0

print("--- Year 9 Math Quiz ---")
print("Answer the following 20 questions:")


for i in range(1, 21):
    
    op = random.choice(['+', '-', '*', '/'])
    
    
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    
    
    if op == '+':
        correct_answer = num1 + num2
    elif op == '-':
        correct_answer = num1 - num2
    elif op == '*':
        correct_answer = num1 * num2
    elif op == '/':
    
        num1 = num1 * num2
        correct_answer = num1 // num2 

   
    user_answer = int(input(f"Question {i}: What is {num1} {op} {num2}? "))
    
    
    if user_answer == correct_answer:
        print("Correct!")
        score = score + 1
    else:
        print(f"Wrong! The correct answer was {correct_answer}")
    print() 


print("--- Quiz Finished ---")
print(f"Your final score is {score} out of 20.")