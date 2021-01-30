from collections import deque
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    temp = []
    while q:
        v = q.popleft()
        temp.append(v)
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return temp

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

print(bfs(graph, 1, visited))