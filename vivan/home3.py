secret_password = "Python9"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = input("Enter the secret passcode: ")
    attempts += 1 

    if guess == secret_password:
        print("Acess granted!!!")
    else:
        print("acess denied")
