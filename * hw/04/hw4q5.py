
#asks user to input a password
password = input("Please enter your password.")
#determines if password has at least one uppercase character 
lowerCounter = 0
upperCounter = 0
digitCounter = 0
nonaCounter = 0
if len(password) >= 8:
    for ch in password:
        if (ch.islower() == True):
            lowerCounter += 1
        elif (ch.isupper() == True):
            upperCounter += 1
        elif (ch.isdigit() == True):
            digitCounter += 1
        else:
            nonaCounter += 1
    if (upperCounter >= 2) and (digitCounter >= 2) and (nonaCounter >=1):
        print("This is a valid password")
    else:
        print("This is not a valid password.") 
else:
    print("This is not a valid password.") 
