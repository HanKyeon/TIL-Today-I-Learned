'''
학교 탐방하기

오르막길 내리막길
피로도 계산 예정. 입구는 0번
모든 건물을 방문하는데 필요한 최소한의 길 선택. 해당 길을 통해서만 건물들을 소개 할 것.
오르막길 k번 오르면 피로도는 k**2
최초 조사된 길을 기준으로 계산. 즉, 올라갔다 내려갔다 뭐 그런거 없이 오르막길은 오르막이고 내리막은 내리막이다. 되돌아오는 길 피로는 없다.

최악의 경로와 최선의 경로 간 피로도 차이 계산.

입력
n, m 제시
m개 줄 a, b, c 제시. c는 오르막0 내리막1로 구성.
같은 경로 상에 2개 이상의 도로가 주어지는 경우는 없으며, 입구는 항상 1번 건물과 연결되어 있다. 입구와 1번 도로 간의 연결 관계는 항상 2번째 줄에 제시.
입구는 항상 1번과 연결 된 상태. 입구 1번 관계는 첫빠따로 제시.

출력
최악의 경로 피로도 - 최선의 경로 피로도
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find해서
    if x < y:
        parent[y] = x
        nodc[x] += nodc[y]
        return nodc[x]
    else:
        parent[x] = y
        nodc[y] += nodc[x]
        return nodc[y]

def lego(li):
    ret= 0
    while li:
        c, a, b = heappop(li)
        ra, rb = find(a), find(b)
        if ra == rb:
            continue
        ret += c
        if union(ra, rb) == n+1:
            return ret

n, m = map(int, input().rstrip().split())
mheap, Mheap = [], []
for _ in range(m+1):
    a, b, c = map(int, input().rstrip().split())
    heappush(Mheap, (c, a, b))
    if c:
        c = 0
    else:
        c = 1
    heappush(mheap, (c, a, b))

parent = list(range(n+1))
nodc = [1]*(n+1)
ans1 = lego(mheap)
parent = list(range(n+1))
nodc = [1]*(n+1)
ans2 = n-lego(Mheap)

print(ans2**2 - ans1**2)

'''
# 빠른 코드

import sys; sys.stdin.readline

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    ru = find(u)
    rv = find(v)
    if ru == rv:
        return False
    if ru < rv:
        parent[rv] = ru
    else:
        parent[ru] = rv
    return True

N, M = map(int, input().split())
A, B, C = map(int, input().split())
if C:
    worst = best = 0
else:
    worst = best = 1
up = []
down = []
for _ in range(M):
    A, B, C = map(int, input().split())
    if C:
        down.append((A - 1, B - 1))
    else:
        up.append((A - 1, B - 1))
parent = list(range(N))
ct = 0
flag = False
for u, v in down:
    if union(u, v):
        ct += 1
        if ct == N:
            flag = True
            break
if not flag:
    for u, v in up:
        if union(u, v):
            best += 1
            ct += 1
            if ct == N:
                break
parent = list(range(N))
ct = 0
flag = False
for u, v in up:
    if union(u, v):
        worst += 1
        ct += 1
        if ct == N:
            flag = True
            break
if not flag:
    for u, v in down:
        if union(u, v):
            ct += 1
            if ct == N:
                break
print(worst ** 2 - best ** 2)
'''