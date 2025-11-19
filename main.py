from pandas.core.computation.common import result_type_many

if __name__ == '__main__':

    total =[]
    number = input("input number :")
    result = []
    final =[]
    for i in range(int(number)):
        python_students = []
        name = input()
        score = float(input())
        python_students.append(name)
        python_students.append(score)
        total.append(python_students)

        print(total)

    for x in range(int(number)):
        result.append(total[x][1])
    print(result)
    initial_result = sorted(set(result))
    second_lowest = initial_result[1]


    for y in range(len(total)):
        if second_lowest == total[y][1]:
            final.append(total[y][0])
            final.sort()
    for z in final:
        print(z)





