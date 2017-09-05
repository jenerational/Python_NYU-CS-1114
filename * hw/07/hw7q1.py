#  Jennie Walker HW 7.1
# November 2 2015 

def main():
    encodedWord = "" 
    inputWord = input("Please enter a word.")
    shiftBy = int(input("What shift should we apply?"))
    for letter in inputWord:
        if letter.islower() == True:
            encodedWord += lowerShift(inputWord, shiftBy, letter)
        elif letter.isupper() == True:
            encodedWord += upperShift(inputWord, shiftBy, letter)
        else:
            encodedWord += letter
    print(encodedWord)

def lowerShift(inputWord, shiftBy, letter):
    uni = ord(letter)
    encodedUni = uni + shiftBy
    while encodedUni > 122:
        encodedUni -= 26 
    return chr(encodedUni)

def upperShift(inputWord, shiftBy, letter): 
    uni = ord(letter)
    encodedUni = uni + shiftBy
    while encodedUni > 90:
        encodedUni -= 26 
    return chr(encodedUni)


main()






