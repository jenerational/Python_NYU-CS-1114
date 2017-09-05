
#sorts out the list
def mystery1(l):
    for fillslot in range(len(l)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if l[location]>l[positionOfMax]:
               positionOfMax = location

       temp = l[fillslot]
       l[fillslot] = alist[positionOfMax]
       l[positionOfMax] = temp

#shifts a list by n
def mystery2(l, n):
    lstCopy = []
    for z in range(0,n):
        lstCopy.append(l[z])
    for i in range(len(l)):
        l[i] = l[(i + n) % len(l)]
    for x in range(n):
        l.pop()
    for d in range(n):
        l.append(lstCopy[d])
    
        
    
#finds the remainder of q/d, starts over if there is a remainder 
def mystery3(q, d): 
    if d == 0: 
        return q
    else:
        return mystery3(d, q % d)

alist = [54,26,93,17,77,31,44,55,20]
print("Original list:" + str(alist) + "\n")
mystery1(alist)
print("Mystery 1:" + str(alist) + "\n")

alist = [54,26,93,17,77,31,44,55,20]
print("Original list:" + str(alist) + "\n") 
mystery2(alist, 3)
print("Mystery 2: " + str(alist) + "\n")

print("Mystery 3: " + str(mystery3(20, 8)))
