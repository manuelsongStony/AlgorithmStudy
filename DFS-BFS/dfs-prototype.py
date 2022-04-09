def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


"""
my version
def dfs(graph, start, visited):

    if visited[start]==False:
        visited[start]=True
        print(start,end=' ')
        for i in graph[start]:
            dfs(graph,i,visited)
"""



visited= [False]*9
graph = [[],
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]
         ]

dfs(graph, 1, visited)