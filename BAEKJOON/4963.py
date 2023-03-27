'''
섬의 갯수

대각선도 이동 가능. 섬 갯수 구해라.

입력
w, h 제시.
h개 줄 1은 땅 0은 바다
0,0 제시 시 종료
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(h, w):
    global n, m
    g[h][w] = 0
    q = deque([(h, w)])
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and g[nh][nw]:
                g[nh][nw] = 0
                q.append((nh, nw))
    return 1

mov = [(-1,0),(0,1),(1,0),(0,-1),(-1,1),(1,1),(1,-1),(-1,-1)]
while True:
    m, n = map(int, input().rstrip().split())
    if not m and not n:
        break
    g = [list(map(int, input().rstrip().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if g[i][j]:
                ans += bfs(i, j)
    print(ans)







