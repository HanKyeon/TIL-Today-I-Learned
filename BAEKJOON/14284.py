'''
간선 이어가기 2

정점 n개 0개 간선으로 이뤄진 무방향 그래프. m개의 가중치 간선 정보가 있는 간선 리스트 제시. 간선을 하나씩 추가 할 것.
특정 정점 s와 t가 연결되는 시점에 간선 추가를 멈출 것. s와 t가 연결되는 시점의 간선 가중치의 합이 최소가 되게 추가하는 간선의 순서를 조정 할 때, 그 최솟값을 구하시오.

입력
정점 갯수 n, 간선 수 m
m개 줄 a, b, c 제시.
s, t 제시.

출력
s와 t가 연결되는 시점의 간선 가중치 합의 최솟값
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dij():
    global n, s, t
    dst = [int(10e9)]*(n+1)
    dst[s] = 0
    heap = [(0, s)]
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        if nod == t:
            return cost
        for co, nnod in g[nod]:
            if dst[nnod] > cost+co:
                dst[nnod] = cost+co
                heappush(heap, (cost+co, nnod))

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
    g[b].append((c, a))
s, t = map(int, input().rstrip().split())

print(dij())



















