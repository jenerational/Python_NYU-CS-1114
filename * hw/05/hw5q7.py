
#asks user for number
n = input("Please enter a number.") 

for i in range(0, int(n)):
    evenCount = 0
    oddCount = 0 
    for ch in str(i):
        #checks if ch is even 
        if (ch=="0") or (ch=="2") or (ch=="4") or (ch == "6") or (ch == "8"):
            evenCount += 1
        else:
            oddCount += 1
    #checks if even count is larger than odd count 
    if evenCount > oddCount:
        print(i)

