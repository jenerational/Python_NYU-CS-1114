
import random
import turtle
import colorsys


def turtleBox():
    print("Please enter two different numbers between 50 and 500.")
    a = int(input("Please enter the first number."))
    b = int (input("Please enter the second number."))
    turtle.pencolor(random.random(),random.random(), random.random())
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    
def turtleCircle():
    turtle.color(random.random(),random.random(), random.random())
    #turtle.color("black", color)
    turtle.begin_fill()
    turtle.circle(80)
    turtle.end_fill()

def main():
    #color = 40e0d0
    turtleBox()
    turtleCircle()

main()
