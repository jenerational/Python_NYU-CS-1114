
#Question 4:

print("Enter the amount of time that John and Bill have worked.")
#asks for user input 
daysJohn = int(input("Please enter the number of days John has worked:"))
hoursJohn = int(input("Please enter the number of hours John has worked:")) 
minutesJohn = int(input("Please enter the number of minutes John has worked:"))
daysBill = int(input("Please enter the number of days Bill has worked:"))
hoursBill = int(input("Please enter the number of hours Bill has worked:"))
minutesBill = int(input("Please enter the number of minutes Bill has worked:"))

totalJohn = daysJohn*24*60 + hoursJohn*60 + minutesJohn
totalBill = daysBill*24*60 + hoursBill*60 + minutesBill 

totalMinutes = totalJohn+totalBill
totalDays = totalMinutes//1440
totalMinutes = totalMinutes % 1440
totalHours = totalMinutes // 60
totalMinutes = totalMinutes % 60


print("The total time both of them worked together is:", str(totalDays),
      "days,", str(totalHours), "hours, and", str(totalMinutes), "minutes.")
