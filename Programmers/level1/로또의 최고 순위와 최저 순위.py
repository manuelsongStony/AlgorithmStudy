def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()
    count = 0
    i = 0
    j = 0

    while i < 6 and j < 6:
        if lottos[i] == win_nums[j]:
            count += 1
            i += 1
            j += 1
        elif lottos[i] > win_nums[j]:
            j += 1
        else:
            i += 1

    """
    for i in range(6): 
        for j in range(6):
            if lottos[i] ==win_nums[j]:
                count+=1
    """

    zero_count = 0

    for ele in lottos:
        if ele == 0:
            zero_count += 1

    low_socre = 7 - count

    high_socre = 7 - count - zero_count

    answer = []

    if low_socre == 7:
        low_socre = 6
    if high_socre == 7:
        high_socre = 6
    answer.append(high_socre)
    answer.append(low_socre)
    return answer