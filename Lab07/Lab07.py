  
print("Exercise 1: ")
inputBIN = input("Please enter a string of 0s and 1s: ") 
currPos = 0
outputStr=""
print("Your string has: ") 
while(currPos < len(inputBIN)):
    numCounter = 1
    flag = inputBIN[currPos] 
    currPos += 1
    while(currPos < len(inputBIN) and flag == inputBIN[currPos]):
          numCounter += 1
          currPos+=1
    outputStr += str(numCounter) + " " + flag+"'s "
print(outputStr)


print("Exercise 2: ")
import random
int1 = random.randint(1, 100)
print("I thought of a number between 1 and 100! Guess it! ") 
guess = int(input("Try to guess what it is: "))
while (int1 != guess):
    if (int1 < guess):
        print("Wrong guess. my number is smaller than yours. ")
        guess = int(input("Try to guess what it is: "))
    else:
        print("Wrong guess. my number is bigger than yours. ")
        guess = int(input("Try to guess what it is: "))
print("You guessed the number. Yayy!!") 
