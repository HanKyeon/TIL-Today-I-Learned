'''
알고 스팟

알고스팟 운영진 미로 갇혔다.
n*m. 벽 이동 불가. 항상 같은 방에 있어야 한다. 이동 할 수 있는 방은 상하좌우이다.
1,1에 있는 알고 스팟 운영진이 n, m 으로 이동하려면 벽을 최소 몇 개 부숴야 하는지 작성.

입력
미로의 크기를 나타내는 가로m 세로n 제시.
미로 상태 제시. 0은 방 1은 벽

출력
n, m으로 이동하기 위해 벽을 몇 개 부숴야 하는가?
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

m, n = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]
v = [[0]*m for _ in range(n)]
heap = [(0, 0, 0)]
while heap:
    c, h, w = heappop(heap)
    if h == n-1 and w == m-1:
        break
    for i in range(4):
        nh, nw = h + dh[i], w + dw[i]
        if 0<=nh<n and 0<=nw<m and not v[nh][nw]:
            v[nh][nw] = 1
            if g[nh][nw] == '1':
                heappush(heap, (c+1, nh, nw))
            else:
                heappush(heap, (c, nh, nw))
print(c)


























