side1 = float(input("Enter your side"))
side2 = float(input("Enter your side"))
side3 = float(input("Enter your side"))
if side1 == side2 and side2 == side3 and side3 == side1:
    print("Your triangle is equaletral")
elif side1 == side2 and side2 == side3:
    print("Your triangle is issocles")
else:
    print("Your triangle is scalene")