'''
게임

형택이는 1부터 9까지의 숫자와 구멍이 있는 직사각형 보드에서 게임을 함
보드의 0,0에 동전 올림.
1. 동전이 있는 곳에 쓰여있는 숫자 X를 본다.
2. 상하좌우 중 하나 고른다
3. 해당 방향으로 X만 이동. 구멍 무시.
동전이 빠지거나 바깥으로 나가면 게임 종료. 되도록 오래 하고 싶음.
보드 상태가 주어졌을 때, 형택이가 최대 몇 번 동전을 움직일 수 있는가

입력
n, m 제시.
n개 줄 보드 제시. 1부터 9까지 자연수 혹은 H. H는 구멍

출력
정답 출력
사이클 가능하면 -1 출력
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)

n, m = map(int, input().rstrip().split())
g = []
for _ in range(n):
    g.append(input().rstrip())
v = [[False for i in range(m)] for j in range(n)]
f = [[False for i in range(m)] for j in range(n)]
ts = []
mov = [(-1,0),(0,1),(1,0),(0,-1)]

def dfs(w, h):
    for i in mov:
        k = int(g[h][w])
        nw = (k * i[0]) + w
        nh = (k * i[1]) + h
        if 0<=nw<m and 0<=nh<n and g[nh][nw] != 'H':
            if f[nh][nw]:
                continue
            if v[nh][nw]:
                print(-1)
                exit()
            v[nh][nw] = True
            dfs(nw, nh)
            v[nh][nw] = False
    f[h][w] = True
    ts.append([w, h])

dfs(0, 0)
dp = [[1 for i in range(m)] for j in range(n)]
while len(ts) != 0:
    val = ts.pop()
    for i in mov:
        k = int(g[val[1]][val[0]])
        nw = (k * i[0]) + val[0]
        nh = (k * i[1]) + val[1]
        if -1 < nw < m and -1 < nh < n and g[nh][nw] != 'H':
            dp[nh][nw] = max(dp[nh][nw], dp[val[1]][val[0]] + 1)

ans = 1
for i in dp:
    for j in i:
        ans = max(ans, j)
print(ans)

'''
# 빠름
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if visited[x][y]:
        print(-1)
        exit()
    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y] = 1
    val = int(board[x][y])
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = x + i * val, y + j * val
        if (0 <= new_x < n) and (0 <= new_y < m):
            if board[new_x][new_y] != 'H':
                visited[x][y] = True
                dp[x][y] = max(dp[x][y], dfs(new_x, new_y) + 1)
                visited[x][y] = False
    return dp[x][y]

n, m = map(int, input().split())
board = [[i for i in input()] for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dfs(0, 0)

print(dp[0][0])
'''

'''
def parse(w):
    return 0 if w == "H" else int(w)

def memo(stp, h, w):
    global n, m
    if not stp:
        return
    for dh, dw in mov:
        nh, nw = h+dh*stp, w+dw*stp
        if 0<=nh<n and 0<=nw<m:
            dp[h][w].append((nh, nw))
def dfs(h, w, dep):
    global n, m, ans
    if not g[h][w]:
        if ans < dep:
            ans = dep
        return
    if not dp[h][w]:
        if ans < dep+1:
            ans = dep+1
        return
    for nh, nw in dp[h][w]:
        if f[nh][nw]:
            continue
        if v[nh][nw]:
            ans = -1
            return
        v[nh][nw] = 1
        dfs(nh, nw, dep+1)
        v[nh][nw] = 0
        if ans == -1:
            return
    f[h][w] = 1

mov = [(-1,0),(0,1),(1,0),(0,-1)]
n, m = map(int, input().rstrip().split())
g = []
dp = [[[] for _ in range(m)] for _ in range(n)]
for i in range(n):
    s = list(map(parse, input().rstrip()))
    for j in range(m):
        memo(s[j], i, j)
    g.append(s)
v = [[0]*m for _ in range(n)]
f = [[0]*m for _ in range(n)]
v[0][0] = 1
ans = 0
dfs(0, 0, 0)
print(ans)
'''

