
def main():
    lst = [123, 'xyz', 'zara', 'abc', 123]
    item = 123
    print(myindex(lst, item))

def myindex(lst, item):
    lstIndex = []
    for x in lst:
        lstIndex.append(x)
        if x == item:
            return (len(lstIndex)-1)
            
main()
