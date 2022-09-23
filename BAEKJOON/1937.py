'''
욕심쟁이 판다.

n*n 대나무 숲. 어떤 지역에서 대나무 먹기 시작. 다 먹으면 상하좌우 중 한 곳으로 이동. 단, 먹고 이동 하는 곳에 대나무가 더 많아야 한다.

어떤 지점에 풀어놓고 어떤 곳으로 이동시켜야 판다가 최대 칸을 방문 할 수 있는지.

입력
대나무숲 크기 n
대나무 숲 정보.

출력
판다 최대 이동 칸 수
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(260000)

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

def dfs(h, w):
    global n
    for i in range(4):
        nh, nw = h+dh[i], w+dw[i]
        if 0<=nh<n and 0<=nw<n and g[h][w] < g[nh][nw]:
            v[nh][nw] = v[h][w] + 1
            dfs(nh, nw)

n = int(input())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
v = [[1]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if v[i][j] == 1:
            dfs(i, j)

ans = max(map(max, v))

print(ans)

'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]
move = [(0,1),(1,0),(0,-1),(-1,0)]
ans = 0

def dfs(x,y):
    if dp[x][y] == -1:
        dp[x][y] = 0
        
        for a,b in move:
            dx=x+a; dy=y+b
            if n>dx>=0 and n>dy>=0 and board[dx][dy] > board[x][y]:
                dp[x][y] = max(dp[x][y],dfs(dx,dy))
    
    return dp[x][y]+1

for i in range(n):
    for j in range(n):
        ans = max(ans,dfs(i,j))
            
print(ans)
'''











