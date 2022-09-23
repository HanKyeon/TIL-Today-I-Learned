'''
레이저 통신

크기가 1*1인 정사각형으로 나눠진 w*h 크기의 지도. 각 칸은 빈칸이나 벽. 두 칸은 c로 표시되어 있는 칸. 두 칸을 레이저로 통신하가ㅣ 위해 설치해야 하는 거울 갯수의 최솟값. 즉, 몇 번 꺾느냐.

입력
첫째 줄에 w와 h 제시.
지도 제시. .길 *벽 c시작/목적지

출력
연결하기 위해 설치해야 하는 거울 갯수의 최솟값.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

def dij(info):
    global n, m
    h, w = info
    v = [[int(4000)]*m for _ in range(n)]
    g[h][w] = 0
    heap = []
    for i in range(4):
        nh, nw = h+dh[i], w+dw[i]
        if 0<=nh<n and 0<=nw<m :
            if g[nh][nw] == '.':
                v[nh][nw] = 0
                heappush(heap, (0, nh, nw, i))
            elif g[nh][nw] == 'C':
                return 0
            else:
                continue

    while heap:
        cnt, h, w, di = heappop(heap)
        if (h, w) == cz[0]:
            # for i in v:
            #     print(i)
            return cnt
        if v[h][w] < cnt:
            continue
        nh, nw = h+dh[di], w+dw[di]
        if 0<=nh<n and 0<=nw<m and g[nh][nw] != '*' and v[nh][nw] >= cnt:
            v[nh][nw] = cnt
            heappush(heap, (cnt, nh, nw, di))
        for i in range(4):
            if i==di:
                continue
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<m and g[nh][nw] != '*' and v[nh][nw] >= cnt+1:
                v[nh][nw] = cnt+1
                heappush(heap, (cnt+1, nh, nw, i))

m, n = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]
cz = []
for i in range(n):
    for j in range(m):
        if g[i][j] == 'C':
            cz.append((i, j))
print(dij(cz.pop()))




'''
5 5
C..**
.*.**
.*...
.***C
.....
'''





