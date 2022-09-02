'''
내리막 길

0,0 시작해서 젤 우하단으로 감소하는 길로만 갈 수 있는 경우의 수

입력
세로M 가로N
높이제시, 높이는 1만 이하 자연수

출력
첫째 줄에 이동 가능한 경로의 수 H 출력. 모든 입력에 대해 H는 10억 이하 음이 아닌 정수
'''
# DFS + DP문제.

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(10e6))

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

def dfs(h, w):
    global m, n, ans, v
    if h == m-1 and w == n-1:
        return 1

    vc = 0
    for i in range(4):
        nh, nw = h + dh[i], w + dw[i]
        if 0<=nh<m and 0<=nw<n and g[nh][nw]<g[h][w] and v[nh][nw] < 0:
            a = dfs(nh, nw)
            vc+=a
        elif 0<=nh<m and 0<=nw<n and g[nh][nw]<g[h][w] and v[nh][nw] >= 0:
            vc += v[nh][nw]
    v[h][w] = vc

    return vc

m, n = map(int, input().split())
g = [list(map(int, input().rstrip().split())) for _ in range(m)]
ans = 0
v = [[-1]*n for _ in range(m)]
dfs(0, 0)
for i in v:
    print(*i)
print(v[0][0])

'''
# 빠른 코드
from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def dfs(r, c):
    if memo[r][c] == -1:
        count = 0
        cur_height = board[r][c]
        
        for r_dir, c_dir in dirs:
            next_r = r+r_dir
            next_c = c+c_dir
            if 0 <= next_r < row and 0 <= next_c < col and board[next_r][next_c] < cur_height:
                count += dfs(next_r, next_c)
        memo[r][c] = count
    return memo[r][c]

row, col = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(row)]
memo = [[-1 for __ in range(col)] for _ in range(row)]
memo[row-1][col-1] = 1

result = dfs(0, 0)
print(result)
'''



'''
# BFS 시간 초과
from collections import deque
import sys
input = sys.stdin.readline

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

m, n = map(int, input().split())
g = [list(map(int, input().rstrip().split())) for _ in range(m)]
sets = set()
q = deque()
q.append((0, 0))
ans = 0
while q:
    h, w = q.popleft()
    fla = False
    if h == m-1 and w == n-1:
        ans += 1
        continue
    if (h, w) in sets:
        continue
    for i in range(4):
        nh, nw = h + dh[i], w + dw[i]
        if 0<=nh<m and 0<=nw<n and g[nh][nw]<g[h][w] and not (nh, nw) in sets:
            q.append((nh, nw))
            fla = True
    if not fla:
        sets.add((h, w))
print(ans)

'''
