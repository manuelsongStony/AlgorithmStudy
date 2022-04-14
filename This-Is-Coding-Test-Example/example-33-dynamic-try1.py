#n=7
#array=[[],[3,10],[5,20],[1,10],[1,20],[2,15],[4,40],[2,200]]

n=10
array=[[],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10]]

last=7
largest_money=0

for i in range(1,n+1):
    #find max of array[x][1] that i>array[x][0]

    tempMax=0
    alpha=0
    if array[i][0]+i-1<=n:
        alpha=array[i][1]
        tempMax=array[i][1]
    else:
        array[i][0]=0

    for j in range (1,i):
        if array[j][0]<i:
            tempMax=max(tempMax,array[j][1]+alpha)

    array[i][1]=tempMax


print(array[n][0])
print(array[n][1])

