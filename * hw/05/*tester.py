

#asks user for lowercase letter string
userString = input("Please enter a lowercase string.") 
#goes though string
currPos = 0
prevOrd = 0
increaseCount = 0
while(currPos < len(userString)):    
    flag = userString[currPos] 
    currPos += 1
    while(currPos < len(userString) and (ord(flag) >= prevOrd)):
          prevOrd = ord(flag)
          currPos+=1
          increaseCount += 1
if increaseCount + 1 == len(userString):
    print("The string", userString, "is increasing.")
else:
    print("The string", userString, "is not increasing.") 

