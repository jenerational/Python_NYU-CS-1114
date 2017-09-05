print("Exercise 6:") 
import turtle
import math 
print("Please enter two different numbers between 50 and 500.")
a = int(input("Please enter the first number."))
b = int (input("Please enter the second number."))
if (a==b):
    print("You entered the same number twice. Please try again.")
elif ((a < 50) or (a>500) or (b < 50) or (b > 500)):
    print("You entered a number not inside the range. Please try again.")
else:
    #calculates degrees to turn
    alpha = math.degrees(math.atan(a/b))
    beta = math.degrees(math.atan(b/a))
    #caluclates hypotenuse
    hyp = math.sqrt(a**2 + b**2)
    #changes pen color
    turtle.pencolor('pink')
    #moves turtle 
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.backward(b/2)
    #changes pen color
    turtle.pencolor('blue')
    #turns turtle
    turtle.left(alpha)
    #moves turtle
    turtle.forward(hyp/2)
    #turns turtle
    turtle.left(beta*2) 
    #moves turtle
    turtle.forward(hyp/2)
    #turns turtle
    turtle.left(alpha*2)
    #moves turtle
    turtle.forward(hyp/2)
    #turns turtle
    turtle.left(beta*2)
    #moves turtle
    turtle.forward(hyp/2)    
    



