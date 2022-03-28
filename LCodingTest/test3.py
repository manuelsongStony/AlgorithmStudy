def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []

    team_num=[0]*(num_teams+1)

    for emp in employees:
        employee=emp.split()
        team_num[int(employee[0])]+=1
        team_num
    #print(team_num)
    for emp in employees:
        employee=emp.split()

        for work in employee[1:]:
            if work in office_tasks:
                #print(emp)
                answer.append(employees.index(emp)+1)



        """
        if team_num[int(employee[0])] <1:
            answer.append(employees.index(emp)+1)
        """
    key_answer=[]

    if len(answer) != 0:
        re = answer.pop()
    else:
        re = 0

    for i in range(len(employees),0,-1):

        if i!= re:
            key_answer.append(i)
        else:
            if len(answer) != 0:
                re = answer.pop()
            else:
                re = 0

    key_answer.reverse()
    return key_answer


num_teams=3
remote_tasks=["development","marketing","hometask"]
office_tasks=["recruitment","education","officetask"]
employees=["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]
print(solution(num_teams, remote_tasks, office_tasks, employees))