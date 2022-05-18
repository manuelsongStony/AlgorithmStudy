def solution(answers):
    answer = []

    first_man = []
    second_man = []
    third_man = []

    k = 1

    for i in range(1, len(answers) + 1):
        if i % 5 == 0:
            first_man.append(5)
        else:
            first_man.append(i % 5)

        if i % 2 == 1:
            second_man.append(2)
        else:
            if k == 6:
                k = 1
            if k==2:
                k+=1
            second_man.append(k)
            k += 1

        third_variable = i % 10

        if third_variable == 1 or third_variable == 2:
            third_man.append(3)
        elif third_variable == 3 or third_variable == 4:
            third_man.append(1)
        elif third_variable == 5 or third_variable == 6:
            third_man.append(2)
        elif third_variable == 7 or third_variable == 8:
            third_man.append(4)
        else:
            third_man.append(5)

    first_man_correct = 0
    second_man_correct = 0
    third_man_correct = 0

    print(first_man)
    print(second_man)
    print(third_man)


    for i in range(len(answers)):
        if answers[i] == first_man[i]:
            first_man_correct += 1
        if answers[i] == second_man[i]:
            second_man_correct += 1
        if answers[i] == third_man[i]:
            third_man_correct += 1

    max_value = max(first_man_correct, second_man_correct, third_man_correct)

    if first_man_correct == max_value:
        answer.append(1)
    if second_man_correct == max_value:
        answer.append(2)
    if third_man_correct == max_value:
        answer.append(3)

    return answer


print(solution([1,2,3,4,5,1,2,3,4,5,6,7,8,8,8,8,8]))