'''
전력난

가로등 중 일부를 소등 할 것. 도시는 불이 켜진 길만 왕래 가능. 길의 길이만큼 돈이 나간다.

입력
집의 수 n 길의 수 m 제시.
m개 줄 a, b, c 제시.
마지막 입력은 0 0이다.

출력
테케마다 절약 가능한 최대 비용 출력
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(200001)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

while True:
    n, m = map(int, input().rstrip().split())
    if not n:
        break
    egs = []
    parent = list(range(n+1))
    sr = 0
    for _ in range(m):
        a, b, c = map(int, input().rstrip().split())
        sr += c
        heappush(egs, (c, a, b))
    ms, mc = 0, 0
    while egs:
        c, a, b = heappop(egs)
        ra, rb = find(a), find(b)
        if ra == rb:
            continue
        ms += c
        mc += 1
        union(ra, rb)
        if mc == n-1:
            break
    print(sr-ms)



'''
import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def solution(n, m):
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i
    edges = []
    all_cost = 0
    for _ in range(m):
        a, b, cost = map(int, input().split())
        all_cost += cost
        edges.append((a, b, cost))
    edges.sort(key=lambda x: x[2])  # sort by cost
    mst_cost = 0
    mst_count = 0
    for edge in edges:
        a, b, cost = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            mst_cost += cost
            mst_count += 1
            if mst_count == n - 1:
                break
    return all_cost - mst_cost

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    print(solution(n, m))
'''








