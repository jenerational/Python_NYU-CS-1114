print("Selection Program:") 

import time

t0 = time.time()

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20,10]
selectionSort(alist)
print(alist)

t1 = time.time()

runTime = t1 - t0
print(runTime)
