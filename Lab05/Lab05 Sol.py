
#Problem 1a
#triangle of *s
number = int(input("Enter number of rows: "))
for i in range(0, number*2, 2):
    print(' '*(number) + '*'*(i+1))
    number -= 1

#Problem 1b ­ Solution 1
#square problem
number2 = int(input("Enter number of rows for square: "))
for i in range(number2):
    row = '$'*number2
    newRow = row.replace('$','#', i)
    print(newRow.replace('$', '%', 1))

#Problem 1b Solution 2
#square problem 
n = int(input("Enter number of rows for square: "))
for i in range(n):
    row=''
    row=row+'#'*(i)+'%'+'$'*(n-i-1)
    print(row)



#Problem 2a
#perfect cubes (i**3) < n
n = int(input("Please enter a positive integer: "))
i = 1
while i**3 < n:
    print(i**3)
    i += 1

#Problem 2b
#prints sum of i**3 for 1 <= i <= n
n = int(input("Please enter a positive integer: "))
cube_sum = 0
for i in range(0,n):
    cube_sum +=(i+1)**3
print(cube_sum)


#Problem 3a
#how many times letter is in a string w for loop
intstr = input('Give me a string: ')
char = input('Give me a letter')
counter = 0
for ch in intstr:
    if ch == char:
        counter+=1
print('Letter ',char , ' appears', counter, 'times in the string.')

#Problem 3b
#how many times letter is in a string w while loop 
intstr = input('Give me a string: ')
char = input('Give me a letter')
counter = 0
current_pos = 0
while(current_pos < len(intstr)):
    if intstr[current_pos ] == char:
        counter += 1
    current_pos +=1
print('Letter ',char , ' appears', counter, 'times in the string.')


#Problem 4a
#counts odd and even digits by going over digits in the string
#iterate over the string and check each character
intstring = input("Enter an integer: ")
odd_counter = 0
even_counter = 0
for ch in intstring:
    if int(ch)%2 == 0:
        even_counter+=1
    else:
        odd_counter+=1
print('There are ', even_counter, ' even digits and ', odd_counter,
              ' odd digits in', intstring)

#Problem 4b
#counts odd and even digits by converting to an int and then using % and // 
#convert input to an integer and get each digit & check
input_number = int(input("Enter an integer: "))
odd_counter = 0
even_counter = 0
      
#get digit at position 1 ­> update n ­>get digit at position 2
n = input_number
while(n!=0):
    current_digit = n % 10
    n = n //10
    if current_digit%2 == 0:
            even_counter+=1
    else:
            odd_counter+=1
print('There are ', even_counter, ' even digits and ', odd_counter,
              ' odd digits in', input_number)


#Problem 5
#draws n-gon w turtle
import turtle 
nSides = int(input("How many sides: "))
wn = turtle.Screen()
nGon = turtle.Turtle()
angle = (nSides-2)*180/nSides
for i in range(nSides):
    nGon.forward(100)
    nGon.lt(180-angle)


#Advanced Problems
#Problem #6
#deletes unwanted blanks (more than 1 in a row) in a string

s = input("Enter a string")
ex_blanks = 0
new_s = ""
i=0
while(i<len(s)):
    if s[i].isspace():
        new_s = new_s+s[i]
        i +=1
        while(s[i].isspace()):
            i +=1
            ex_blanks=1
    else:
        new_s = new_s+s[i]
        i +=1
if ex_blanks == 1:
    print('New string is: ', new_s)
else:
    print("Input string does not have excessive blanks")
