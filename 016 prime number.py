
def main():
    n = int(input("Please enter a number to see if it's prime. "))
    print(primeCheck(n))

def primeCheck(n):
    for x in range(2, n):
        nDiv = n/x
        if nDiv % 1 == 0:
            return "Your number is not prime."
    return "Your number is prime."

main()

