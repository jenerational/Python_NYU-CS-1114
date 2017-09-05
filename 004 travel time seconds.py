#Jennie Walker, 09/16/2015, CS 1114
#tells user it is about to prompt them for travel time 
print("Please enter the length of travel in days, hours, minutes and seconds.")
#individually asks for each input 
days = int(input("Number of days:"))
hours = int(input("Number of hours:"))
minutes = int(input("Number of minutes:"))
seconds = int(input("Number of seconds:")) 

#total number of seconds = number of days times the amount of seconds in a day 
numOfSeconds = days * 86400
#redefines total # as self + amt of hours times seconds in an hour
numOfSeconds = numOfSeconds + (hours * 3600)
#redefines total # as self + amt of min time seconds in a minute
numOfSeconds = numOfSeconds + (minutes * 60)
#redefines self as self plus number of seconds. Converts total to string
numOfSeconds = str(numOfSeconds + seconds)


#prints result to user. 
print("Your travel time of " + str(days) + "days, " + str(hours) + "hours, "
      + str(minutes) + "minutes, and " + str(seconds) + "seconds is "
      + numOfSeconds + " seconds.") 


totalSeconds = int(input("Please enter the total amount of seconds."))

secondInMinte = 60
minutesInHour = 60
hoursInDay = 24
secondsInHour = mintesInHour*secondsInMinute
secondsInDay = hoursInDay*secondsInHour

remainingSeconds = totalSeconds

fullDays = remainingSeconds // secondsInDay
remainingSeconds = remainingSeconds % secondsInDay

fullHours = remainingSeconds // secondsInHour
remainingSeconds = remainingSeconds % secondsInMinute

fullMinutes = remainingSeconds // secondsInMinute
remainingSeconds = remainingSeconds % secondsInMinute 

print(totalSeconds, "seconds are", \
      fullDays, "days,", \
      fullHours, "hours,", \
      fullMinutes, "minutes, and", \
      remainingSeconds, "seconds.") 


