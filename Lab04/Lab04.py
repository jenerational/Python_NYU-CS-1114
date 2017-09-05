#Lab 4 - Jennie Walker

print("Exercise 1:")
#asks user for two numbers
print("Please enter two numbers for a coordinate,")
a = int(input("Please enter the x value."))
b = int(input("Please enter the y value."))
#determines coordinate quadrant
if (a > 0) and (b > 0):
    quad = "quadrant 1." 
if (a <0 ) and (b > 0):
    quad = "quadrant 2."
if (a < 0) and (b < 0):
    quad = "quadrant 3."
if (a > 0) and (b < 0):
    quad = "quadrant 4."
if (a == 0) or (b == 0):
    quad = "no specific quadrant." 

print("Point", str(a) + ",", str(b), "is in", str(quad)) 

print("Exercise 2:")
#handed in with paper
print("n/a")

print("Exercise 3:")
oldSOE = input("Please enter your old SoE Phone Number with hyphens.")
#determines if old number has correct area code
if (oldSOE[:7] == "718-260"):
    print("646-997" + oldSOE[7:]) 
else:
    print("This is not a valid old SoE phone Number.") 

print("Exercise 4:")
import turtle
#asks user for color, shape and size of drawing
userColor = input("Please enter a color.")
userShape = input("Please enter 'triangle' or 'square'.")
userSize = int(input("Please enter an integer."))

if (userShape == "triangle"):
    turtle.pencolor(userColor)
    turtle.forward(userSize)
    turtle.left(120)
    turtle.forward(userSize)
    turtle.left(120)
    turtle.forward(userSize)
    turtle.left(120)
elif (userShape == "square"):
    turtle.pencolor(userColor)
    turtle.forward(userSize)
    turtle.left(90)
    turtle.forward(userSize)
    turtle.left(90)
    turtle.forward(userSize)
    turtle.left(90)
    turtle.forward(userSize)
    turtle.left(90)
#in case there is no valid input
else:
    print("This is not a valid input") 

print("Exercise 5:")
#asks user for three word phrase
word1 = input("Please enter the first word of a three word phrase.")
word2 = input("Please enter the second word of a three word phrase.")
word3 = input("Please enter the third word of a three word phrase.")
print("The first letter of each word is:", word1[0], word2[0], word3[0])
wordNum = input("Which word would you like to print in all caps - 1, 2, or 3?")
if (wordNum == "1"):
    print(word1.upper())
elif (wordNum == "2"):
    print(word2.upper())
elif (wordNum == "3"):
    print(word3.upper())
else:
    print("That is not a valid input.") 
thLet = input("Please enter a three letter word to be returned in ASCII")
for ch in thLet:
    print(ord(ch))

print("Exercsie 6:")
password = input("Please enter your password.")
#determines if password has at least one uppercase character 
upperCounter = 0
for ch in password:
    if (ch.isupper() == True):
        upperCounter += 1
if (upperCounter >= 1):
    print("This is a valid password")
else:
    print("This is not a valid password.")


print("Exercise 7:")
numString = input("Please enter two integers separated by a space.") 
#finds space in string
spaceIndex = numString.find(" ")
#separates numbers
num1 = int(numString[:spaceIndex])
num2 = int(numString[spaceIndex+1:])
#adds and prints numbers 
print(str(num1), "+", str(num2), "=", str(num1 + num2))


print("Exercise 8:")
userInput = input("Please enter something.")
#checks to see if string is integer
if userInput.isdigit():
    print("You have entered a number.")
else:
    print("This is not a number.") 
