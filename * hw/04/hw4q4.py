
#asks user to input a word and converts to all lowercase
userWord = input("Please enter a word.").lower()
vowelCounter = 0
for ch in userWord:
    if (ch == "a") or (ch == "e") or (ch == "i") or (ch == "o") or (ch =="u"):
        vowelCounter += 1
print(userWord, "has", str(vowelCounter), "vowels and",
      str(len(userWord) - vowelCounter), "consonants.")
