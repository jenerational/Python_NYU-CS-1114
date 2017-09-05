
def sumColumn(filename):
    target = open(filename, 'r')
    total = 0
    allNums = target.readlines()
    target.close()
    for i in allNums:
        total += int(i)
    return total 

def main():
    print(sumColumn("Lab11-2 xyz.txt"))

main()
