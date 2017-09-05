
#caesar cipher

#Please enter a positive integer: 397
#what shift should we apply? 4
#The encoded number is: 731

inputNum = input("Please enter a positive integer.")
shiftBy = int(input("What shift should we apply?"))
encodedNum = ""
for digChar in inputNum:
    dig = int(digChar) 
    #%10 so we only get the ones digit in case the number runs into the 10s
    encodedDig = (dig + shiftBy) % 10
    encodedNum = encodedNum + str(encodedDig)
print("The encoded number is:", encodedNum)


# ~or~
#message: "example"
#shift by: 2
#encoded message: gzcorng
#when using unicode: 

inputWord = input("Please enter a word.")
shiftBy = int(input("What shift should we apply?"))
encodedWord = ""
for letter in inputWord:
    uni = ord(letter)
    encodedUni = uni + shiftBy
    while encodedUni > 122:
        encodededUni -= 26 
    encodedLet = chr(encodedUni)
    encodedWord = encodedWord + encodedLet
print("The encoded word is:", encodedWord) 


