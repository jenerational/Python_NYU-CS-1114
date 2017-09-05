
def main():
    in_file = open("018.0 Cheerleader.txt", "r", encoding='utf8')
    out_file = open("018.4 Cheerleader with line numbers.txt", "w", encoding = 'UTF-8')

    line_number = 1
    for line in in_file:
        out_line = str(line_number) + ". " + line
        print(out_line, end = '', file = out_file)
        line_number += 1

    in_file.close()
    out_file.close()
    print('done')

main() 
