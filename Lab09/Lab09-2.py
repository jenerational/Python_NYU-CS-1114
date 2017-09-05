
def main():
    list1 = [2, 'S', 3.13, 3.13, "Python"]
    list2 = ["Pythy", 2, 12, "hello", 3.13]
    print(getCommonEle(list1, list2))

def getCommonEle(list1, list2):
    L = []
    for x in list1:
        if (list2.count(x) >= 1) and (L.count(x) == 0):
            L.append(x)
    return L

main()
                
