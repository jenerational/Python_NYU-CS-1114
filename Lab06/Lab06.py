print("Exercise 1:")
n = int(input("Please enter a number. "))
z = 1
for i in range (1, n+1):
    z = z*i
print(z)

print("Exercise 2:")
userString = input("Please enter a string. ")
outString = ""
for ch in userString:
    if ch.islower() == True:
        ch = ch.upper()
    else:
        ch = ch.lower()
    outString += ch
print(outString)

print("Exercise 3:")
print("Please enter a name in two forms. ")
name1 = input("Enter Last Name, First Name. ")
name2 = input("Enter First Name Last Name. ")
commaIndex = name1.find(",")
spaceIndex = name2.find(" ")
firstName1 = name1[commaIndex+2:]
lastName1 = name1[:commaIndex]
firstName2 = name2[:spaceIndex]
lastName2 = name2[spaceIndex+1:]
if (firstName1 == firstName2) and (lastName1 == lastName2):
    print("These two names are the same!")
else:
    print("These two names are different.") 

