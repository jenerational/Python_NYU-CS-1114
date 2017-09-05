
#CS 1114 Lab 8-1a
#October 30, 2015

print("Exercise la: ")
fibNum = int(input("Please enter a number. "))
fibSum = 0
if fibNum == 0:
    print("0")
elif fibNum == 1:
    print("1")
else:
    num1 = 0
    num2 = 1
    for i in range(2, fibNum+1):
        num3 = num1 + num2 
        fibSum += num3
        num1 = num2
        num2 = num3
    print(num3)
