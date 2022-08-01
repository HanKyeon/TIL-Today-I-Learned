'''
DFS와 BFS

노드 n개, m개 간선, 시작 노드v
DFS로 순회한 순서
BFS로 순회한 순서
출력해라.
'''
from collections import deque

n, m, v = map(int, input().split())

dt = [[] for _ in range(n+1)]
visited = [0] * (n + 1)
dfs_list = []

for i in range(m) :
    a, b = map(int, input().split())
    dt[a].append(b)
    dt[b].append(a)

for d in dt :
    d.sort()

def dfs(x) :
    dfs_list.append(x)
    visited[x] = 1
    for i in dt[x] :
        if visited[i] != 1 :
            dfs(i)
    return dfs_list

def bfs(y) :
    q = deque()
    q.append(y)
    ql =[]
    qcheck = [0] * (n + 1)
    qcheck[y] = 1

    while q :
        ny = q.popleft()
        ql.append(ny)
        for i in dt[ny] :
            if qcheck[i] != 1 :
                qcheck[i] = 1
                q.append(i)
    return ql

print(' '.join(map(str, dfs(v))))
print(' '.join(map(str, bfs(v))))

