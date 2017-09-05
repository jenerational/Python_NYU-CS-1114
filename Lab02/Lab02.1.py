
print("Exercise 1:") 
#asks user to enter an integer in kilograms
kilograms = int(input("Please enter an integer in kilograms."))
#converts kilograms to pounds 
pounds = kilograms * 2.2046
#finds the remainder of pounds when divided by 1
rem = pounds%1
#redefines pounds as an integer
pounds=pounds-rem
#converts the remainder to ounces 
ounces = rem * 16
#prints 
print(str(kilograms), "is",  str(pounds), "pounds and", str(ounces), "ounces.")

print("Exercise 2:")
#asks user to enter inches integer
inches = int(input("Please enter an integer in inches"))
#converts inches to feet
feet = inches / 12
#redefines feet as an integer
feet = feet-(feet%1)
#finds the remainder of the inches minus the feet 
rem2 = inches % 12
#prints
print(str(inches), "is", str(feet), "feet and", str(rem2), "inches.")

print("Exercsie 3:")
#inports math module
import math 
#asks user to enter radius integer
radius = int(input("Please enter an integer for the radius."))
#calculates circumfrence of circle 
circ =  2 * math.pi * radius
#calculates area of circle
area = math.pi * radius * radius
#prints
print("Your circle with radius", str(radius), "has a circumfrence of",
      str(circ), "and an area of", str(area))


print("Exercise 4:") 
#inputs turtle module
import turtle
#makes color blue
turtle.pencolor('blue')
#moves turtle forward 60 and rotates it right 120 degrees. repeats 5 times
turtle.forward(60)
turtle.right(60)
turtle.forward(60)
turtle.right(60)
turtle.forward(60)
turtle.right(60)
turtle.forward(60)
turtle.right(60)
turtle.forward(60)
turtle.right(60)
#moves turtle forward to create a spiral
turtle.forward(70)
turtle.right(60)
#makes color green
turtle.pencolor('green')
turtle.forward(60)
turtle.right(60)
turtle.forward(70)
turtle.right(60)
turtle.forward(70)
turtle.right(60)
turtle.forward(70)
turtle.right(60)
turtle.forward(70)
turtle.right(60)
#creates third spiral
turtle.forward(80)
turtle.right(60)
#makes color purple
turtle.pencolor('purple')
turtle.forward(70)
turtle.right(60)
turtle.forward(80)
turtle.right(60)
turtle.forward(80)
turtle.right(60)
turtle.forward(80)
turtle.right(60)
turtle.forward(80)2

turtle.right(60)
#creates fourth spiral
turtle.forward(90)
turtle.right(60)
#makes color pink
turtle.pencolor('pink')
turtle.forward(80)
turtle.right(60)
turtle.forward(90)
turtle.right(60)
turtle.forward(90)
turtle.right(60)
turtle.forward(90)
turtle.right(60)
turtle.forward(90)
turtle.right(60)
turtle.forward(90)
turtle.right(60)


print("Exercise 6:")
#asks user for birthday
birthDate = input("Please enter your birthday in YYYYMMDD format.")
#asks user for today's date 
todayDate = input("Please enter today's date in YYYYMMDD format.")
#separates year strings
birthYear = int(birthDate[:4])
todayYear = int(todayDate[:4])
#separates months from strings
birthMonth = int(birthDate[4:6])
todayMonth = int(todayDate[4:6])
#separates days from strings
birthDay = int(birthDate[6:])
todayDay = int(todayDate[6:])
#Calculates days 
birthDays = (birthYear * 365) + (birthMonth * 30) + (birthDay)
todayDays = (todayYear * 365) + (todayMonth * 30) + (todayDay)
#calculates difference in total days
totalDays = (todayDays - birthDays)
#calculates number of years
totalYear = totalDays//365
#calculates remainder of days
totalDays = totalDays%365
#calculates number of months
totalMonth = totalDays//30
#calculates remainder of days
totalDay = totalDays%30
#prints
print("You are", str(totalYear), "years,", str(totalMonth), "months, and",
      str(totalDay), "days.")



print("Exercise 7:") 
#asks user for first length
length1ft = int(input("Please enter the first length's number of feet."))
length1in = int(input("Please enter the first length's number of inches."))
#asks user for second length
length2ft = int(input("Please enter the second length's number of feet."))
length2in = int(input("Please enter the second length's number of inches."))
#calculates total number of inches
length1 = (length1ft * 12) + (length1in)
length2 = (length2ft * 12) + (length2in)
#calculates inches sum
totalLength = length1 + length2
#converts back into feet and inches
totalFeet = totalLength // 12
totalInches = totalLength % 12
#prints
print("Their sum is", str(totalFeet), "feet and", str(totalInches), "inches.")


