from collections import deque
n, k = 3, 3
s, x, y = 2, 3, 2

"""
n, k = 3, 3
s, x, y = 1, 2, 2
"""
map=[[1,0,2],[0,0,0],[3,0,0]]


k_array=[deque([]) for _ in range(k+1)]
for i in range(len(map)):
    for j in range(len(map)):
        if map[i][j]!=0:
            k_array[map[i][j]].append((i,j))


for _ in range(0,s):
    for virus in range(1,k+1):
        for _ in range(len(k_array[virus])):
            row,col=k_array[virus].popleft()

            if row+1<n and map[row+1][col]==0:
                map[row + 1][col]=virus
                k_array[virus].append((row+1,col))

            if row-1>=0 and map[row-1][col]==0:
                map[row - 1][col]=virus
                k_array[virus].append((row-1,col))

            if col + 1 < n and map[row][col+1] == 0:
                map[row][col+1] = virus
                k_array[virus].append((row, col+1))

            if col - 1 >= 0 and map[row][col-1] == 0:
                map[row][col-1] = virus
                k_array[virus].append((row, col-1))



#print(k_array)
#print(k_array[1].popleft())
print(map)
print(map[x-1][y-1])
