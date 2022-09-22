'''
특정 거리의 도시 찾기

1번부터 n번까지 도시와 m개의 단 방향 도로. 모든 도리의 거리는 1.
특정한 도시 x로부터 출발하여 도달 할 수 있는 모든 도시 중에서 최단 거리가 정확히 k인 모든 도시들의 번호를 출력하는 프로그램 작성.
자기자신 거리0

입력
도시 갯수 n, 도로 갯수 m, 거리 정보 k, 출발 도시 번호 x 제시. 2이상 30만이하 1이상100만이하 1이상30만이하 1이상 n이하
m개 줄에 걸쳐 a, b 제시. a에서 b로 가는 단방향 도로가 존재한다는 의미. a와 b는 서로 다른 자연수.

출력
x로부터 출발하여 도달 할 수 있는 도시 중에서 최단 거리가 k인 모든 도시의 번호를 한 줄에 하나씩 오름차순 출력.
이 때 도달 할 수 있는 도시 중에서 최단 거리가 k인 도시가 하나도 없으면 -1 출력
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dij(sta):
    global k
    dst = [int(10e9)]*(n+1)
    dst[sta] = 0
    heap = [(0, sta)]
    while heap:
        sumc, nod = heappop(heap)
        for i in g[nod]:
            cost = sumc+1
            if dst[i] > cost:
                dst[i] = cost
                heappush(heap, (cost, i))
    ans = [i for i, v in enumerate(dst) if v==k]
    if not ans:
        print(-1)
        return
    for i in ans:
        print(i)

n, m, k, st = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    g[a].append(b)
dij(st)

'''
# 빠른 코드

import sys
from collections import deque
input = sys.stdin.readline
inf = sys.maxsize

n, m, k, x = map(int, input().split())
inlst = [[] for _ in range(n+1)]
for i in range(m):
	s, e = map(int, input().split())
	inlst[s].append(e)

lst = [inf for _ in range(n+1)]
lst[x] = 0
que = deque()
que.append(x)
while que:
	node = que.popleft()
	if lst[node] > k: continue
	for i in inlst[node]:
		if lst[i] == inf:
			lst[i] = lst[node] + 1
			que.append(i)
ans = []
for i in range(1, n+1):
	if lst[i] == k: ans.append(i)
if ans: print(*ans, sep='\n')
else: print(-1)
'''


