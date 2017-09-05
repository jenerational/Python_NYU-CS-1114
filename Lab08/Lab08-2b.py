
#CS 1114 Lab 8-2b
#October 30, 2015

print("Exercise 2b: ")
def main():
    userStr = input("Please enter a DNA string: ")
    userSubstr = input("Please enter a DNA substring. ")
    print(multiFind(userStr, userSubstr))

def multiFind(userStr, userSubstr):
    strStarts = ""
    if len(userSubstr) > len(userStr):
        return -1
    else:
        for ch in userStr:
            if ch == userSubstr[0]:
                strStart = userStr.index(ch)
                chCount = 0
                for i in range(0, len(userSubstr)):
                    if userSubstr[i] == userStr[strStart+i]:
                        chCount += 1
                if chCount == len(userSubstr):
                    strStarts += (str(strStart) + ",")
        if strStarts != "":
            return(strStarts[:len(strStarts)-1])
        else:
            return -1 
                
main()


#non-function code:
#
#userStr = input("Please enter a DNA string: ")
#userSubstr = input("Please enter a DNA substring. ")
#if len(userSubstr) > len(userStr):
#    print("-1")
#else:
#    for ch in userStr:
#        if ch == userSubstr[0]:
#            strStart = userStr.index(ch)
#            chCount = 0
#            for i in range(0, len(userSubstr)):
#                if userSubstr[i] == userStr[strStart+i]:
#                    chCount += 1
#    if chCount == len(userSubstr):
#        print(str(strStart))
#    else:
#          print("-1")
                
                    
