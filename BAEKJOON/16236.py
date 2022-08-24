'''
아기 상어

N N 크기 공간 물고기 M마리 아기 상어 1
처음 아기 상어 크기 2
자기보다 작은 물고기만 먹을 수 있고
자기와 같으면 지나갈 수 있고
자기보다 크면 지나갈 수 없다.

어디로 이동 할 지 결정하는 방법은 아래와 같다.

-더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
-먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
-먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
--거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
--거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다

아기 상어는 자기 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
크기가 2인 아기상어는 2마리 먹으면 3으로 증가하고, 3인 아기상어는 3마리 먹으면 4가 된다.

아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구해라.

입력
공간의 크기 N 제시
공간 상태 제시.
0 빈칸 / 1~6 물고기 크기
9 아기상어

출력
엄마한테 sos 안하고 물고기 잡아먹는 시간
'''
from collections import deque
import sys
input = sys.stdin.readline

# 사방이동.
# 위쪽이 우선이기에 윗방향 우선 탐색, 좌측이 우선이기에 좌방향 우선 탐색.
dh = [-1, 0, 0, 1]
dw = [0, -1, 1, 0]

def bfs(h, w): # 좌표, 현재까지 이동 거리(시간초)
    global n, muk, ans, sha
    global sz, hg # 그냥 전역 선언으로 사이즈와 배고픈 정도 확인
    q = deque()
    v = [[0]*n for _ in range(n)]
    c = 0 # 이동거리
    q.append((h, w, c))
    v[h][w], g[h][w] = 1, 0 # 현위치 방문처리, 상어 이동을 위해 0처리.
    caneat = [] # 먹을 수 있는 것 리스트
    while q:
        h, w, c = q.popleft()
        for i in range(4):
            nh, nw = h + dh[i], w + dw[i]
            if 0<=nh<n and 0<=nw<n and 0 < g[nh][nw] < sz: # 0 아니도 상어보다 작으면
                v[nh][nw] = 1
                caneat.append((c+1, nh, nw))
            elif 0<=nh<n and 0<=nw<n and v[nh][nw] == 0 and (g[nh][nw] == 0 or g[nh][nw] == sz): # 범위내, 0이고 크기가 같은 물고기면
                v[nh][nw] = 1 # 방문한다!
                q.append((nh, nw, c+1)) # 추가한다!
    if caneat: # 먹을 수 있는걸 거리, h, w 순으로 정렬해서 첫번째꺼 먹는다.
        caneat.sort() # 정렬
        nc, nh, nw = caneat[0] # 거리, h, w
        sha[0] = (nh, nw) # 이동 할 거다~
        muk -= 1 # 먹었다!
        ans += nc # 이만큼 걸렸다!
        hg += 1 # 배 채웠다!
        if hg == sz: # 배를 다 채웠으면
            sz += 1 # 큰다!
            hg = 0 # 또 배고프다!
        return nh, nw #  탈출!
    sha = None
    return
# 입력
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
sha, muk = [], 0, # 상어 좌표, 먹이갯수
for i in range(n):
    for j in range(n):
        if g[i][j] == 9:
            sha.append((i, j))
        elif 0 < g[i][j] < 7:
            muk += 1
sz, hg, ans = 2, 0, 0 # 상어 크기, 배고픔, 답
while sha: # 먹이가 없을 때 상어 좌표를 None으로 바꾸고 리턴한다.
    bfs(sha[0][0], sha[0][1])
# 출력
print(ans)


'''
96 ms

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
v = 1
dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]
fish = []
shark = [2, 0]
q = deque([])
def bfs():
    global q, fish, v
    move = 0
    while q:
        # print(*visited,sep='\n')
        for _ in range(len(q)):
            # print(q)
            x, y, m = q.popleft()
            visited[x][y] = v
            if 0 < grid[x][y] < shark[0]:
                move = m
                grid[x][y] = 0
                # print(shark,'@@@@@',q,x,y,m,'@@@@@@@@@@@@@@@')
                q = deque([])
                fish.pop()
                shark[1] += 1
                if shark[1] == shark[0]:
                    shark[0] += 1
                    shark[1] = 0
                # print(q, (x,y),shark, fish)
                if not fish:
                    return m
                elif fish[-1] >= shark[0]:
                    return m
                v += 1
            for dx, dy in dir:
                if 0 <= x + dx < N and 0 <= y + dy < N:
                    if not visited[x + dx][y + dy] == v:
                        if grid[x + dx][y + dy] <= shark[0] and (x + dx, y + dy, m + 1) not in q:
                            q.append((x + dx, y + dy, m + 1))
            q = deque(sorted(q, key=lambda x: (x[2], x[0], x[1])))
    return move
for i in range(N):
    for j in range(N):
        if 0 < grid[i][j] < 7:
            fish.append(grid[i][j])
        elif grid[i][j] == 9:
            grid[i][j] = 0
            q.append((i, j, 0))
fish = sorted(fish, reverse=True)
result = bfs()
if result == None:
    print(0)
else:
    print(result)


'''








