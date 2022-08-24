'''
치즈

N M 모눈종이. 세로 가로.
2변 이상이 공기와 접촉되어 있다면 녹는다.
구멍 뿅뿅 나있고, 외부와 격리된 상태면 없는 것으로 한다!
치즈가 모두 녹아 없어지는게 걸리는 시간!
가장자리는 치즈 없다!

입력:
N M 5이상 100이하
치즈1 치즈x0

출력
치즈가 모두 없어지는데 걸리는 시간.
'''
from collections import deque
import sys
input = sys.stdin.readline
# 사방이동
dh = [-1, 1, 0, 0]
dw = [0, 0, 1, -1]
# BFS
def bfs():
    global n, m
    v = [[0]*m for _ in range(n)] # 방문 그래프
    q = deque() # 큐
    q.append((0, 0)) # 0,0에서 시작
    while q: # 다 돌 때까지
        h, w = q.popleft() # 좌표
        for i in range(4): # 사방 확인
            nh, nw = h + dh[i], w + dw[i] # 새 좌표
            if 0 <= nh < n and 0 <= nw < m and g[nh][nw] == 0 and v[nh][nw] == 0: # 좌표 내이고 0이고 방문 안했으면
                v[nh][nw] = 1 # 방문처리
                q.append((nh, nw)) # 큐에 추가
            elif 0 <= nh < n and 0 <= nw < m and g[nh][nw] == 1: # 1이라면
                v[nh][nw] += 1 # 1추가
                if v[nh][nw] >= 2: # 추가하고 2개 이상이면
                    v[nh][nw] = 1 # 방문처리 1로 해주고
                    g[nh][nw] = 0 # 녹았다고 처리해줌

n, m = map(int, input().split()) # n*m 받기
g = [list(map(int, input().split())) for _ in range(n)] # 그래프
ans = 0 # 정답
while sum(map(sum, g)): # 그래프의 합이 0이 될 때까지
    bfs() # 한 번 씩 실행
    ans += 1 # 한 번 실행마다 1시간
print(ans) # 출력



'''
파이썬으로 556ms 한 괴물 아저씨 코드

from collections import deque


dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def updateOutside(nums):
    r, c = nums
    Q = deque()
    Q.append([r, c])

    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if cheeze_map[nr][nc] == 0:
                    visited[nr][nc] = 1
                    Q.append([nr, nc])

def meltChecker():
    goodbye_cheeze = []
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue

            if cheeze_map[i][j] == 1:
                cnt = 0
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if cheeze_map[nr][nc] == 0 and visited[nr][nc]:
                        cnt += 1

                if cnt >= 2:
                    goodbye_cheeze.append([i, j])

    return goodbye_cheeze

def updateCheeze(nums):
    global cheeze_left
    for C in nums:
        r, c = C
        cheeze_map[r][c] = 0
        cheeze_left -= 1
        if not visited[r][c]:
            visited[r][c] = 1
            updateOutside([r, c])


N, M = map(int, input().split())
cheeze_map = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

updateOutside([0, 0])

cheeze_left = 0
for i in range(N):
    cheeze_left += cheeze_map[i].count(1)

time = 0
while cheeze_left:

    melt_cheeze = meltChecker()
    updateCheeze(melt_cheeze)

    time += 1

print(time)
'''


