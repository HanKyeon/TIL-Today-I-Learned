'''
횡단보도

n개 지역, 몇개 횡단보도.
파란 불이 들어오는 순서를 알고 있다. 주기는 총 m분이며, 1분마다 신호가 바뀐다.
주기가 i라면, i, m+i, 2m+i 마다 켜진다. 다른 모든 횡단보도는 빨간 불이다. 한 주기동안 같은 횡단보도에 파란불 여러번 들어올 수 있음.
횡단보도 이동 시간 1분. 신호가 s~e 시간에 들어온다면 반드시 s~e-1 시간에 건너야 한다.
횡단보도와 신호 정보 제시. 0분에서 시작해서 1번 지역에서 n번 지역까지 가는 최소 시간을 구해라.

입력
지역 수 n, 주기 m 공백 제시.
m개 줄, 1+i 번째 줄에는 i,M+i. 2M+i ... 분에 시작해서 1분동안 파란불이 들어오는 횡단보도의 두 끝점 a, b 제시.

출력
1번 지역에서 n번 지역까지 가는데 최소 시간을 분 단위로 출력.
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dij():
    global n, m
    dst = [int(1e12)]*(n+1)
    dst[1] = 0
    heap = [(0, 1)]
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        if nod == n:
            return cost
        zg = cost%m
        for i, nnod in g[nod]:
            nt = cost+i-zg+1 if i-zg >=0 else cost+i-zg+m+1
            if dst[nnod] > nt:
                dst[nnod] = nt
                heappush(heap, (nt, nnod))

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().rstrip().split())
    g[a].append((i, b))
    g[b].append((i, a))
print(dij())

'''
# 빠른 코드

import os, io
from heapq import heappush, heappop
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
inf = float('inf')
djk = [0, 0] + [inf] * (N - 1)
heap = [(0, 1)]

for i in range(1, M + 1):
	a, b = map(int, input().split())
	graph[a].append((b, i))
	graph[b].append((a, i))

while 1:
	cur = heappop(heap)[1]
	if cur == N: break
	for v, c in graph[cur]:
		c = (c - djk[cur]) % M
		if c == 0: c = M
		if djk[cur] + c < djk[v]:
			djk[v] = djk[cur] + c
			heappush(heap, (djk[v], v))

print(djk[-1])

'''








