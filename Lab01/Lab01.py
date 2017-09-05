print("My Name")

num1 = int(input("Enter an integer."))
num2 = int(input("Enter a second integer."))
sum1 = str(num1 + num2)
product = str(num1 * num2)
difference = str(num1 - num2) 
print("Their sum is: " + sum1)
print("Their product is: " + product)
print("Their difference is: " + difference) 


fah = int(input("Enter a Fahrenheit temperature."))
cel = str((fah - 32) * (5/9))
fah = str(fah)
print("Your Fahrenheit temperature is: " + fah + ". In Celcius, it is: " + cel)

num3 = int(input("Enter a number."))
num3bin = bin(num3)
num3hex = hex(num3)
print("Your number in binary is: " + num3bin)
print("Your number in hexidecimal is: " + num3hex) 
