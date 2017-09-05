
'''
Jennie Walker
jw4043
Jennie_Walker_jw4043_hw9.py
'''

#imports math function
import math

def mainQ1():
    #preset q values
    lst = [-19, -3, 20, -1, 0, 25]
    print(maxAbsVal(lst)) 

def maxAbsVal(lst):
    #creates blank list 
    lstAV=[]
    #adds abs val of each list item to new list
    for x in lst:
        lstAV.append(math.fabs(x))
    #sets list max at 0
    lstMax = 0
    for x in lstAV:
        #if abs val is bigger than previous, it becomes new list max
        if x > lstMax:
            lstMax = x
    return lstMax
        
def mainQ2():
    #preset q values 
    lst = ['a', 'b', 10, 'bb', 'a']
    val = 'a'
    print(findAll(lst, val))

def findAll(lst, val):
    #creates empty list for index values
    L = []
    lstIndex = []
    for z in lst:
        L.append(z)
        if z == val:
            lstIndex.append(len(L)-1)
    return lstIndex

def mainQ3():
    lst1 = [1, 2, 3, 4, 5, 6]
    revLst1 = reverse1(lst1)
    print("After reverse1, lst1 is ", lst1,
          "and the returned list is ", revLst1)
    lst2 = [1, 2, 3, 4, 5, 6]
    lst2 = reverse2(lst2)
    print("After reverse2, lst2 is ", lst2)

def reverse1(lst):
    L = []
    for item in range(len(lst), 0, -1):
        L.append(item)
    return L


def reverse2(lst):
    lst.reverse()
    return lst

def mainQ4():
    inputBIN = input("Please enter a string to encode: ") 
    outputBIN = (runLenEn(inputBIN))
    print(outputBIN)
    print(runLenDec(outputBIN))

def runLenEn(inputBIN):
    currPos = 0
    outputStr=[]
    while(currPos < len(inputBIN)):
        numCounter = 1
        flag = inputBIN[currPos] 
        currPos += 1
        while(currPos < len(inputBIN) and flag == inputBIN[currPos]):
              numCounter += 1
              currPos+=1
        L = []
        L.append(flag)
        L.append(numCounter)
        outputStr.append(L)
    return (outputStr)
    
def runLenDec(outputBIN):
    outputStr = ""
    for x in outputBIN:
        outputStr += x[0] * int(x[1])
    return outputStr

mainQ1()
mainQ2()
mainQ3()
mainQ4()
