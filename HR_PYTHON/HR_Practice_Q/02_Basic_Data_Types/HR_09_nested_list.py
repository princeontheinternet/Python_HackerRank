# NESTED LIST and SECOND LOWEST ELEMENT


"""
Given the names and grades for each student in a class of  students,
    store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
    order their names alphabetically and print each name on a new line.

    --> Sample Input:
        ------------
        5
        Harry
        37.21
        Berry
        37.21
        Tina
        37.2
        Akriti
        41
        Harsh
        39

    --> Sample Output:
        --------------
        Berry
        Harry
"""


if __name__ == '__main__':

    student_list = []
    marks = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        student_list.append(student)
        marks.append(score)

    print(marks)    # TODO: remove after testing
    print(student_list) # TODO: remove after testing

    second_lowest_score = sorted(list(set(marks)))[1]

    student_name_second_lowest_score = [i[0] for i in student_list if i[1] == second_lowest_score]

    print(student_name_second_lowest_score)  # TODO: remove after testing

    for names in sorted(student_name_second_lowest_score):  # using sorted as the names should be sorted
        print(names)



