'''
안전영역

비와요. 비오면 그 높이 이하는 다 잠겨요.
안전 영역은 아이스크림 얼려먹기랑 똑같아요. 그 최대 갯수
N*N

입력
N 제시
N*N 높이 정보 제시
높이는 1이상 100이하
'''
import sys
sys.setrecursionlimit(10000000) # 리커션 에러
# 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, num): # dfs
    global n
    v[x][y] = num # 방문처리
    for i in range(4): # 재귀 dfs
        nx, ny = x+dx[i], y+dy[i]
        # 범위 안이고, 그래프값이 안잠겼고 방문처리 안됐으면 dfs
        if 0<=nx<n and 0<=ny<n and g[nx][ny] > num and v[nx][ny] != num:
            dfs(nx, ny, num)

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
v = [[0]*n for _ in range(n)] # 방문처리
# mx, mn = max(map(max, g)), min(map(min, g))
nns = [0]*(101)
mc = 1
for i in g:
    for j in i:
        nns[j] += 1
scanh = [i for i, v in enumerate(nns) if v != 0] # 그래프에 존재하는 높이리스트
for s in scanh:
    c = 0 # 높이마다 섬 갯수
    for i in range(n):
        for j in range(n):
            if g[i][j] <= s: # 잠겼으면 continue
                continue
            elif g[i][j] > s and v[i][j] != s: # 안잠겼고 방문 안했으면 dfs하고 1추가
                dfs(i, j, s)
                c+=1
    if c > mc: # 기존 저장된 맥스보다 크면 저장한다.
        mc = c
print(mc)



