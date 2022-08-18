'''
알파벳

세로R 가로C 대문자 알파벳 적혀있음.
좌상단에서 출발
새로 이동한 칸에 적혀있는 알파벳은 이전 알파벳과 달라야 한다. 완전 쌔삥이어야 함.
좌상단 출발해서 말이 최대로 몇칸 갈 수 있는가? 자기 자신도 1칸으로 친다.

입력
C R 1이상 20이하 둘 다
CCCC
CCCC

출력
1,1(0,0)에서 말이 최대로 갈 수 있는 거리 출력
'''
import sys 
input=sys.stdin.readline

## DFS Pypy3
R,C = map(int, input().split())
arr=[list(input()) for _ in range(R)]
check=[0]*(26)

dx=[1,-1,0,0]
dy=[0,0,1,-1]
maxi=0

def dfs(x,y,cnt):
    global maxi
    maxi=max(cnt,maxi)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<R and ny<C and nx>=0 and ny>=0 and check[ord(arr[nx][ny])-65]==0:
            check[ord(arr[nx][ny])-65]=1
            ncnt=cnt+1
            dfs(nx,ny,ncnt)
            check[ord(arr[nx][ny])-65]=0
check[ord(arr[0][0])-65]=1
dfs(0,0,1)
print(maxi)

### BFS set
import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 1
def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])])
    while q:
        x, y, ans = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)

BFS(0, 0)
print(answer)



from collections import deque
import sys
input = sys.stdin.readline
# 이동
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]
# BFS
def bfs(x, y, co, alp):
    global r, c
    co+=1
    q = deque()
    q.append((x, y, co, alp))
    maxc = 0
    while q:
        h, w, nc, nal = q.popleft()
        if maxc < nc:
            maxc = nc
        if maxc == r*c:
            return maxc
        for i in range(4):
            nh, nw = h + dh[i], w + dw[i]
            if 0 <= nh < r and 0 <= nw < c and not g[nh][nw] in nal:
                q.append((nh, nw, nc+1, nal + g[nh][nw]))
    return maxc

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, ct):
    global mac
    mac = max(mac, ct)
    sts.add(g[x][y])
    if mac == r*c or mac == 26:
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<r and 0<=ny<c and not g[nx][ny] in sts:
            dfs(nx, ny, ct+1)
            sts.remove(g[nx][ny])

r, c = map(int, input().split())
g = [input() for _ in range(r)]
mac, sts = 0, set()
dfs(0, 0, 1)
print(mac)
# print(bfs(0, 0, 0, g[0][0]))


