import copy

#ㄷ귿자 ㄹ을자 고려안함 유턴? : searched 그래프를 새로만들던지 아니면, 1 로바꾸기?
def dfs_search(board, turned, position1x, position1y, position2x, position2y, count):


    if position2x == len(board) - 1 and position2y == len(board) - 1:
        return count
    if position1x == len(board) or position1y == len(board) or position2x == len(board) or position2y == len(board) :
        return count + 10e9
    if board[position1x][position1y] == 1 or board[position2x][position2y] == 1:
        return count + 10e9

    """
    print(count)
    copyed_board = copy.deepcopy(board)
    copyed_board[position1x][position1y] = 9
    copyed_board[position2x][position2y] = 9
    for i in copyed_board:
        print(i)
    print()
"""
    a1 = 10e9
    a2 = 10e9
    a3 = 10e9
    a4 = 10e9
    # 2번돌리기 없음
    if turned == True:
        a1 = dfs_search(board, False, position1x + 1, position1y, position2x + 1, position2y, count + 1)
        a2 = dfs_search(board, False, position1x, position1y + 1, position2x, position2y + 1, count + 1)
    else:
        if position1x == position2x:
            a1 = dfs_search(board, False, position1x + 1, position1y, position2x + 1, position2y, count + 1)
            a2 =dfs_search(board, False, position1x, position1y + 1, position2x, position2y + 1, count + 1)

            if position1x+1<len(board) and position2x+1<len(board) and board[position1x+1][position1y] == 0 and board[position2x+1][position2y] == 0:
                # 회전 아래
                a3=dfs_search(board, True, position1x, position1y, position2x + 1, position2y - 1, count + 1)

                # p1 p2바꾸기
                a4 = dfs_search(board, True, position2x, position2y, position1x + 1, position1y + 1, count + 1)

        else:
            a1 = dfs_search(board, False, position1x + 1, position1y, position2x + 1, position2y, count + 1)
            a2 = dfs_search(board, False, position1x, position1y + 1, position2x, position2y + 1, count + 1)
            if position1y+1<len(board) and position2y+1<len(board) and board[position1x][position1y+1] == 0 and board[position2x][position2y+1] == 0:
                # 회전 오른
                a3 = dfs_search(board, True, position1x, position1y, position2x - 1, position2y + 1, count + 1)
                # p1 p2바꾸기
                a4 = dfs_search(board, True, position2x, position2y, position1x + 1, position1y + 1, count + 1)

    return min(a1,a2,a3,a4)

"""
(0, 0)(0, 1) -> (0, 0)(1, 0) o
그대로 but 아래로 돌림
(0, 0)(0, 1) -> (1, 1)(1, 0) o
늘어남
(1, 0)(1, 1) -> (0, 1)(1, 1) x
그대로 but 위로돌림
위로 돌림 and 왼쪽으로 돌리는거 안됌
무조건 아래 아니면 오른쪽돌리기
(0, 0)(0, 1) -> (0, 0)(1, 0)x
"""
# go_down
board=[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

board=[[0, 0, 1, 1, 1],
       [0, 0, 1, 1, 0],
       [0, 1, 0, 1, 1],
       [0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0]]
print(dfs_search(board,False,0,0,0,1,0))
