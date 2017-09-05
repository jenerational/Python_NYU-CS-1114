
#asks user to input a number 
n = int(input("Please enter an integer.")) 
#creates second triangle 
z = n-1
newStr = ""
if (n < 10): 
    for i in range(0, n):
        newStr += str(i+1)
        print((" "*z)+newStr)
        z -= 1 
else:
    for i in range(0, 9):
        newStr += str(i+1)
        print((" "*(z+n-7))+newStr)
        z -= 1
    z += 1
    for i in range(9, n):
        newStr += str(i+1)
        print((" "*z*2)+newStr)
        z -= 1
