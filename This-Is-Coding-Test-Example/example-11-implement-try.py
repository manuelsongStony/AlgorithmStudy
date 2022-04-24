"""
n, k, l = 6, 3, 3  # nxn, 사과, 방향
apple = [[3, 4], [2, 5], [5, 3]]
direction = [(3, "D"), (15, "L"), (17, "D")]

n,k,l=10,4,4
apple=[[1,2],[1,3],[1,4],[1,5]]
direction=[(8,"D"),(10,"D"),(11,"D"),(13,"L")]
"""
n,k,l=10,5,4
apple=[[1,5],[1,3],[1,2],[1,6],[1,7]]
direction=[(8,"D"),(10,"D"),(11,"D"),(13,"L")]


head_postion = [0, 0]
tail_positions = []
dxdy = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 왼쪽 향해 이동 => 1열씩이동

time = 0
direction_index = 0
dxdy_j = 0
while (head_postion not in tail_positions and head_postion[0] > -1 and
       head_postion[0] < n and head_postion[1] > -1 and head_postion[1] < n):

    time += 1

    tail_positions.insert(0,[head_postion[0],head_postion[1]]) #tail_positions.append(head_postion) 이면 헤드 바뀔때 다같이바뀜
    head_postion[0] += dxdy[dxdy_j][0]
    head_postion[1] += dxdy[dxdy_j][1]

    if head_postion not in apple:
        tail_positions.pop(-1)
    else:
        apple.remove(head_postion)

    if direction_index == l:
        direction_index = 0

    if time == direction[direction_index][0]:

        if direction[direction_index][1] == "L":
            if dxdy_j == 3:
                dxdy_j = 0
            else:
                dxdy_j += 1
        else:
            if dxdy_j == 0:
                dxdy_j = 3
            else:
                dxdy_j -= 1

        direction_index += 1
    print(time)
    for i in range(n):
        for j in range(n):

            if [i,j] in tail_positions:
                print("t", end='')
            elif [i,j] ==head_postion:
                print("h", end='')
            elif [i, j] in apple:
                print("@", end='')
            else: print("*", end='')
        print()
    print()
print(time)
