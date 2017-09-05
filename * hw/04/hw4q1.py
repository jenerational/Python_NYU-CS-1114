#asks user for odd lengthed input
userStr = input("Please enter a string with an odd length.") 
#caluclates length of string
strLen = int(len(userStr))
#creates variable for middle char of string 
midStrLen = int((strLen-1)/2)
#prints middle character and first/second halves of the string 
print("The middle character is", userStr[midStrLen])
print("The first half of the string is", userStr[:midStrLen])
print("The second half of the string is", userStr[midStrLen+1:])
