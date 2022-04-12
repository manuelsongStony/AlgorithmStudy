#다이나믹은 맨마지막꺼부터 생각  ->점화식 짜기
n,m=3,4

array=[[1,3,3,2],[2,1,4,1],[0,6,4,7]]



#n=n-1
for col in range(1,m):
    for row in range(n):
        if row==0:
            array[row][col]=array[row][col]+max(0,array[row][col-1],array[row+1][col-1])
        elif row==(n-1):
            array[row][col]=array[row][col]+max(array[row - 1][col-1], array[row][col-1], 0)
        else:
            array[row][col]=array[row][col]+max(array[row-1][col-1],array[row][col-1],array[row+1][col-1])


result=0
for i in range(n):
    result=max(result,array[i][m-1])

print(result)