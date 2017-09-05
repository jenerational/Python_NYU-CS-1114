#prompts user for char, w and h to print box of char
userChar = input("Please enter a character.")
userW = int(input("Enter a width."))
userH = int(input("Enter a height.")) 
for line in range(0, userH):
    print(userChar * userW) 

