n,m=map(int,input().split())
graph=[]

for i in range(n):
    graph.append(list(map(int,input())))


count=0

def search_maze(x,y,past_value):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    elif graph[x][y] == 0:
        return False
    elif graph[x][y]==1 or graph[x][y]>1+past_value:
        graph[x][y]=1+past_value
        search_maze(x+1,y,1+past_value)
        search_maze(x, y+1, 1 + past_value)
        search_maze(x - 1, y, 1 + past_value)
        search_maze(x, y-1, 1 + past_value)


search_maze(0,0,0)
print(graph[n-1][m-1])


