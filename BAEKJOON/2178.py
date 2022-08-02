'''
미로탐색
'''
from collections import deque
# 입력
n, m = map(int,input().split())
g = []
for _ in range(n) :
    g.append(list(map(int, input())))
# bfs에 필요한 내용들
q= deque()
x, y = 0, 0
q.append([x, y, 0])
# 사방 이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# bfs
while q:
    ne = q.popleft()
    nx, ny, c = ne[0], ne[1], ne[2]
    if g[nx][ny] == 0 : # 이미 방문 상태면 이동 안함
        continue
    g[nx][ny] = 0
    c += 1
    if nx == n-1 and ny == m-1 : # 이동 끝났으면 탈출
        print(c)
        break
    # 사방향을 큐에 추가. 범위 내에 있고, 방문 안되어 있을 때.
    for i, j in zip(dx, dy) :
        if 0 <= nx+i < n and 0 <= ny+j < m and g[nx+i][ny+j] != 0 :
            q.append([nx+i, ny+j, c])

# 방문처리 및 깊이로 셌는데, x y를 팝해서 받는 변수로 하고 nx ny를 x+dx y+dy라 하면
# g[nx][ny] = g[x][y]+1 이 형태로 숫자를 편하게 셀 수 있다.