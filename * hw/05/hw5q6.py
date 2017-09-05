userStr = input("Please enter a line of text. ")
userCh = input("Please enter the character you want to remove. ")
newStr = ""
for ch in userStr:
    if ch != userCh:
        newStr += ch
print(newStr)
