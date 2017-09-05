
seqLen = int(input("Please enter the length of the sequence: "))
intSum = 1
for counter in range(0, seqLen):
    intSum *= int(input("Please enter a positive integer."))
print("The geometric mean is:", (intSum)**(1/seqLen))
