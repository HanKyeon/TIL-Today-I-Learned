'''
좀비

N개 도시 M개 도로.
k개 도시 좀비로 인해 점령.
1번 도시에서 n번 도시로 이동 예정.
각 도시를 이동 할 때마다 1박, 1박마다 숙박비 지불, 좀비 상태면 숙박 불가능.
좀비에게 점령당한 도시로부터 S번 이하 이동으로 이동 할 수 있는 도시는 위험도시로 정의되며, 그 외의 도시는 안전 도시. 안전도시라면 숙박비가 p이고, 위험 도시라면 숙박비 q원.
1부터 n까지 이동하는데 드는 최단 비용 구하기.

입력
n, m, k, s 제시. 도시 수, 길 수, 좀비도시 수, 위험도시 범위
숙박비 p, q. 안전도시p 위험도시q
k개 줄 걸쳐 점령당한 도시 제시.
m개줄 걸쳐 각 도시를 연결하느 ㄴ도로 정보 제시. 양방향 이동 가능.

출력
최소비용 출력
'''
# 기념비적으로 내가 속도 1위함 하하
from collections import deque
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def bfs():
    dq = deque()
    while zc:
        dq.append((s, zc.pop()))
    while dq:
        cnt, ct = dq.popleft()
        if dp[ct] > cnt:
            continue
        for i in g[ct]:
            if cnt-1 and cnt-1 > dp[i]:
                dp[i] = cnt-1
                cst[i] = q
                dq.append((cnt-1,i))

def dij():
    dst = [int(10e9)]*(n+1)
    heap = [(0, 1)]
    dst[1] = 0
    while heap:
        cost, nod = heappop(heap)
        if nod == n:
            return dst[-1]-cst[-1]
        if dst[nod] < cost:
            continue
        for i in g[nod]:
            costco = cost+cst[i]
            if dst[i] > costco:
                dst[i] = costco
                heappush(heap, (costco, i))

n, m, k, s = map(int, input().rstrip().split())
s+=1
p, q = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
cst = [p]*(n+1)
dp = [0]*(n+1)
zc = []
for _ in range(k):
    zb = int(input())
    zc.append(zb)
    dp[zb] = s
    cst[zb] = int(10e9)
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    g[a].append(b)
    g[b].append(a)

bfs()
print(dij())

'''

def bfs():
    dq = deque()
    for i in zc:
        dq.append((s+1, i))
    while dq:
        cnt, ct = dq.popleft()
        if dp[ct] > cnt:
            continue
        for i in g[ct]:
            if dp[ct]-1 and dp[ct]-1 > dp[i]:
                dp[i] = dp[ct]-1
                cst[i] = q
                dq.append((dp[ct]-1,i))

def dij():
    dst = [int(10e9)]*(n+1)
    heap = [(0, 1)]
    dst[1] = 0
    while heap:
        cost, nod = heappop(heap)
        if nod == n-1:
            return dst[-1]-cst[-1]
        if dst[nod] < cost:
            continue
        for i in g[nod]:
            costco = cost+cst[i]
            if dst[i] > costco:
                dst[i] = costco
                heappush(heap, (costco, i))
    return dst[-1] - cst[-1]

n, m, k, s = map(int, input().rstrip().split())
p, q = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
cst = [p]*(n+1)
dp = [0]*(n+1)
zc = []
for _ in range(k):
    zb = int(input())
    zc.append(zb)
    dp[zb] = s+1
    cst[zb] = int(10e9)
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    g[a].append(b)
    g[b].append(a)

bfs()
print(dp)
print(cst)

print(dij())
'''







