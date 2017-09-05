
'''Jennie Walker
jw4043
Jennie_Walker_jw4043_hw10'''

def main1():
    lst = [2, 5, 0, -1, 4, 9]
    #prints lst in random order
    print(createPerm(lst))
    n = int(input("Please enter a positive integer. "))
    lstInt = []
    for x in range(1, n+1):
        lstInt.append(x)
    #prints 1-(n) in random order 
    print(createPerm(lstInt))

def createPerm(lst):
    import random
    random.shuffle(lst)
    return lst


def main2():
    lst1 = createLst()
    lst2 = createLst()
    if len(lst1) == len(lst2):
        print(addList(lst1, lst2))
    else:
        print("Lists are different lengths.") 

def createLst():
    print("Write Done when you are finished with the list.")
    lstInput = 'not Done'
    lst = []
    while (lstInput != "Done"):
        lstInput = input("Please enter a positive integer. ")
        if (lstInput != "Done"):
             lst.append(lstInput)
    return lst

def addList(lst1, lst2):
    lstSum = []
    for x in range(0, len(lst1)):
        xSum = int(lst1[x]) + int(lst2[x])
        lstSum.append(xSum)
    return lstSum


def main3():
    lst = [2,4,6,8,10] 
    print(createPreList(lst))

def createPreList(lst):
    totalList = []
    for x in range(1, len(lst)+1):
        subList = [] 
        for i in lst[:x]:
            subList.append(i)
        totalList.append(subList)
    return totalList 

        

def main4():
    menu = readMenu()
    price = 0.0 
    print("Please enter three customber orders.")
    for cust in range(0, 3):
        print("Please enter your order.")
        order = readCustOrder()
        price += computePrice(menu, order)
    print("The collective price is:", price) 
    tax = price * .085
    print("The tax is", tax)
    tip = price * .15
    print("The tip is", tip)
    total = price + tax + tip 
    print("Your total is:", total) 

def readMenu():
    n = int(input("How many items are on the menu? "))
    foodList = []
    for x in range(0, n):
        listadd = []
        namePrice = input("Enter item in the form of 'name:price'. ")
        colonIndex = namePrice.find(':')
        listadd.append(namePrice[:colonIndex])
        listadd.append(namePrice[colonIndex+1])
        foodList.append(listadd)        
    return foodList

def readCustOrder():
    print("Write 'Done' when you are finished with your order.")
    lstInput = 'not Done'
    lst = []
    while (lstInput != "Done"):
        lstInput = input("What would you like to order? ")
        if (lstInput != "Done"):
             lst.append(lstInput)
    return lst

def computePrice(menu, order):
    price = 0.0 
    for item in order:
        for food in menu:
            if food[0] == item:
                price += float(food[1])
    print(price)
    return price
    
    

main1()
main2()
main3()
main4() 
