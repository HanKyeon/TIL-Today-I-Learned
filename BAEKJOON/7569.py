'''
도마도

N*M*H 도마도
직접 맞닿은 곳만 영향 끼쳐서 익힌다.

상자크기 M, N 상자 수 H
상자에 담긴 도마도들의 상태가 M개의 정수로 주어짐.
N M M M M
N M M M M
N . . . NM
*H번 제시.

도마도가 하나 이상 존재.
도마도가 며칠 걸려 익히는지 출력

입력
2이상 100이하 M, N 1이상 100이하 H 제시.
도마도 상태 정보 1층부터 제시.
'''
'''
3차원 배열을 만들라는 소리인가?

bfs를 할 때 더 작은 c값이면 return을 해야하나?
'''
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0] # 0이상 n미만
dy = [0, 0, 1, -1, 0, 0] # 0이상 m미만
dz = [0, 0, 0, 0, -1, 1] # 0이상 h미만
# [h][n][m] [z][x][y] 순으로 읽어야 한다.
def bfs(qu):
    global m, n, h, mc
    pass

m, n, h = map(int, input().split())
g = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)] # 그래프
mc = 0 # 답
q = deque() # 덱
for i in range(h):
    for j in range(n):
        for k in range(m):
            if g[i][j][k] == 1: # 삼중으로 훑어서 1이 있는 곳 담기
                q.append((i, j, k))

while q:
    z, x, y = q.popleft() # pop
    if mc < g[z][x][y] :
        mc = g[z][x][y] # mc가 작으면 갱신해줌
    for i in range(6): # 상하좌우전후 확인
        nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
        if 0<=nz<h and 0<=nx<n and 0<=ny<m and g[nz][nx][ny] == 0:
            q.append((nz, nx, ny)) # 추가해주고
            g[nz][nx][ny] = g[z][x][y] + 1 # 값 갱신. 두개 서순해도 됨
# 0이 있으면 -1이 나와야 하므로 0으로 바꿔줌.
for i in g:
    for j in i:
        if 0 in j:
            mc = 0
            break
    if mc == 0:
        break

print(mc-1)

