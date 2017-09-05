
#imports math function 
import math
#asks user to enter two lengths for rt triangle legs 
print("Please enter the lengths of the two legs in a right triangle.")
leg1 = float(input("Length of the first leg."))
leg2 = float(input("Length of the second leg.")) 
#calculates hypotenuse squared
hypSq = (leg1**2) + (leg2**2)  
#sqrt previous answer --> gets length of hypotenuse
hyp = math.sqrt(hypSq)
#prints
print(hyp)


import turtle
#asks user to enter two lengths for rt triangle legs 
print("Please enter the lengths of the two legs in a right triangle.")
leg1 = float(input("Length of the first leg."))
leg2 = float(input("Length of the second leg."))
#calculates hypotenuse
hyp = math.sqrt((leg1**2) + (leg2**2))  
#calculates alpha
alpha = math.degrees(math.atan(leg1/leg2))
#moves turtle in direction and rotates it, repeatedly 
turtle.forward(leg1)
turtle.left(90)
turtle.forward(leg2)
turtle.left(180-alpha)
turtle.forward(hyp)
turtle.left(180-alpha) 
