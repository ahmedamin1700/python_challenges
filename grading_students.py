# HackerRank Challenge.
# Ahmed Amin 19 / 10 / 2020.

# HackerLand University has the following grading policy:
#
# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's grade according to these rules:
#
# If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple
# of 5. If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

def grading_students(grades):
    final_grades = []
    for n in range(len(grades)):
        if grades[n] < 38:
            final_grades.append(grades[n])
        else:
            if grades[n] % 5 == 0:
                final_grades.append(grades[n])
            else:
                final_grade = grades[n]
                while final_grade % 5 != 0:
                    final_grade += 1
                diff = final_grade - grades[n]
                if diff < 3:
                    final_grades.append(final_grade)
                else:
                    final_grades.append(grades[n])
    return final_grades


grades_input1 = [73, 67, 38, 33]
print(grading_students(grades_input1))
