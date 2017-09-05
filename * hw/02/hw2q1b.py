
#Question 1b

userWeight = int(input("Please enter your weight in pounds.")) 
userHeight = int(input("Please enter your height in inches."))
weightKG = userWeight * 0.453592
heightM = userHeight *  0.0254
userBMI = weightKG/(heightM**2)
print("Your BMI is", str(userBMI) + ".") 

