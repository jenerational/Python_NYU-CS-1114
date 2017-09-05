
#asks user to input a mathematical expression
userOp = input("Please enter a mathematical expression. ")
for ch in userOp:
    #for multipling operand
    if (ch == "x") or (ch == "*"):
        #finds the operand
        opIndex = userOp.find(ch)
        #locates the two numbers
        num1 = int(userOp[:opIndex])
        num2 = int(userOp[opIndex+1:])
        #multiples the two numbers
        print(str(num1*num2))
    elif (ch == "/"):
        opIndex = userOp.find(ch)
        num1 = int(userOp[:opIndex])
        num2 = int(userOp[opIndex+1:])
        #divides the two numbers
        print(str(num1/num2)) 
    elif (ch == "+"):
        opIndex = userOp.find(ch)
        num1 = int(userOp[:opIndex])
        num2 = int(userOp[opIndex+1:])
        #adds the two numbers
        print(str(num1+num2))
    elif (ch == "-"):
        opIndex = userOp.find(ch)
        num1 = int(userOp[:opIndex])
        num2 = int(userOp[opIndex+1:])
        #subtracts the two numbers 
        print(str(num1-num2)) 
