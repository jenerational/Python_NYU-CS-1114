
import random

def writeRandNumbers(filename, n):
    target = open(filename, 'w')
    for i in range(n):
        target.write(str(random.randint(1, 100)) + "\n")

def main():
    writeRandNumbers("Lab11-2 xyz.txt", 5)

main()
