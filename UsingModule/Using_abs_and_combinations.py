from itertools import combinations

def find_closest(house_position, last_chicken):
    min_distacne = 9e10
    for chic in last_chicken:
        min_distacne = min(min_distacne, abs(chic[0] - house_position[0])+abs(house_position[1] - chic[1]))
    return min_distacne
n,m=5,2
map=[[0,2,0,1,0],[1,0,1,0,0],[0,0,0,0,0],[2,0,0,1,1],[2,2,0,1,2]]

chicken=[]
house=[]

for i in range(len(map)):
    for j in range(len(map)):
        if map[i][j]==1:
            house.append((i,j))

        if map[i][j] == 2:
            chicken.append((i, j))



result=list(combinations(chicken,m))

min_chic_distance=10e9
for chic_case in result:
    temp_distacne=0
    for home in house:
        temp_distacne+=find_closest(home, chic_case)

    min_chic_distance=min(min_chic_distance,temp_distacne)

print(min_chic_distance)