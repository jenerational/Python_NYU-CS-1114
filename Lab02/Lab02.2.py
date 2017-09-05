
print("Exercise 6:")
#asks user for birthday
birthDate = input("Please enter your birthday in YYYYMMDD format.")
#asks user for today's date 
todayDate = input("Please enter today's date in YYYYMMDD format.")
#separates year strings
birthYear = int(birthDate[:4])
todayYear = int(todayDate[:4])
#separates months from strings
birthMonth = int(birthDate[4:6])
todayMonth = int(todayDate[4:6])
#separates days from strings
birthDay = int(birthDate[6:])
todayDay = int(todayDate[6:])
#Calculates days 
birthDays = (birthYear * 365) + (birthMonth * 30) + (birthDay)
todayDays = (todayYear * 365) + (todayMonth * 30) + (todayDay)
#calculates difference in total days
totalDays = (todayDays - birthDays)
#calculates number of years
totalYear = totalDays//365
#calculates remainder of days
totalDays = totalDays%365
#calculates number of months
totalMonth = totalDays//30
#calculates remainder of days
totalDay = totalDays%30
#prints
print("You are", str(totalYear), "years,", str(totalMonth), "months, and",
      str(totalDay), "days.")



print("Exercise 7:") 
#asks user for first length
length1ft = int(input("Please enter the first length's number of feet."))
length1in = int(input("Please enter the first length's number of inches."))
#asks user for second length
length2ft = int(input("Please enter the second length's number of feet."))
length2in = int(input("Please enter the second length's number of inches."))
#calculates total number of inches
length1 = (length1ft * 12) + (length1in)
length2 = (length2ft * 12) + (length2in)
#calculates inches sum
totalLength = length1 + length2
#converts back into feet and inches
totalFeet = totalLength // 12
totalInches = totalLength % 12
#prints
print("Their sum is", str(totalFeet), "feet and", str(totalInches), "inches.")



