
def htmlTableGen(filename):
    import csv
    #writes basic html setup
    htmlTable = "<!DOCTYPE html> \n <html> \n \n <table>\n"
    #starts reading csv file
    line = 1
    target = open(filename, 'r')
    tarRead = csv.reader(target)
    for row in tarRead:
        if line == 1:
            #header print 
            htmlTable += "\t<tr>\n"
            for elem in row:
                htmlTable += "\t\t<th>"
                htmlTable += elem
                htmlTable += "</th>\n"
            line = 2
            htmlTable += "\t</tr>\n" 
        else:
            htmlTable += "\t<tr>\n"
            for elem in row:
                htmlTable += "\t\t<td>"
                htmlTable += elem
                htmlTable += "</td>\n"
            line = 2
            htmlTable += "\t</tr>\n" 
    return htmlTable  
    
    

def main():
    print(htmlTableGen("lab11_q4_samplefile1-mac.csv")) 
    
main()
