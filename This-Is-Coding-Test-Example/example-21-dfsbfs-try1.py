"""
n,l,r=4,10,50
p_array=[[10,100,20,90],
       [80,100,60,70],
       [70,20,30,40],
       [50,20,100,10]]
"""

n,l,r=3,5,10
p_array=[[10,15,20],
       [20,30,25],
       [40,22,10]]

answer=0
#위아래 좌우 dfs 해서 숫자 한개로 만들기 숫자별로

p_map=[[0]*n for _ in range(4)]
glboal_n=1
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def have_adjacent(arry,x,y):

    for i in range(4):
        t_x=x + dx[i]
        t_y=y + dy[i]
        if t_x < 0 or t_y < 0 or t_x>= n or t_y >= n:
            continue

        if l <= abs(arry[x][y] - arry[t_x][t_y]) and r >= abs(arry[x][y] - arry[t_x][t_y]):
            return True

    return False

#print(have_adjacent(p_array,2,1))


global_denominator=0
global_numerator=0

def dfs_people(arry,map_arry,x,y,temp_array):

    if map_arry[x][y]!=0:
        return

    map_arry[x][y]=glboal_n
    temp_array.append((x,y))

    for i in range(4):
        t_x = x + dx[i]
        t_y = y + dy[i]

        if t_x < 0 or t_y < 0 or t_x>= n or t_y >= n:
            continue
        if l <= abs(arry[x][y] - arry[t_x][t_y]) and r >= abs(arry[x][y] - arry[t_x][t_y]):
            dfs_people(arry, map_arry, t_x, t_y,temp_array)




flag=True
while(flag):
    flag=False
    p_map = [[0] * n for _ in range(4)]
    glboal_array=[]

    for i in range(n):
        for j in range(n):
            if p_map[i][j]==0:
                if have_adjacent(p_array,i,j):
                    temp_array=[]
                    dfs_people(p_array,p_map,i,j,temp_array)

                    glboal_array.append(temp_array)
                    glboal_n+=1

                    flag=True

    for ele in glboal_array:
        denominator=0
        numerator=len(ele)
        for k in ele:
            denominator+=p_array[k[0]][k[1]]

        average_people=denominator//numerator

        for k in ele:
            p_array[k[0]][k[1]]=average_people

    if flag:
        answer+=1


print(answer)