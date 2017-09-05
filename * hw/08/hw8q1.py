

def main():
    #asks user for input 
    dayNum = int(input("How many days are there in the month? "))
    dayStart = int(input("What day does the month start on? (1-7) "))
    dayList()
    dayPrint(dayNum, dayStart)

def dayList():
    #prints days
    print("Mo \t Tu \t We \t Th \t Fr \t Sa \t Su")

def dayPrint(dayNum, dayStart):
    #creates first week string, starting on correct day
    weekNum = ((dayNum + dayStart-2) // 7) + 1
    ln = ""
    ln += "\t" * (dayStart-1)
    #fills in other days in first week
    for z in range (1, 9-dayStart):
        ln += str(z) + "\t"
    print(ln) 
    #fills in other weeks 
    for i in range (2, weekNum):
        ln = ""
        for x in range((i-1)*7-dayStart+2, (i*7)+2 - dayStart):
            ln += str(x) + "\t"
        print(ln)
    ln = "" 
    #fills last week, stopping at last day 
    for c in range((weekNum-1)*7-dayStart+2, dayNum+1):
        ln += str(c) + "\t"
    print(ln)
    
main() 
