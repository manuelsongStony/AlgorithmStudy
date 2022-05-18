def solution(arr):
    answer = []
    before_number=-1
    for i in arr:
        if i ==before_number:
            continue
        else:
            answer.append(i)
            before_number=i
    return answer