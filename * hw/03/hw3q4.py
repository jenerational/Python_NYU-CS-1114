
#imports math
import math
#ask user for three triangle sides 
print("Please input the sides of three triangles.")
a = float(input("Please enter the first side."))
b = float(input("Please enter the second side."))
c = float(input("Please enter the third side.")) 

#calculates if sides are equal
if (a == b):
    if (b == c):
        print("Your triangle is an equilateral triangle.")
    else:
        if a == a * (math.sqrt(2)):
            print("Your isoceles triangle is a right triangle.") 
        else:
            print("Your isoceles triangle is not a right triangle.")
elif (a == c):
    if (b == c):
        print("Your triangle is an equilateral triangle.")
    else:
        if a == a * (math.sqrt(2)):
            print("Your isoceles triangle is a right triangle.") 
        else:
            print("Your isoceles triangle is not a right triangle.") 
elif (b == c):
    if (a == c):
        print("Your triangle is an equilateral triangle.")
    else:
        if b == b * (math.sqrt(2)):
            print("Your isoceles triangle is a right triangle.") 
        else:
            print("Your isoceles triangle is not a right triangle.")
else:
    print("Your triangle is not an isosceles or an equilateral triangle.")



