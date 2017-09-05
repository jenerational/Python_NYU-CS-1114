
intSum = input("Please enter a positive integer. ") 
total = int(intSum)
seqLen = 1
while (intSum != "Done"):
    intSum = input("Please enter a positive integer. ")
    if (intSum != "Done"):
        total *= int(intSum)
        seqLen += 1 
print("The geometric mean is:", (total)**(1/seqLen))
