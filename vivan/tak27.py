temprature = float(input("Enter you temprature in celsius:"))
if temprature < 0:
    print("IT is freezing")
elif temprature <= 20:
    print("It is cold")
elif temprature <= 30:
    print("It is warm")
elif temprature >= 30:
    print("Hot")