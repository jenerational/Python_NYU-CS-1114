
import time
import random

#insertion w 10000 rand inputs
print("Insertion Program:")

#sets up list
alist = []
for listAdd in range(0, 10000):
    alist.append(random.randint(0,1234567))

t0 = time.time()

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

insertionSort(alist)
t1 = time.time()
print(alist)
runTime = t1 - t0
print("\nRun Time:")
print(runTime, "seconds.")


#quicksort w 10000 rand inputs

print("\n\nQuicksort Program:") 

for listAdd in range(0, 10000):
    alist.append(random.randint(0,1234567))

t0 = time.time()

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

quickSort(alist)
t1 = time.time()

print(alist)

runTime = t1 - t0
print("\nRun Time:")
print(runTime, "seconds.")


#selection with 10000 rand inputs
print("\n\nSelection Program:") 

for listAdd in range(0, 10000):
    alist.append(random.randint(0,1234567))

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

selectionSort(alist)
t1 = time.time()

print(alist)

runTime = t1 - t0
print("\nRun Time:")
print(runTime, "seconds.")

