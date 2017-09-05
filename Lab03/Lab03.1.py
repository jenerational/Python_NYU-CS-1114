print("Exercise 1:") 
inputNum = int(input("Please enter a number that is equal or less than 100."))
#converts int to roman numerals 
outputNum = ""
if (inputNum >= 100):
    outputNum = outputNum+"C"
    inputNum -= 100
if (inputNum<100) and (inputNum >= 50):
    outputNum = outputNum+"L"
    inputNum -= 50
if (inputNum >= 10):
    outputNum = outputNum+"X"
    inputNum -= 10
if (inputNum >= 10):
    outputNum = outputNum+"X"
    inputNum -= 10
if (inputNum >= 10):
    outputNum = outputNum+"X"
    inputNum -= 10
if (inputNum >= 10):
    outputNum = outputNum+"X"
    inputNum -= 10
if (inputNum >= 5):
    outputNum = outputNum+"V"
    inputNum -= 5
if (inputNum >= 1):
    outputNum = outputNum+"I"
    inputNum -= 1
if (inputNum >= 1):
    outputNum = outputNum+"I"
    inputNum -= 1
if (inputNum >= 1):
    outputNum = outputNum+"I"
    inputNum -= 1
if (inputNum >= 1):
    outputNum = outputNum+"I"
    inputNum -= 1
#prints
print(outputNum)


print("Exercise 2:")
print("Enter three numbers to see if they can form a right triangle.")
a = int(input("Enter the first number."))
b = int(input("Enter the second number."))
c = int(input("Enter the third number."))

if (c > a) and (c > b):
    if (a**2 + b**2 == c**2):
        print(str(a) + ",", str(b) + ", and", str(c), "form a right triangle.")
    else:
        print(str(a) + ",", str(b) + ", and", str(c), " do not form a right triangle.")
elif (a > b) and (a > c): 
    if (c**2 + b**2 == a**2):
        print(str(a) + ",", str(b) + ", and", str(c), "form a right triangle.")
    else:
        print(str(a) + ",", str(b) + ", and", str(c), " do not form a right triangle.")
elif (b > a) and (b > c):
    if (a**2 + c**2 == b**2):
        print(str(a) + ",", str(b) + ", and", str(c), "form a right triangle.")
    else:
        print(str(a) + ",", str(b) + ", and", str(c), " do not form a right triangle.")
else:
    print(str(a) + ",", str(b) + ", and", str(c), " do not form a right triangle.")


print("Exercise 3: n/a")


print("Exercise 4:")
print("Please enter two numbers.")
a = int(input("Enter the first number."))
b = int(input("Enter the second number."))
if (a==0) and (b!=0):
    print(str(a) + "x +", str(b), "= 0 has no solution.")
elif (a==0) and (b==0):
    print(str(a) + "x +", str(b), "= 0 has infinite solutions.")
else:
    x = (-b/a)
    print("Ther is a single solution and x =", str(x))


print("Exercise 5:")
userName = input("Please enter your name.")
gradYear = int(input("Please enter your year of college graduation."))
currentYear = int(input("Please enter the year at the start of the most recent school year."))
yearDif = gradYear - currentYear
if yearDif > 4:
    print("You have not yet entered college.")
elif yearDif == 4:
    print("You are a freshman.")
elif yearDif == 3:
    print("You are a sophomore.")
elif yearDif == 2:
    print("You are a junior.")
elif yearDif == 1:
    print("You are a senior.")
elif yearDif < 1:
    print("You have graduated.") 

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


