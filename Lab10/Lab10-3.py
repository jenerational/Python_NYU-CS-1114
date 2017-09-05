
def main():
    lst = [123, 'xyz', 'zara', 'abc', 123]
    item = 123
    print(allIndices(lst, item))

def allIndices(lst, item):
    L = []
    itemCount = []
    for x in lst:
        L.append(x)
        if x == item:
            itemCount.append(len(L)-1)
    if len(itemCount) == 0:
        itemCount = -1
    return itemCount 
    
main()
