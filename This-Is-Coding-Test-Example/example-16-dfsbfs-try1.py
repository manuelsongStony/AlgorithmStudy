import copy
n, m = 7, 7
map = [[2, 0, 0, 0, 1, 1, 0],
         [0, 0, 1, 0, 1, 2, 0],
         [0, 1, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0]]

max_safe_area = 0

virus_position=[]
zero_position=[]

def count_zero(array):
    counter=0
    for i in range(n):
        for j in range(m):
            if array[i][j]==0:
                counter+=1
    return counter


def check_virus(array):
    for i in range(n):
        for j in range(m):
            if array[i][j]==2:
                virus_position.append((i,j))
            elif array[i][j]==0:
                zero_position.append((i,j))

def dfs_spread(array, x, y):
    array[x][y] = 2

    if x + 1 < n:
        if array[x + 1][y] == 0:
            dfs_spread(array, x + 1, y)

    if x - 1 > -1:
        if array[x - 1][y] == 0:
            dfs_spread(array, x - 1, y)

    if y + 1 < m:
        if array[x][y + 1] == 0:
            dfs_spread(array, x, y + 1)

    if y - 1 > -1:
        if array[x][y - 1] == 0:
            dfs_spread(array, x, y - 1)






set_combination=[]
def find_combination(zero_count):

    for i in range(zero_count):
        for j in range(i+1,zero_count):
            for k in range(j+1, zero_count):
                temp=[]
                temp.append(zero_position[i])
                temp.append(zero_position[j])
                temp.append(zero_position[k])
                set_combination.append(temp)







check_virus(map)

copy_map=copy.deepcopy(map)

zero_count=count_zero(map)

find_combination(zero_count)




result=0

print("length is" +str(len(set_combination)) )
for i in set_combination:
    copy_map = copy.deepcopy(map)

    copy_map[i[0][0]][i[0][1]]=1
    copy_map[i[1][0]][i[1][1]] = 1
    copy_map[i[2][0]][i[2][1]] = 1

    for position in virus_position:
        dfs_spread(copy_map, position[0], position[1])

    result=max(result,count_zero(copy_map))


print(result)