

#asks user for lowercase letter string
userStr = input("Please enter a lowercase string.") 
#goes though string
currPos = 0
flagCount = 0
while(currPos < len(userStr)-1):    
    if userStr[currPos]<userStr[currPos+1]:
        boolFlag = True
        flagCount += 1
    else:
        boolFlag = False
    currPos += 1
if (flagCount+1 == len(userStr)): 
    print("The string", userStr, "is increasing.")
else:
    print("The string", userStr, "is not increasing.") 


