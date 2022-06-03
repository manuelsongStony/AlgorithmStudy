import re


def solution(words, queries):
    answer = []

    for regular in queries:

        array = list(regular)
        stirng_regular = '^'
        for i in array:
            if i == '?':
                stirng_regular = stirng_regular + '.'
            else:
                stirng_regular = stirng_regular + i
        stirng_regular = stirng_regular + '$'
        count = 0
        for target in words:
            if re.match(stirng_regular, target):
                count += 1
        answer.append(count)
    return answer