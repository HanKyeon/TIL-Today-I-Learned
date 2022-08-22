'''
치즈

사각형의 판. 빵꾸뚫린 치즈.
까생이는 치즈 없음. 공기와 접촉된 부분은 1시간에 녹음.
치즈 내의 공기가 공기와 만나면 그 부분들도 삭는다.

입력
가로 세로길이 양정수로 제시. 최대 100 100
치즈 없는 칸0 치즈 있는 칸 1 숫자 사이 빈 칸 제시.

출력
치즈가 모두 녹아 없어지는데 걸리는 시간.
모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여있는 칸의 갯수
'''
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs1time(stl):
    global n, m
    li = deque(stl)
    
    while li:
        x, y = li.popleft()
        g[x][y] -= 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and g[nx][ny] == 1:
                g[nx][ny] -= 1
            elif 0<=nx<n and 0<=ny<m and g[nx][ny] != 1:
                li.append((nx, ny))
        


n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
startli = []
for i in range(n):
    startli.append((i, 0))
    startli.append((i, m-1))
for j in range(m):
    startli.append((0, j))
    startli.append((n-1, j))

for i in g:
    print(i)
bfs1time(startli)
for i in g:
    print(i)

