
def main():
    lst = [123, 'xyz', 'zara', 'abc', 123]
    item = 123
    print(mycount(lst, item))

def mycount(lst, item):
    count = 0
    for x in lst:
        if x == item:
            count += 1
    return count 

main()
