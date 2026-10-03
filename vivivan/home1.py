correct_username = "student9"
correct_password = "Password123"


username_input = input("Enter your username: ")
password_input = input("Enter your password: ")


if username_input == correct_username and password_input == correct_password:
    print("Login successful! Welcome.")
else:
    print("Access denied. Incorrect username or password.")