'''
농장 관리

섬 찾아라.
섬은 같은 높이를 가지는 하나의 격자 혹은 인접한 격자들의 집합. 인접의 정의는 x, y 좌표 차이 모두 1 이하인 경우. 즉, 8방인듯. 뽕우리와 인접한 격자는 모두 산 봉우리의 높이보다 작아야 한다.

입력
n, m 제시.
n개 줄 m개 정수 제시. 최대 높이 500 & 0이상 양수

출력
산봉우리 갯수
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(h, w, val):
    global n, m, minh, ans
    v[h][w] = 1
    q = deque([(h, w)])
    ret = 1
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and not v[nh][nw]:
                if g[nh][nw] <= g[h][w]:
                    v[nh][nw] = 1
                    q.append((nh, nw))
                elif ret and g[nh][nw] > val:
                    ret = 0
    return ret

mov = [(-1,0),(0,1),(1,0),(0,-1), (1,1),(1,-1),(-1,1),(-1,-1)]
n, m = map(int, input().rstrip().split())
g = []
minh = 501
for _ in range(n):
    s = list(map(int, input().rstrip().split()))
    for j in s:
        if j < minh:
            minh = j
    g.append(s)
ans = 0
v = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if v[i][j] or g[i][j] == minh:
            continue
        ans += bfs(i, j, g[i][j])
print(ans)


import sys
sys.setrecursionlimit(10 ** 6)
def dfs(a, b):
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]
    global trigger
    visited[a][b] = True
    for i in range(8):
        x = a + dx[i]
        y = b + dy[i]
        if -1 < x < n and -1 < y < m:
            if graph[a][b] < graph[x][y]:
                trigger = False
            if not visited[x][y] and graph[x][y] == graph[a][b]:
                dfs(x, y)

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] > 0 and not visited[i][j]:
            trigger = True
            dfs(i, j)
            if trigger:
                cnt += 1
print(cnt)
















