'''
백도어

분기점 n개.
입력으로 각 분기점을 지나칠 수 있는지 여부, 각 분기점에서 다른 분기점으로 가는데 걸리는 시간 제시. 현 위치에서 넥서스까지 갈 수 있는 최소 시간 구하기.

입력
n, m 제시. 노드 수, 간선 수
분기점 n-1은 넥서스라 보여도 갈 수 있다. 다른 보이는 분기점은 갈 수 없다.
m개 줄 걸쳐 a, b, t가 공백 구분 제시. a와 b를 지나는데 t 시간 걸린다. 연결은 양방향, 한 분기에서 다른 분기로 가는 간선은 최대 1개

출력
안들키고 가는데 걸리는 최소 시간. 갈 수 없다면 -1 출력.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dij():
    global n
    dst = [int(10e9)]*n
    dst[0] = 0
    heap = [(0, 0)]
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        if nod == n-1:
            return cost
        for co, nnod in g[nod]:
            if dst[nnod] > cost+co:
                dst[nnod] = cost+co
                heappush(heap, (cost+co, nnod))
    return -1

n, m = map(int, input().rstrip().split())
v = list(map(int, input().rstrip().split()))
v.pop()
v.append(0)
g = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    if v[a] or v[b]:
        continue
    g[a].append((c, b))
    g[b].append((c, a))
print(dij())



