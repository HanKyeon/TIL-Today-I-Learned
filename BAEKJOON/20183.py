'''
골목 대장 호석 - 효율성 2

n개 마을과 m개 골목.
교차로는 1부터 n까지. 골목은 양방향, 각 교차로 간 최대 1개.
간선마다 갖아 많이 낸 돈이 적은 경로이며, 가진 돈으로 갈 수 있어야 한다.
한 골목에서 내야하는 최대 요금의 최솟값. 가진 돈으로 절대 못가면 -1 출력.

입력
n, m, a, b, c 제시. 교차로 골목 시작점 도착점 돈
m개 줄 교차로 a, b, c 제시.

출력
c원 이하로 가는 경로 중 지나가는 골목 요금의 최댓값의 최솟값. 갈 수 없다면 -1.
'''
import sys
from heapq import heappop, heappush
import math
input = sys.stdin.readline
sys.stdin = open("파일", "r", encoding="utf-8") # 이 친구는 위의 input = sys.stdin.readline과 함께 못씀.
inf = math.inf

def dij(maxCost):
    global n, s, e, mny
    dst = [inf]*(n+1)
    dst[s] = 0
    heap = [(0, s)]
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        if cost > mny:
            return -1
        if nod == e:
            return maxCost
        for co, nnod in g[nod]:
            if co > maxCost:
                continue
            if cost+co < dst[nnod]:
                dst[nnod] = cost+co
                heappush(heap, (cost+co, nnod))
    return -1

n, m, s, e, mny = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
maxc = 0
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    if c > maxc:
        maxc = c
    g[a].append((c, b))
    g[b].append((c, a))

sta, end = 0, maxc
ans = inf
while sta <= end:
    mid = (sta+end) // 2
    a = dij(mid)
    if 0<=a:
        if a < ans:
            ans = a
        end = mid-1
        continue
    sta = mid+1
if ans == inf:
    ans = -1
print(ans)


'''
# 시간 초과

import sys
from heapq import heappop, heappush
import math
input = sys.stdin.readline
inf = math.inf

def dij(maxCost):
    global n, m, s, e, mny
    dst = [inf]*(n+1)
    dst[s] = 0
    heap = [(0, mny, s)] # 요금 최댓값, 전체 코스트, 현재 노드
    while heap:
        c, cost, nod = heappop(heap)
        if dst[nod] < c:
            continue
        if nod == e:
            return c
        for co, nnod in g[nod]:
            if cost < co:
                continue
            if co > c and dst[nnod] >= co:
                dst[nnod] = co
                heappush(heap, (co, cost-co, nnod))
            elif co <= c and dst[nod] >= c:
                dst[nnod] = c
                heappush(heap, (c, cost-co, nnod))
    return -1

n, m, s, e, mny = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
    g[b].append((c, a))
print(dij())
'''

'''
6 6 1 6 5
1 2 2
1 3 1
3 4 1
2 5 2
4 5 1
5 6 2
'''










