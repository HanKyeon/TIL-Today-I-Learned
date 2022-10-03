'''
거울 설치

집 곳곳에 거울을 설치.
새 집 이사. 거울을 잘 설치해서 장난 칠것. 한 쪽문에서 다른 쪽 문을 볼 수 있도록 거울 설치.
집 정보 제시. 한 쪽 문에서 다른 거울 보기 위해 설치해야 하는 거울의 최소 갯수
집 정보 제시.
거울 이빠이, 볼 수 있음.

입력
집 크기 n 제시.
n개 문자로 집 정보 제시.
#은 문이 설치된 곳, 항상 2개
.은 아무것도 없음
! 은 거울 설치 가능
*은 벽

출력
설치해야 할 거울 최소 갯수
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

def dij():
    global n
    h, w = dr.pop()
    heap = []
    v = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]
    v[h][w] = [1,1,1,1]
    for i in range(4):
        nh, nw = h+dh[i], w+dw[i]
        if 0<=nh<n and 0<=nw<n:
            if g[nh][nw] == '*':
                continue
            elif g[nh][nw] == '#':
                return 0
            else:
                heappush(heap, (0, nh, nw, i))
                v[nh][nw][i] = 1
    while heap:
        cnt, h, w, di = heappop(heap)
        nh, nw = h+dh[di], w+dw[di]
        if 0<=nh<n and 0<=nw<n and not v[nh][nw][di]:
            if g[nh][nw] == '#':
                return cnt
            if g[nh][nw] != '*':
                v[nh][nw][di] = 1
                heappush(heap, (cnt, nh, nw, di))
        if g[h][w] == '!':
            v[h][w] = [1,1,1,1]
            for i in range(4):
                if i == di:
                    continue
                nh, nw = h+dh[i], w+dw[i]
                if 0<=nh<n and 0<=nw<n and not v[nh][nw][i] and g[nh][nw] != '*':
                    if g[nh][nw] == '#':
                        return cnt+1
                    v[nh][nw][i] = 1 
                    heappush(heap, (cnt+1, nh, nw, i))

n = int(input())
g = [list(input().rstrip()) for _ in range(n)]
dr = []
for i in range(n):
    for j in range(n):
        if g[i][j] == '#':
            dr.append((i, j))
print(dij())






