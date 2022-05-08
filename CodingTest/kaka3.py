def solution(alp, cop, problems):


    answer = 0

    answer=max(problems, key=lambda x: x[1])[1]
    answer = max(problems, key=lambda x: x[0])[0]


    return answer







alp=10
cop=10
problems=[[10,15,2,1,2],[20,20,3,3,4]]
print(solution(alp, cop, problems))