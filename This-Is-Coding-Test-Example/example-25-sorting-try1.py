#https://programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    stages.sort()
    array = [0] * (N + 2)

    for i in stages:
        array[i] += 1

    total_count = len(stages)

    odd_array = []
    for i in range(1, N + 1):

        if total_count == 0:
            odd_array.append((i, 0))
        else:
            odd_array.append((i, array[i] / total_count))
            total_count -= array[i]

    odd_array.sort(key=lambda x: (-x[1], x[0]))

    answer = []
    for i in odd_array:
        answer.append(i[0])

    return answer