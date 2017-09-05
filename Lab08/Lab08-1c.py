
#CS 1114 Lab 8-1c
#October 30, 2015

print("Exercise 1c: ")
def main():
    fibNum = int(input("Please enter a number. "))
    print (funcFib(fibNum))

def funcFib(fibNum):
    fibSum = 0
    if fibNum == 0:
        print("0")
    elif fibNum == 1:
        print("1")
    else:
        print("0")
        print("1")
        num1 = 0
        num2 = 1
        for i in range(2, fibNum+1):
            num3 = num1 + num2 
            fibSum += num3
            num1 = num2
            num2 = num3
            print(num3)
        return
main()


