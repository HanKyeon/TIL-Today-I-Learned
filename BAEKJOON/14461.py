'''
소가 길을 건너간 이유 7

목초지 n*n. 바깥으로 못나감. 상하좌우 이동 가능, 차 확인해야함. 길 건너는데 T초.
1,1 to n,n
길을 세 번 건널 때마다 목초지에 있는 풀을 먹어야 한다.
목초지마다 풀이 자란 정도가 달라서 풀을 먹는데 걸리는 시간도 다르다.

입력
n, t 제시.
n개 줄 풀 먹는 시간 제시.

출력
존의 집까지 걸리는 시간.
'''
import sys
from heapq import heappop, heappush
import math
input = sys.stdin.readline
inf = math.inf
mov = [(-1,0),(0,1),(1,0),(0,-1)]

def dij():
    global n, t
    dst[0][0][2] = 0
    heap = [(0, 0, 0, 2)]
    while heap:
        cost, h, w, pul = heappop(heap)
        if dst[h][w][pul] < cost:
            continue
        if h == n-1 and w == n-1:
            return cost
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<n:
                if pul >= 1 and dst[nh][nw][pul-1] > cost+t:
                    dst[nh][nw][pul-1] = cost+t
                    heappush(heap, (cost+t, nh, nw, pul-1))
                elif not pul and dst[nh][nw][2] > cost+g[nh][nw]+t:
                    dst[nh][nw][2] = cost+g[nh][nw]+t
                    heappush(heap, (cost+g[nh][nw]+t, nh, nw, 2))

n, t = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
dst = [[[inf, inf, inf] for _ in range(n)] for _ in range(n)]
print(dij())
for i in dst:
    print(i)

'''
5 1
1 10 1 100 1
10 1 100 1 1
1 100 1 1 1
100 1 1 1 1
1 1 1 1 1
'''




