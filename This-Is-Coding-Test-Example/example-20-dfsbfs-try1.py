import copy
from itertools import combinations


def check_caught(map,position):
    #check left
    flag=True
    for i in range(position[1]-1,-1,-1):
        if map[position[0]][i]=='T' and flag:
            return False
        elif map[position[0]][i]=='O' :
            flag=False
    # check right
    flag = True
    for i in range(position[1] +1, len(map)):
        if map[position[0]][i] == 'T' and flag:
            return False
        elif map[position[0]][i] == 'O':
            flag = False

    # check up
    flag = True
    for i in range(position[0] - 1, -1, -1):
        if map[i][position[1]] == 'T' and flag:
            return False
        elif map[i][position[1]] == 'O':
            flag = False
    # check down
    flag = True
    for i in range(position[0] + 1, len(map)):
        if map[i][position[1]] == 'T' and flag:
            return False
        elif map[i][position[1]] == 'O':
            flag = False

    return True



n=5
map=[['X','S','X','X','T'],['T','X','S','X','X'],['X','X','X','X','X'],['X','T','X','X','X'],['X','X','T','X','X']]

"""
n=4
map=[['S','S','S','T'],['X','X','X','X'],['X','X','X','X'],['T','T','T','X']]
"""
temp=[]
set_S=[]
for i in range(n):
    for j in range(n):
        if map[i][j]=='X':
            temp.append((i,j))
        if map[i][j]=='S':
            set_S.append((i,j))

comb=list(combinations(temp,3))

answer=''
#comb=[((0,3),(1,1),(2,2))]
for ele in comb:
    temp_map=copy.deepcopy(map)
    for i in range(3):
        temp_map[ele[i][0]][ele[i][1]]='O'

    answer_flag=True
    for j in set_S:
        if not check_caught(temp_map,j):
            answer_flag = False
            break

    if answer_flag==True:
        answer='Yes'
        break

if answer=='':
    answer='No'

print(answer)



