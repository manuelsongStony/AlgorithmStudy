n=int(input())
directionList=list(input().split())
position=[1,1]
for d in directionList:
    if d =="L":
        if position[1] > 1:
            position[1] -= 1
    elif d == "R":
        if position[1]<n:
            position[1]+=1
    elif d == "U":
        if position[0]>1:
            position[0]-=1
    elif d == "D":
        if position[0]<n:
            position[0]+=1

print(position[0],position[1])