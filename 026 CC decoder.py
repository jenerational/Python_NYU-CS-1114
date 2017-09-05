
def CCRead(let, shift):
    uni = ord(let)
    encodedUni = uni + shift
    if (uni >= 65) and (uni <= 90): 
        while encodedUni > 90:
            encodedUni -= 26
    if (uni >= 97) and (uni <= 122):
        while encodedUni > 122:
            encodedUni -= 26 
    encodedLet = chr(encodedUni)
    return encodedLet

def main():
    inputWord = input("Please enter a phrase or word. ")
    for shiftBy in range(1, 26):
        encodedWord = ""
        for char in inputWord:
            if char.isalpha() == True:
                char = CCRead(char, shiftBy)
            encodedWord += char
        print("Shift of", str(shiftBy), ":", encodedWord)

main() 
