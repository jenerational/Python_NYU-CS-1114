
def writeName(filename, firstName, lastName):
    target = open(filename, 'w')
    target.write(firstName)
    target.write(" ")
    target.write(lastName)
    target.close

def main():
    writeName("Lab11-1 xyz.txt", "Charles", "Darwin") 

main() 
