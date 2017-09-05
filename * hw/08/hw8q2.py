def main():
    #asks for user input
    userPhr = input("Please enter a phrase. ")
    #adds space to phrase for part c
    userPhr = userPhr + " "
    #prints functions
    print(findFirst(userPhr))
    print(findOther(userPhr))
    print(revPhr(userPhr))

def findFirst(userPhr):
    #uses first space to find the first word
    spaceIndex = userPhr.find(" ")
    word1 = userPhr[:spaceIndex]
    return word1

def findOther(userPhr):
    #uses first space to find the rest of the word
    spaceIndex = userPhr.find(" ")
    wordOther = userPhr[spaceIndex+1:]
    return(wordOther)


def revPhr(userPhr):
    spaceCount = 0
    #counts spaces to find word count
    for ch in userPhr:
        if ch == " ":
            spaceCount += 1
    #creates empty list
    lst = []
    #sets previous function in for loop to separate each word
    #adds each separate word into previously empty list
    for x in range(0, spaceCount):
        word1 = findFirst(userPhr)
        userPhr = findOther(userPhr)
        lst.append(word1)
    #creates empty string
    retPhr = ""
    #uses negative step to add words in to string in reverse order 
    for z in range(len(lst), 0, -1):
        retPhr += lst[z-1] + " "
    #returns string of reverse words 
    return retPhr

main()
