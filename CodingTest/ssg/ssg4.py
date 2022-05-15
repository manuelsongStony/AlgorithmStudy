import copy

def drop_macron(board,new_state):
    new_board = copy.deepcopy(board)
    for i in range(5,-1,-1):
        if new_board[i][new_state[0]-1]==0:
            new_board[i][new_state[0]-1]=new_state[1]
            return new_board


def do_game(board,new_state):
    newboard=drop_macron(board,new_state)




macaron=[[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]]
#result=["000000","000000","000000","000000","000000","204004"]

#macaron=[[1,1],[1,2],[1,4],[2,1],[2,2],[2,3],[3,4],[3,1],[3,2],[3,3],[3,4],[4,4],[4,3],[5,4],[6,1]]
#result=["000000","000000","000000","000000","000000","404001"]

board=[[0]*6 for _ in range(6)]

for ele in macaron:
    board=drop_macron(board,ele)

    if ele[0]:



for x in board:
    print(x)