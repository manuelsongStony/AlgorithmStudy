import copy

n,k=2,3
array=[[2,14,1],[3,3,3],[15,1,1],[4,2,2],[7,5,2],[14,2,2]]


#answer=18+15#33
answer=0

for _ in range(n):
    max_worriers=0
    max_index=0
    for i in range(len(array)):
        multi=min(k,array[i][2])
        if max_worriers < (array[i][0]+(multi*array[i][1])):
            max_worriers=array[i][0]+(multi*array[i][1])
            max_index=i



    answer+=max_worriers
    k-=array[max_index][2]
    array.pop(max_index)

print(answer)