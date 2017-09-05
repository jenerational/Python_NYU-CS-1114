
inputNum = int(input("Please enter a number."))

outputNum = ""
while (inputNum >= 1000):
    outputNum = outputNum+"M"
    inputNum -= 1000
while (inputNum < 1000) and (inputNum >= 500):
    outputNum = outputNum+"D"
    inputNum -=500
while (inputNum < 500) and (inputNum >= 100):
    outputNum = outputNum+"C"
    inputNum -= 100
while (inputNum < 100) and (inputNum >= 50):
    outputNum = outputNum+"L"
    inputNum -= 50
while (inputNum <50) and (inputNum >= 10):
    outputNum = outputNum+"X"
    inputNum -= 10
while (inputNum < 10) and (inputNum >= 5):
    outputNum = outputNum+"V"
    inputNum -= 5
while (inputNum >= 1):
    outputNum = outputNum+"I"
    inputNum -= 1


print(outputNum) 
