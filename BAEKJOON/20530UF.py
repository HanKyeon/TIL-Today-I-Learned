'''
양분

나무 T는 양분을 먹고 자란다.
정점 N과 N-1로 구성되어야 하지만 N개의 간선을 가지게 되었다.

N개 정점과 N개의 간선으로 이루어진 연결 그래프 T가 주어진다.
정점은 1번부터 N번까지 번호가 매겨져 있고, 간선도 1번부터 N번까지 번호가 매겨져 있다. 아래 쿼리를 수행하라.
쿼리
u v : u번 정점에서 v번 정점으로 가는 단순 경로의 수 출력

입력
N, Q 제시. 간선 갯수 N, 쿼리 갯수 Q
N개 줄 a, b 제시 간선.
Q개 줄 쿼리 제시.
'''
'''
간선 정보를 입력한 뒤 어느 한 지점에서 dfs해서 사이클을 찾는다.
사이클의 부모는 사이클에서 가장 작은 수로.
나머지 union 할 때 root가 사이클이라면 continue 하는걸로.

아래처럼 구성이 된다.
트리 - 사이클 - 트리
같은 트리 내 -> 1회
다른 트리-> 다른 트리 -> 2회
사이클을 set()로 만들어주고
사이클의 숫자 중에 있다면 
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # union 해서.
    if x in cyc:
        parent[y] = x
        return
    elif y in cyc:
        parent[x] = y
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def dfs(idx): # 사이클 찾는 dfs 함수
    for i in g[idx]:
        if v[i]:
            ret = {i}
            while stk[-1] != i:
                num = stk.pop()
                ret.add(num)
            return ret
        v[i] = 1
        g[i].remove(idx)
        stk.append(i)
        a = dfs(i)
        if a:
            return a
        if stk:
            stk.pop()
    return False

n, qst = map(int, input().rstrip().split())
parent = list(range(n+1))
g = [set() for _ in range(n+1)]
egs = []
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    g[a].add(b)
    g[b].add(a)
    egs.append((a, b))

stk = [1]
v = [0]*(n+1)
v[1] = 1
cyc = dfs(1)

for a, b in egs:
    if a in cyc and b in cyc:
        continue
    ra, rb = find(a), find(b)
    union(ra, rb)

for _ in range(qst):
    a, b = map(int, input().rstrip().split())
    if find(a) == find(b):
        print(1)
    else:
        print(2)
for i in range(1, n+1):
    if i in cyc:
        continue
    find(i)
print(cyc)
print(parent)

'''
# 짱 빠른 코드

import sys
input = lambda: map(int, sys.stdin.readline().split())
N, Q = input()
graph = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
for _ in range(N):
    a, b = input()
    degree[a] += 1
    degree[b] += 1
    graph[a].append(b)
    graph[b].append(a)

visited = [-1 for _ in range(N+1)]
q = [i for i,v in enumerate(degree) if v==1]
while len(q) > 0:
    nq = []
    for cur in q:
        for nxt in graph[cur]:
            if visited[nxt] == -1:
                visited[cur] = nxt
                degree[nxt] -= 1
                if degree[nxt] == 1:
                    nq.append(nxt)
    q = nq

def zp(x):
    if visited[x] == x: return x
    if visited[x] == -1:
        visited[x] = x
        return x
    visited[x] = zp(visited[x])
    return visited[x]

for i in range(1, N+1):
    zp(i)

ans = []
for _ in range(Q):
    u, v = input()
    ans.append("1" if visited[u]==visited[v] else "2")
print("\n".join(ans))
'''


'''
# 4 5 6 사이클
# 1 2 3 4 트리
# 5 7 8 9 10 트리
# 6 11 12 13 14 15 16 트리
16 1
1 3
2 3
3 4
4 5
5 6
6 4
5 7
7 8
7 9
7 10
6 11
6 12
11 13
11 14
12 15
12 16
1 2
'''







