
'''Jennie Walker
jw4043
Jennie_Walker_jw4043_hw12
This program prints the metro stops of a user selected line 
'''

def listPrint(line):
    stopData = open("train_stop_data-Mac.csv", 'r')
    #reads through first two lines
    stopData.readline()
    stopData.readline()
    lineList = []
    for entry in stopData:
        stopInfo = entry.split(",")
        stopNum = stopInfo[0]
        if stopNum[0] == line:
            try:
                float(stopNum)
            except ValueError:
                stopNum = stopNum[:len(stopNum)-1]
            if stopInfo[2] not in lineList:
                lineList.append(stopInfo[2])
    listPrint = line + " line: "
    for x in lineList:
        listPrint += x + ", "
    print(listPrint) 
                
                        
        
    stopData.close()

def main():
    doneStatus = False
    while doneStatus == False:
        userLine = input("Please enter a train line, or 'done' to stop: ")
        if userLine != "done":
            listPrint(userLine)
        else:
            doneStatus = True
        
main()
