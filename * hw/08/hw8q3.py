#modified Q8-3

def main():
    #asks user for input
    n = int(input("What number of spaces would you like in the margin? "))
    m = int(input("How many times would you like it to run? "))
    symbol = input("Please enter a symbol. ")
    #runs two tree functions 
    printShiftTri(n, m, symbol)
    printPineTree(n, symbol)

def printShiftTri(n, m, symbol): 
    #sets starter number of spaces
    l = n + m - 1
    for z in range(1, m*2, 2):
        #prints within function
        print((" "*l)+(symbol*z))
        l -= 1
    return

def printPineTree(n, symbol):
    #sets first for loop for # of trees
    for i in range(1, n+1):
        l = i + n-i
        #sets second for loop for number of lines per tree 
        for z in range(1, i*2+3, 2): 
            #prints within function
            print(" "*l + symbol*z)
            l -= 1
    return 

main()
