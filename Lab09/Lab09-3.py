
def main():
    lst = []
    userL = input("Please enter a list item.")
    while (userL != "Done"):
        lst.append(int(userL))
        userL = input("Please enter a list item.")
    print(squareSum(lst))

def squareSum(lst):
    sum = 0 
    for x in lst:
        sum += x**2
    return sum

main()
