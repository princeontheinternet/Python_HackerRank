# Use of Dictionary

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    print(student_marks)
    query_name = input()

    for st_name, st_marks in student_marks.items():
        if query_name == st_name:
            len_of_mark_list = len(st_marks)
            avg = sum(st_marks)/len_of_mark_list
            print("{0:0.2f}".format(avg))

# Another way

    # res = sum(student_marks[query_name])/len(student_marks[query_name])
    # print("{:.2f}".format(res))


