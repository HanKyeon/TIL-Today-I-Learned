'''
네트워크 연결

네트워크 연결 할 것이다.
자료를 공유하기 위해 모든 컴이 연결되어 잇어야 한다. 경로가 존재해야 한다.
최소 비용으로 네트워크를 연결하는데 필요한 최소 비용 출력

입력
노드 n
간선 m
m개 줄 간선 정보. a, b, c

출력
최소비용
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 해서
    global n
    if x < y:
        parent[y] = x
        nodc[x] += nodc[y]
        if nodc[x] == n:
            return True
    else:
        parent[x] = y
        nodc[y] += nodc[x]
        if nodc[y] == n:
            return True
    return False

def mst():
    ret = 0
    while heap:
        cost, nod1, nod2 = heappop(heap)
        nod1, nod2 = find(nod1), find(nod2)
        if nod1 == nod2:
            continue
        ret += cost
        if union(nod1, nod2):
            return ret

n, m = int(input()), int(input())
heap = []
parent = list(range(n+1))
nodc = [1]*(n+1)
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    heappush(heap, (c, a, b))

ans = mst()
print(ans)







