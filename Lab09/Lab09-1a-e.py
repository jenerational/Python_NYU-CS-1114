
def main():
    print("a. Count:")
    lst = [0, 32, 'a', '0', '4', 15, 'q', '0']
    item = '0'
    print(count(lst, item))
    print("b. Powers of 2:")
    n = int(input("Please enter an integer."))
    print(powersOfTwo(n))
    print("c. Find Min Index:")
    lst =  [56, 24, 58, 10, 33, 95]
    print(findMinIndex(lst))
    print("d. Circular Shift List 1:") 
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 3
    print(circularShiftList1(lst, k))
    print("e. Circular Shift List 2:")
    print(circularShiftList2(lst, k))

def count(lst, item):
    lstCount = 0
    for x in lst:
        if item == x:
            lstCount += 1
    return lstCount

def powersOfTwo(n):
    L = []
    for x in range(1, n+1):
        L.append(2**x)
    return L

def findMinIndex(lst):
    min = lst[0]
    for x in lst:
        if x < min:
            min = x
    return lst.index(min)
    
def circularShiftList1(lst, k):
    L = []
    for x in lst[len(lst)-k:]:
        L.append(x)
    for x in lst[:len(lst)-k]:
        L.append(x)
    return L

def circularShiftList2(lst, k):
    L = lst[len(lst)-k:] + lst[:len(lst)-k]
    return L

main()
