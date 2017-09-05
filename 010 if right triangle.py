print("Enter three numbers to see if they can form a right triangle.")
a = int(input("Enter the first number."))
b = int(input("Enter the second number."))
c = int(input("Enter the third number."))

if (a**2 + b**2 == c**2):
        print(str(a) + ",", str(b) + ", and", str(c), "form a right triangle.")
elif (c**2 + b**2 == a**2):
        print(str(a) + ",", str(b) + ", and", str(c), "form a right triangle.")
elif (a**2 + c**2 == b**2):
        print(str(a) + ",", str(b) + ", and", str(c), "form a right triangle.")
else:
    print(str(a) + ",", str(b) + ", and", str(c), " do not form a right triangle.")
