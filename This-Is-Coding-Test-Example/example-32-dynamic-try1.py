#다이나믹은 맨마지막꺼부터 생각  ->점화식 짜기
n=5

array=[[0],[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]




#n=n-1
for row in range(1,n+1):
    for col in range(row):
        if col==0:
            array[row][0]=array[row][0]+array[row-1][0]
        elif col==(row-1):
            array[row][col]=array[row][col]+array[row-1][col-1]
        else:
            array[row][col]=array[row][col]+max(array[row-1][col-1],array[row-1][col])


result=0
for i in range(n):
    result=max(result,array[n][i])

print(result)