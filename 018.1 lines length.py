
def main():
    in_file = open("018.0 Cheerleader.txt", "r", encoding='utf8')
    out_file = open("018.3 Cheerleader - line length.txt", "w", encoding = 'UTF-8')

    line_number = 1
    for line in in_file:
        number_of_words = count_words(line)
        out_line = "line " + str(line_number) + ": " \
                   + str(number_of_words) + " words"
        print(out_line, file = out_file)
        line_number += 1

    in_file.close()
    out_file.close()
    print('done')

def count_words(string):
    words_list = string.split()
    return len(words_list)

main() 

