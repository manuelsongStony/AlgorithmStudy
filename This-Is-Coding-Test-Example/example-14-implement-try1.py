#can not solved
import copy


def get_max_index(distance):
    max_distance = 0
    index = 0
    for i in range(len(distance)):

        if distance[i] >= max_distance:
            index = i
            max_distance = distance[i]
    return index


n,weak,dist=12,[1, 5, 6, 10],[1, 2, 3, 4]
#n,weak,dist=12,[1, 3, 4, 9, 10],[3, 5, 7]
n,weak,dist=15,[1, 3, 4, 9, 10],[3, 5, 7]
#제일 긴거리를 떄버리는 방식으로

distance =  []

for i in range(len(weak)-1):
    distance.append(weak[i+1]-weak[i])

distance.append(n-weak[-1]+weak[0])


print(distance)
index=get_max_index(distance)

copy_distance=copy.deepcopy(distance)
copy_distance.pop(index)

count=1
if sum(copy_distance)<dist[-1]:
    print(count)
else:
    count+=1
    index = get_max_index(copy_distance)
    copy_distance.pop(index)





