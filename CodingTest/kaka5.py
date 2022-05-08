


def solution(rc, operations):


    for operation in operations:
        if operation=="ShiftRow":
            rc.insert(0,rc.pop(len(rc)-1))
        else:
            temp_head=rc[0][0]
            temp_tail=rc[len(rc)-1][len(rc[0])-1]
            for i in range(0,len(rc)-1):
                rc[i][0]=rc[i+1][0]
            for i in range(len(rc)-2,-1,-1):
                rc[i+1][len(rc[0])-1]=rc[i][len(rc[0])-1]

            rc[0].pop(len(rc[0]) - 1)

            rc[0].insert(1,temp_head)


            rc[len(rc)-1].pop(0)

            rc[len(rc)-1].insert(len(rc[0])-2, temp_tail)




    answer = rc

    return answer




rc=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

rc=[[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

operations=["ShiftRow", "Rotate", "ShiftRow", "Rotate"]
#operations=["Rotate"]
print(solution(rc,operations))
#[[1, 6, 7 ,8], [5, 9, 10, 4], [2, 3, 12, 11]]
