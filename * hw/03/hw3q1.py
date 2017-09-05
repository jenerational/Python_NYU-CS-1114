
#Question 1a

userWeight = int(input("Please enter your weight in kilograms.")) 
userHeight = int(input("Please enter your height in meters."))
userBMI = userWeight/(userHeight**2)
if (userBMI < 18.5):
    status = "Underweight"
if (userBMI >=18.5) and (userBMI < 25):
    status = "Normal"
if (userBMI >= 25) and (userBMI < 30):
    status = "Overweight"
if (userBMI >=30):
    status = "Obese" 
print("Your BMI is", str(userBMI), "and you are", status + ".") 

