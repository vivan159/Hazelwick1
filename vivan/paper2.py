list = ["milk","bread","baked","beans","battleship"]
num=int(input("Enter a number between 0 and 5"))
if num <= 0 and num >=5:
    print("ok")
    if num == 1:
        print("milk")
elif num == 2:
    print("Bread")
elif num == 3:
    print("baked beans")
elif num == 4:
    print("battleship")