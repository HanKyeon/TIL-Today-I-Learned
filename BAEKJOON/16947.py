'''
서울 지하철 2호선

지하철 2호선 51개역, 역과 역 사이 연결 구간 51개. 정점 51개, 간선 51개 그래프.

입력
역의 갯수 n 제시.
n개 줄 역과 역을 연결하는 구간의 정보 제시.

출력
n개 정수 출력.
1번 역과 순환선 사이의 거리, 2번 역과 순환선 사이의 거리. 이미 순환선이라면 0
'''
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(3333)

# 사이클 찾기
def dfs(nod):
    if cyc:
        return
    for nnod in g[nod]:
        if v[nnod]: # 방문된 곳을 찾은건 사이클이다.
            cyc.append(nnod)
            while stk and stk[-1] != nnod:
                cyc.append(stk.pop())
            return
        else:
            g[nnod].remove(nod)
            v[nnod] = 1
            stk.append(nnod)
            dfs(nnod)
            if cyc:
                return
            stk.pop()

def bfs():
    global n
    dst = [3333] * (n+1)
    q = deque()
    while cyc:
        nod = cyc.pop()
        q.append(nod)
        dst[nod] = 0
    while q:
        nod = q.popleft()
        for nnod in bg[nod]:
            if dst[nnod] != 3333:
                continue
            dst[nnod] = dst[nod]+1
            q.append(nnod)
    return dst

# 입력
n = int(input())
g = [set() for _ in range(n+1)]
bg = [set() for _ in range(n+1)]
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    g[a].add(b)
    g[b].add(a)
    bg[a].add(b)
    bg[b].add(a)

# 사이클 찾기
stk = []
v = [0]*(n+1)
cyc = []
v[1] = 1
dfs(1)

ans = bfs()
ans.pop(0)
print(*ans)

'''
똑똑이의 풀이

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(cv,pv):
    if cache[cv] == 1: return cv
    cache[cv] = 1

    for nv in grid[cv]:
        if nv == pv: continue  # 양방향 그래프기 때문
        result = dfs(nv,cv)
        if result >= 0:
            cache[cv] = 2
            return result if cv != result else -1

    return -1

def bfs():
    q = []
    for i in range(n):
        if cache[i] == 2: 
            q.append(i)
            dist[i] = 0

    while q:
        tmp = []

        for cv in q:
            for nv in grid[cv]:
                if dist[nv] != -1: continue
                dist[nv] = dist[cv] + 1
                tmp.append(nv)

        q = tmp

n = int(input())
grid = [[] for _ in range(n)]
cache = [0]*n
dist = [-1]*n

for _ in range(n):
    a,b = map(int, input().split())
    grid[a-1].append(b-1)
    grid[b-1].append(a-1)

dfs(0,-1)
bfs()
print(*dist)
'''
