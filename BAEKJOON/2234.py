'''
성곽

굵은 선은 벽, 점선은 통로. 지도 입력 받아서 다음을 계산하라.
1. 성에 있는 방의 갯수
2. 가장 넓은 방의 넓이
3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기.
성은 m*n 정사각형칸. 성에는 최소 두 개의 방.

입력
정수 m, n 제시.
n개 줄에 벽 정보 제시.
서쪽에 벽이 있다면 1, 북족에 벽이 있다면 2, 동쪽에 벽이 있다면 4, 남쪽에 벽이 있다면 8을 더한 갓ㅂ 제시. 이진수의 각 비트이다. 값은 0이상 15이하 범위.

출력
1의 답
2의 답
3의 답
'''
from collections import deque
import sys
input = sys.stdin.readline

'''
없음0
서1 북2 동4 남8
서북3 북동6 동남12 동서5 북남10 서남9
서북동7 서북남11 서동남13 북동남14
동서남북15
'''
# for i in range(16):
#     s = bin(i)[2:]
#     s = list(map(int, s))
#     while len(s)<4:
#         s = [0]+s
#     print(s)

# dh = [1, 0, -1, 0]
# dw = [0, 1, 0, -1]

mov = [(1,0), (0,1), (-1,0), (0,-1)]
ntm = [[1,1,1,1],[1,1,1,0],[1,1,0,1],[1,1,0,0],[1,0,1,1],[1,0,1,0],[1,0,0,1],[1,0,0,0],[0,1,1,1],[0,1,1,0],[0,1,0,1],[0,1,0,0],[0,0,1,1],[0,0,1,0],[0,0,0,1],[0,0,0,0]]

def bfs(i, j, nbr):
    global n, m
    v[i][j] = nbr
    q = deque([(i, j)])
    cnt = 1
    while q:
        h, w = q.popleft()
        for i in range(4):
            if ntm[g[h][w]][i]:
                nh, nw = h+mov[i][0], w+mov[i][1]
                if 0<=nh<n and 0<=nw<m and not v[nh][nw]:
                    v[nh][nw] = nbr
                    q.append((nh, nw))
                    cnt += 1
            else:
                nh, nw = h+mov[i][0], w+mov[i][1]
                if 0<=nh<n and 0<=nw<m and 0<v[nh][nw]<nbr and (nbr, v[nh][nw]) not in relation:
                    relation.add((nbr, v[nh][nw]))
    rcnt.append(cnt)

m, n = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
rcnt = [0]
relation = set()
cnt = 1
for i in range(n):
    for j in range(m):
        if not v[i][j]:
            bfs(i, j, cnt)
            cnt += 1

ans = 0
for x, y in relation:
    s = rcnt[x]+rcnt[y]
    if ans < s:
        ans = s
print(len(rcnt)-1)
print(max(rcnt))
print(ans)


'''
# 빠른 코드
def pos(y, x):
    global r, c
    return y >= 0 and y < r and x >= 0 and x < c

def bfs(y, x):
    global wall, vis, cnt, r, c, turn, color

    ret = 1
    d = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    q = [(y, x)]
    can = [(y, x)]
    vis[y][x] = True
    while q:
        y, x = q.pop(0)
        for i in range(4):
            ny, nx = y + d[i][0], x + d[i][1]
            if pos(ny, nx) and (wall[y][x] & (1 << i)) == 0 and not vis[ny][nx]:
                vis[ny][nx] = True
                q.append((ny, nx))
                can.append((ny, nx))
                ret += 1
    for p in can:
        y, x = p
        cnt[y][x] = ret
        color[y][x] = turn
    turn += 1
    return ret

c, r = map(int, input().split())
vis = [[False for i in range(c)] for j in range(r)]
cnt = [[0 for i in range(c + 1)] for j in range(r + 1)]
color = [[0 for i in range(c + 1)] for j in range(r + 1)]
wall = []
turn = 0
for _ in range(r):
    wall.append(list(map(int, input().split())))
ans = [0, 0, 0]
for y in range(r):
    for x in range(c):
        if not vis[y][x]:
            ret = bfs(y, x)
            ans[0] += 1
            ans[1] = max(ans[1], ret)
for y in range(r):
    for x in range(c):
        if color[y][x] != color[y + 1][x]:
            ans[2] = max(ans[2], cnt[y][x] + cnt[y + 1][x])
        if color[y][x] != color[y][x + 1]:
            ans[2] = max(ans[2], cnt[y][x] + cnt[y][x + 1])
for a in ans:
    print(a)
'''




