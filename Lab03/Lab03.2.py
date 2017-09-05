#Advanced Exercises for Lab 3

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


print("Exercise 7:")
monthNum = int(input("Please enter a number from 1 to 12."))
if (monthNum == 1): 
    print("You entered January, and the number of days in January is 31.")
elif (monthNum == 2):
    print("You entered February, and the number of days in February is 28.")
elif (monthNum == 3): 
    print("You entered March, and the number of days in March is 31.")
elif (monthNum == 4):
    print("You entered April and the number of days in April is 30.")
elif (monthNum == 5):
    print("You entered May and the number of days in May is 31.")
elif (monthNum == 6): 
    print("You entered June, and the number of days in June is 30.") 
elif (monthNum == 7):
    print("You entered July, and the number of days in July is 31.") 
elif (monthNum == 8):
    print("You entered August, and the number of days in August is 31.") 
elif (monthNum == 9):
    print("You entered September, and the number of days in September is 30.") 
elif (monthNum == 10):
    print("You entered October, and the number of days in October is 31.") 
elif (monthNum == 11):
    print("You entered November, and the number of days in November is 30.")
elif (monthNum == 12):
    print("You entered December, and the number of days in December is 31.") 
else:
    print("You did not enter a valid imput. Try again") 

    
print("Exercise 8:")
import turtle

input_number = input('Please enter a two digit number')
num1 = input_number[0]
num2 = input_number[1]

tp=turtle.pos()
if(num1 == '0'):
    turtle.pencolor('red')
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
elif(num1 == '1'):
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.backward(50)
    turtle.forward(100)
elif(num1 == '2'):
    turtle.pencolor('red')
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
elif(num1 == '3'):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(100)
elif(num1 == '4'):
    turtle.pencolor('red')
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.backward(100)
    turtle.forward(200)
    turtle.left(90)
elif(num1 == '5'):
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.backward(100)
elif(num1 == '6'):
    turtle.pencolor('red')
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(180)
elif(num1 == '7'):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
elif(num1 == '8'):
    turtle.pencolor('red')
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
elif(num1 == '9'):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    
turtle.penup()
turtle.setpos(tp)
turtle.forward(150)
turtle.pendown()
turtle.pencolor('black') 

if(num2 == '0'):
    turtle.pencolor('red')
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
elif(num2 == '1'):
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.backward(50)
    turtle.forward(100)
elif(num2 == '2'):
    turtle.pencolor('red')
    turtle.backward(100)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
elif(num2 == '3'):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(100)
elif(num2 == '4'):
    turtle.pencolor('red')
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.backward(100)
    turtle.forward(200)
    turtle.left(90)
elif(num2 == '5'):
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.backward(100)
elif(num2 == '6'):
    turtle.pencolor('red')
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(180)
elif(num2 == '7'):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
elif(num2 == '8'):
    turtle.pencolor('red')
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
elif(num2 == '9'):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)

