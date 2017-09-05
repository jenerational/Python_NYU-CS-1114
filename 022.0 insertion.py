print("Insertion Program:")

import time
t0 = time.time()

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20,10]
insertionSort(alist)
print(alist)

t1 = time.time()

runTime = t1 - t0
print(runTime)
