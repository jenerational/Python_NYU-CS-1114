#Jennie Walker HW 5, Q2
#asks user to input a number 
n = int(input("Please enter an integer.")) 
#creates first triangle
l = 0
for i in range(0, n*2, 2):
    print(" "*l+"*"*((n*2)-(i+1)))
    l += 1 
#creates second triangle 
i = n+1
z = n-1
for i in range(1, n*2, 2):
    print(" "*z+"*"*(i))
    z -= 1 
