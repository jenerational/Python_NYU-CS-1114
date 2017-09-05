#asks user for character input
userChar = input("Please enter a character.")
#tests to see if upper or lowercase letter
if (userChar.islower() == True):
    print(userChar, "is a lowercase letter.")
elif (userChar.isupper() == True):
    print(userChar, "is an uppercase letter.") 
#tests to see if digit
elif (userChar.isdigit() == True):
    print(userChar, "is a digit.")
#otherwise assumes character is alphanumeric 
else:
    print(userChar, "is a non-alphanumeric character.") 
