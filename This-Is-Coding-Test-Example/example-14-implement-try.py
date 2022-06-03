#can not solved
def get_max_index(diff):
    max_val = -1e9
    tup_max = (0, 0)
    for i in range(len(diff)):
        if max_val < diff[i][0]:
            max_val = diff[i][0]
            if i == 0:
                tup_max = (len(diff) - 1, i)
            else:
                tup_max = (i - 1, i)

    return tup_max


def solution(n, weak, dist):
    answer = 0

    dist.sort(reverse=True)

    diff = []

    first_last = n - weak[len(weak) - 1] + weak[0]

    for i in range(len(weak)):
        if i == 0:
            diff.append((first_last, weak[i + 1] - weak[i]))
        elif i == len(weak) - 1:
            diff.append((weak[i] - weak[i - 1], first_last))

        else:
            diff.append((weak[i] - weak[i - 1], weak[i + 1] - weak[i]))

    # 맥스먹고 왼쪽오른쪽본후 안감싸지면 가장많이 먹는걸로 선택

    max_index = get_max_index(diff)

    print(diff)
    print(max_index)

    return answer