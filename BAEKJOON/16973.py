'''
직사각형 탈출

크기 n m 격자판에 크기 h w 직사각형. 좌상단1,1 우하단 n,m
직사각형의 가장 좌상단은 sr, sc일 때, Fr Fc로 이동시키기 위한 최소 이동 횟수

격자 판에는 빈 칸 또는 벽 존재. 직사각형은 벽이 있는 칸에 잇을 수 없다. 격자판 벗어날 수 없다.
직사각형은 한 번에 한칸씩만 이동 가능.

입력
격자판의 크기 N, M 제시. N개 줄에 격자판 정보 제시. 0빈칸 1벽
직사각형 크기 h,w 시작좌표 sr,sc 도착좌표 fr,fc 제시

출력
최소 이동 횟수 출력
'''
from collections import deque
import sys
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]

n, m = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
lh, lw, sh, sw, eh, ew = map(int, input().rstrip().split())
sh, sw, eh, ew = sh-1, sw-1, eh-1, ew-1
v = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if g[i][j] == 1:
            for k in range(i-lh+1,i+1):
                for l in range(j-lw+1, j+1):
                    if 0<=k<n and 0<=l<m:
                        v[k][l] = 1

for i in v:
    print(i)

q = deque([(sh, sw)])
v[sh][sw] = 1
def bfs():
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and not v[nh][nw]:
                if nh == eh and nw == ew:
                    return v[h][w]
                v[nh][nw] = v[h][w]+1
                q.append((nh, nw))
    return -1

print(bfs())








