from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)

for i in range(m):
    index, value = map(int, input().split())
    graph[index].append(value)


def bfs(graph, start, depth):
    q = deque([(start, 0)])
    array = []
    while q:
        ele, distance = q.popleft()
        if distance == depth:
            array.append(ele)

        visited[ele] = True

        for i in graph[ele]:
            if visited[i] == False:
                q.append((i, distance + 1))
                visited[i] = True

    array.sort()
    if array:
        for i in array:
            print(i)
    else:
        print(-1)


bfs(graph, x, k)
