'''
그림

큰 도화지에 그림이 그려져 있을 때, 그 그림의 갯수와 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하라.
섬찾기 문제.

입력
n, m 제시.
n개 줄 그림 제시.

출력
섬 갯수, 가장 넓은 섬 넓이 출력. 하나도 없으면 0
'''
import sys
from collections import deque
input = sys.stdin.readline

mov = [(-1,0),(0,1),(1,0),(0,-1)]
n, m = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
cnt, ans = 0, 0
def bfs(h, w):
    global ans, n, m
    q = deque([(h, w)])
    v[h][w] = 1
    ret = 1
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and g[nh][nw] and not v[nh][nw]:
                v[nh][nw] = 1
                ret += 1
                q.append((nh, nw))
    if ans < ret:
        ans = ret

for i in range(n):
    for j in range(m):
        if g[i][j] and not v[i][j]:
            cnt += 1
            bfs(i, j)

print(cnt)
print(ans)



