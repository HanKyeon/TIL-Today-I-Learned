'''
열혈강호 3

n명의 직원, m명의 일. 번호가 1~n 1~m
각 직원은 한 개의 일만 가능. 각 일을 담당하는 사람은 1명.
단, n명 중 k명은 최대 2개의 일 가능.
m개 일 중 최대 몇개 가능?

입력
n, m 제시.
n개 줄 갯수 할 수 있는 일들

출력
최대 할 수 있는 일의 갯수.
'''
import sys
input = sys.stdin.readline

def matching(idx):
    for i in g[idx]:
        if v[i]:
            continue
        v[i] = 1
        if not connect[i] or matching(connect[i]):
            connect[i] = idx
            return True
    return False

n, m, k = map(int, input().rstrip().split())
g = [[]]
for _ in range(n):
    s = list(map(int, input().rstrip().split()))
    s.pop(0)
    g.append(s)
ans = 0
connect = [0]*(m+1)
for i in range(1, n+1):
    v = [0]*(m+1)
    if matching(i):
        ans += 1
cnt = 0
for i in range(1, n+1):
    if len(g[i]) < 2:
        continue
    v = [0]*(m+1)
    if matching(i):
        cnt += 1
    if cnt == k:
        break
print(ans+cnt)

'''
# 빠른 코드

import sys
from collections import deque
read = sys.stdin.readline

n, m, k = map(int, read().split())
edges = [list(map(lambda x: int(x) - 1, read().split()[1:])) for _ in range(n)] * 2

inf = 2000
dist = [inf] * (n * 2)
match_v = set()
match_u = [-1] * m


def bfs(vert):
    q = deque()
    ret = False
    for v in vert:
        if v not in match_v:
            q.append(v)
            dist[v] = 0
        else:
            dist[v] = inf
    min_dist = inf
    while q:
        v1 = q.popleft()
        d1 = dist[v1]
        if d1 >= min_dist:
            break
        for u in edges[v1]:
            v2 = match_u[u]
            if v2 == -1:
                min_dist = d1 + 1
                ret = True
            elif dist[v2] == inf:
                q.append(v2)
                dist[v2] = d1 + 1
    return ret


def dfs(v):
    d = dist[v]
    for u in edges[v]:
        v2 = match_u[u]
        if v2 == -1:
            match_u[u] = v
            return True
        elif dist[v2] == d + 1:
            if dfs(v2):
                match_u[u] = v
                return True
    dist[v] = inf
    return False


count = 0

while bfs(range(n)):
    for v in range(n):
        if dist[v] == 0:
            if dfs(v):
                match_v.add(v)
                count += 1

while bfs(range(2 * n)):
    for v in range(2 * n):
        if dist[v] == 0:
            if dfs(v):
                match_v.add(v)
                count += 1
                k -= 1
                if k == 0:
                    break
    if k == 0:
        break

print(count)
'''

'''
# 빠른 코드 2
import sys
input = sys.stdin.readline

def dfs(visited, i):
    visited[i] = True
    for v in graph[i]:
        if R[v] == -1:
            R[v] = i
            return True
    for v in graph[i]:
        if not visited[R[v]] and R[v] != i and dfs(visited, R[v]):
            R[v] = i
            return True
    return False


N, M, K = map(int, input().split())
graph = []
R = [-1] * M
ans = 0

for i in range(N):
    _, *want = list(map(int, input().split()))
    graph.append([v - 1 for v in want])

for i in range(N):
    if dfs([False] * N, i): ans += 1
    if ans == M: break

if K and ans != M:
    for i in range(N):
        if len(graph[i]) >= 2 and K and dfs([False] * N, i): ans += 1; K -= 1
        if ans == M: break

print(ans)
'''