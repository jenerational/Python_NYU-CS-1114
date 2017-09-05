
def addEntry(phonebook, name, phonenumber):
    if isValid(phonenumber) == False:
        return 
    for key in phonebook:
        if key == name:
            #prints error message
            print(name, "is already in the phonebook.")
            return
    #dict[key] = value --> adds to dictionsary 
    phonebook[name] = phonenumber

def lookup(phonebook, name):
    for key in phonebook:
        if key == name:
            return phonebook[name]
    print(name, "has not been found.") 

def isValid(phonenumber):
    valid = True
    if len(phonenumber) != 10:
        valid = False
    for dig in phonenumber:
        if dig.isdigit() == False:
            valid = False
    if valid == False:
        print(phonenumber, 'is not valid.')
    return valid 
        
def printAll(phonebook):
    #print all of dict
    for key in phonebook:
        print(key, phonebook[key])
    

def main():
    phoneTxt = open('Lab12-phonebook.txt', 'r')
    phonebook = {}
    for line in phoneTxt:
        entry = line.split(" ")
        name = entry[1] + " " + entry[0][:len(entry[0])-1]
        phonenumber = entry[2][:len(entry[2])-1]
        addEntry(phonebook, name, phonenumber)
    printAll(phonebook)
    lookup(phonebook, 'Evan Gallagher') 

main() 

