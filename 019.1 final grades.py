def main():
    grades_file = open("019.0 grades.csv", "r")
    final_grades_file = open("019.2 final grades.csv", "w")


    headers_line = grades_file.readline()

    print("NYU ID", "Final Grade", sep = ',', file = final_grades_file)

    for curr_line in grades_file:
        curr_line = curr_line.strip()
        curr_list = curr_line.split(',')

        NYU_ID = curr_list[0]
        midterm1 = int(curr_list[1])
        midterm2 = int(curr_list[2])
        final_exam = int(curr_list[3])
        homework = int(curr_list[4])
        lab = int(curr_list[5])
        participation = int(curr_list[6])

        final_grade = calc_final_grade(midterm1, midterm2, final_exam,
                                       homework, lab, participation)

        print(NYU_ID, final_grade, sep = ',', file = final_grades_file)


    final_grades_file.close()
    grades_file.close()
    print('done')
        

def calc_final_grade(midterm1, midterm2, final_exam,
                     homework, lab, participation):
    exam_grade = max(0.33*midterm1 + 0.33*midterm2 + 0.34*final_exam,
                     0.3*midterm1 + 0.3*midterm2 + 0.4*final_exam)                    
    final_grade = 0.6*exam_grade + 0.2*homework + 0.15*lab + 0.05*participation
    final_grade = round(final_grade)
    return final_grade


main() 
