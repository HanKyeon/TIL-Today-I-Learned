'''
창영이와 퇴근

n*n 격자. 1,1부터 n,n까지 이동. 상하좌우 이동. 격자엔 높이 있음.
인접한 격자 사이의 높이 차 절댓값이 경사. 경사가 클 수록 경사가 가파르다.
지나는 최대 경사의 최솟값을 구해라.

입력
n 제시.
n개 줄 격자 높이 제시.

출력
1,1에서 n,n까지 경로상 최대 경사 최솟값 출력.
'''
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

mov = [(-1,0), (0,1), (1,0), (0,-1)]

def dij():
    global n
    dst = [[1000000001]*n for _ in range(n)]
    dst[0][0] = 0
    heap = [(0, 0, 0)]
    while heap:
        cha, h, w = heappop(heap)
        if cha > dst[h][w]:
            continue
        if h == n-1 and w == n-1:
            return cha
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<n:
                ncha = abs(g[h][w]-g[nh][nw])
                if ncha <= cha and dst[nh][nw] > cha:
                    dst[nh][nw] = cha
                    heappush(heap, (cha, nh, nw))
                elif ncha > cha and dst[nh][nw] > ncha:
                    dst[nh][nw] = ncha
                    heappush(heap, (ncha, nh, nw))

n = int(input())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
print(dij())





'''
3
20 15 20
5 10 20
2 1 0

5
'''