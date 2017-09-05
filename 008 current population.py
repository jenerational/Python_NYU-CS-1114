
inputYear = int(input("Please enter a year."))
#calculates number of second in gap between 2015 and input year
yearGapSec = (inputYear - 2015) * 365 * 24 * 60 * 60
#identifies number of sections per birth, death, of additional immigrant 
birth = 7
death = 13
immigrant = 35 
#calulates number of births in year gap
birthGap = yearGapSec // 7
deathGap = yearGapSec // 13
immigrantGap = yearGapSec // 35
#calculates current population 
population = 307357870 + birthGap - deathGap + immigrantGap
#prints
print("The current population is", str(population), ".")
