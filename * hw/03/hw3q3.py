#imports math function
import math 
#asks users for three numbers for quadratic equation
print("Please input three floating numbers.")
a = float(input("Please enter the first number."))
b = float(input("Please enter the second number."))
c = float(input("Please enter the third number."))
if ((b**2)-(4*a*c) < 0):
    print("This quadratic formula has no solutions.") 
elif (a == b == c == 0):
    print("X has an infinite number of solutions.") 
elif ((b**2)-(4*a*c) == 0):
    plusX = (-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
    print("X has one solution and it is X =", str(plusX))
else:
    plusX = (-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
    minusX = (-b-math.sqrt((b**2)-(4*a*c)))/(2*a)
    print("X has two solutions and they are", str(plusX), "and", str(minusX))


