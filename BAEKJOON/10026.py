'''
적록색약

R과 G의 차이를 거의 못느낀다.
N*N 그리드 칸. RGB 제시

그림은 몇개의 칸으로 나뉘어져 있다.
같은 색상이 상하좌우로 인접해 있는 경우 두 글자는 같은 구역
아이스크림 얼려먹기 같음

적록색약이 봤을 때 구역의 수와 정상이 봤을 때 구역의 수

입력
N 1이상 100이하
N개의 그림 제시

출력
색약 구역 갯수, 정상 구역 갯수
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
sy = 'RG'

def 색약(x, y, val): # 색약 dfs
    global n
    v[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if val == 'B' and 0 <= nx < n and 0 <= ny < n and g[nx][ny] == 'B' and v[nx][ny] == 0:
            색약(nx, ny, val)
        elif val in sy and 0 <= nx < n and 0 <= ny < n and g[nx][ny] in sy and v[nx][ny] == 0:
            색약(nx, ny, val)

def 정상(x, y, val): # 정상 dfs
    global n
    v[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and g[nx][ny] == val and v[nx][ny] == 0:
            정상(nx, ny, val)

n = int(input())
g = [input() for _ in range(n)]
v = [[0]*n for _ in range(n)]

sc, jc = 0, 0 # 색약 갯수, 정상 갯수
for i in range(n): # 색약 갯수 세기
    for j in range(n):
        if v[i][j] == 0:
            색약(i, j, g[i][j])
            sc += 1

v = [[0]*n for _ in range(n)] # 아까 v 썼으니 다시 초기화 해야함.
for i in range(n): # 정상 개수 세기
    for j in range(n):
        if v[i][j] == 0:
            정상(i, j, g[i][j])
            jc += 1

print(jc, sc) # 정상 색약 순서로 출력











