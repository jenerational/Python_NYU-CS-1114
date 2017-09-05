
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
            htmlTable += "\t<tr>\n\t\t<th>"
            for ch in row:
                if ch != ",":
                    htmlTable += ch
                else:
                    htmlTable += "</th>\n\t\t<th>"
            htmlTable += "\t</tr>\n" 
        else:
            htmlTable += "\t<tr>\n\t\t<td>"
            for ch in row:
                if ch != ",":
                    htmlTable += ch
                else:
                    htmlTable += "</td>\n\t\t<td>"
            htmlTable += "\t</tr>\n" 
        line += 1 
    return htmlTable  
    
    

def main():
    print(htmlTableGen("lab11_q4_samplefile1-mac.csv")) 
    
main()
