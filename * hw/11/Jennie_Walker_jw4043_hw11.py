
'''Jennie Walker
jw4043
Jennie_Walker_jw4043_hw11'''

#Part A
def cleanData(compWeatherFile, cleanedWeatherFile):
    compData = open(compWeatherFile, 'r')
    cleanData = open(cleanedWeatherFile, 'w') 
    #reads through first two lines
    compData.readline()
    compData.readline()
    cleanData.write("City, Date, High, Low, Precipitation \n")
    for line in compData:
        entry = line.split(",")
        try:
            float(entry[8])
        except ValueError:
            entry[8] = '0'
        cleanLine = entry[0] + ", " + entry[1] + ", " + entry[2] + ", " + entry[3] + ", " + entry[8]
        #reads through empty line 
        compData.readline()
        cleanData.write(cleanLine + "\n")
    compData.close()
    cleanData.close()
        
#Part B
def FtoC(fTemp):
    cTemp = (float(fTemp) - 32) * (5/9)
    return cTemp

def INtoCM(inches):
    centimeters = float(inches) * 2.54
    return centimeters
    
def convertDataToMetric(impWeatherFile, metWeatherFile):
    impData = open(impWeatherFile, 'r')
    metData = open(metWeatherFile, 'w')
    #deletes header line 
    impData.readline()
    #rewrite header line in new file
    metData.write("City, Date, High, Low, Precipitation \n")
    for line in impData:
        entry = line.split(", ")
        entry[2] = str(FtoC(entry[2]))
        entry[3] = str(FtoC(entry[3]))
        entry[4] = str(INtoCM(entry[4]))
        metLine = entry[0] + ", " + entry[1] + ", " + entry[2] + ", " + entry[3] + ", " + entry[4]
        metData.write(metLine + "\n")

    impData.close()
    metData.close()

#Part C
def printAvgPerMo(city, weatherFile, unitType):
    print("Average temperatures for", city)
    if unitType == 'imperial':
        T = 'F'
    elif unitType == 'metric':
        T = 'C'
    highSums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    lowSums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    dayCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    highAvg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    lowAvg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    for month in range(0, 12):
        dataFile = open(weatherFile, 'r')
        dataFile.readline()
        dataFile.readline()
        for line in dataFile:
            entry = line.split(", ")
            if city == entry[0]:
                date = entry[1]
                date = date.split('/')
                if int(date[0]) == (month+1):
                    highSums[month] += float(entry[2])
                    lowSums[month] += float(entry[3])
                    dayCount[month] += 1
                    dataFile.readline()
                else:
                    dataFile.readline()
                    dataFile.readline() 
        highAvg[month] = highSums[month]//dayCount[month]
        lowAvg[month] = lowSums[month]//dayCount[month]
        dataFile.close()
        print(str(months[month]) + ":", str(highAvg[month]) + T, "High,", str(lowAvg[month]) + T, "Low") 

#Part D    
def highTempFinder(weatherFile, city, unitType):
    if unitType == 'imperial':
        T = 'F'
    elif unitType == 'metric':
        T = 'C' 
    highTemp = 0
    dataFile = open(weatherFile, 'r')
    for line in dataFile:
        entry = line.split(", ")
        if city == entry[0]:
            if float(entry[2]) > float(highTemp):
                highTemp = entry[2]
        dataFile.readline()
    print("The highest temperature in", city, "is:", highTemp + "˚" + T)
                
                
    
                
    
    

def main():
    #Part A
    print("Running Part A")
    compWeatherFile = "weather.csv"
    cleanedWeatherFile = "imperialWeather.csv"
    cleanData(compWeatherFile, cleanedWeatherFile)
    #Part B
    print("Running Part B")
    metWeatherFile = "metricWeather.csv"
    convertDataToMetric(cleanedWeatherFile, metWeatherFile)
    #Part C
    print("Running Part C")
    printAvgPerMo("San Francisco", "imperialWeather.csv", "imperial")
    printAvgPerMo("New York", "metricWeather.csv", "metric")
    printAvgPerMo("San Jose", "imperialWeather.csv", "imperial")
    #Part D
    print("Running Part D")
    highTempFinder('metricWeather.csv', 'San Francisco', 'metric')
    
    

main()
