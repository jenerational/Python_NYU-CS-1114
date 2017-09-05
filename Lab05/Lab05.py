
#Jennie Walker, Lab 5
print("Exercise 1a:") 
n = int(input("Please enter an integer.")) 
l = n+1
for i in range(1, n*2, 2):
    print(" "*l+"*"*i)
    l -= 1

print("Exercise 1b:")
n = int(input("Please enter an integer.")) 
for i in range(1, n+1):
    print(("#"*(i-1))+"%"+("$"*(n-i)))

print("Exercise 2:")
n = int(input("Please enter an integer.")) 
for i in range(1, n+1):
    print(str(i**3))

print("Exercise 3a:")
userStr = input("Please enter a string.").lower()
userChar = input("Please enter a letter.").lower()
charCounter = 0
for ch in userStr:
    if ch == userChar:
        charCounter += 1
print("Letter", userChar, "appears", str(charCounter), "times in the string.")

print("Exercise 3b:") 
userStr = input("Please enter a string.").lower()
userChar = input("Please enter a letter.").lower()
strLen = len(userStr)
n = 0
charCounter = 0
while n < strLen:
    if userStr[n] == userChar:
        charCounter += 1
    n +=1
print("Letter", userChar, "appears", str(charCounter), "times in the string.")


print("Exercise 4a:")
n = input("Please enter an integer.") 
evenCounter = 0
oddCounter = 0
for ch in n:
    if (ch == "0") or (ch == "2") or (ch == "4") or (ch == "6") or (ch == "8"):
        evenCounter += 1
    else:
        oddCounter += 1
print("There are", str(evenCounter), "even digits and", str(oddCounter),
      "odd digits in your number.")

print("Exercise 4b:")
n = int(input("Please enter an integer.")) 
evenCounter = 0
oddCounter = 0
while n > 1:
    if n % 2 == 0:
        evenCounter += 1
    else:
        oddCounter +=1
    n = n // 10
print("There are", str(evenCounter), "even digits and", str(oddCounter),
      "odd digits in your number.")

print("Exercise 5:")
import turtle
n = int(input("Please enter an integer.")) 
for i in range (1, n+1):
    turtle.forward(100)
    turtle.left(360/n)

print("Exercise 6:") 
n = int(input("Please enter an integer.")) 
for i in range(1, n+1):
    if i % i**(1/3) == 0:
        print(i)
