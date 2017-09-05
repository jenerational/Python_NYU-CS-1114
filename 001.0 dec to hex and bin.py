# Jennifer Walker
# CS 1114 & CS 1122
# Created 9/11/2015
# Edited 2/16/2016
# Converts numbers from dec to hex and bin 

def numHex(num):
    numH = hex(num)
    #prints hex num without the "0x" 
    print("Your number in hexidecimal is: " + numH[2:])

def numBin(num):
    numB = bin(num)
    #cuts off the 0b that marks the number as binary
    print(numB)
    numB = numB[2:]
    #prints number with full 8 characters including first 0s
    while len(numB) < 8:
        numB = "0" + numB
    #prints bin num 
    print("Your number in binary is: " + numB)


def main():
    #user enters number in Base 10
    userNum = int(input("Enter a number in deicmal. "))
    #converts to hexidecimal
    numHex(userNum)
    #converts to binary
    numBin(userNum)

main()
