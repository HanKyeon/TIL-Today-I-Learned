'''
미세먼지 안녕!

공청기 구매 예정.
크기가 r*c 격자판 r,c 미세먼지 양 실시간 모니터링.
공청기는 항상 1번 열에 설치. 크기는 두 행 차지. 공청기가 설치되어 있지 않은 칸에는 미세먼지가 있고, r,c에 있는 미세먼지의 양은 Ar,c 이다.

1초동안
1. 미세먼지 확산. 확산은 미세먼지가 있는 모든 칸에서 동시 발생.
- r,c 미세먼지는 인접한 네 방향으로 확산된다. 인접한 방향에 공청기가 있거나, 칸이 없으면 확산x
- 확산되는 양은 메인미세먼지//5 이다.
- r,c에 남은 미세먼지 양은 메인 미세먼지 양 - (확산된 미세먼지양)이다.
2. 공기청정기 작동.
- 위쪽 공청기는 반시계 방향 순환, 아래쪾은 시계방향 순환.
- 바람이 불면 미세먼지가 발마의 방향대로 모두 한 칸 씩 이동.
- 공청기에서 부는 바람은 미세먼지x, 공청기에 도착하면 미세먼지 정화됨.

T초 후 남아있는 미세먼지의 양.

입력
R, C, T r과 c는 6이상 50이하, t는 1000이하.
R개 줄 Arc 제시. 공ㅈ청기가 설치된 곳은 Arc가 -1이고, 나머지는 미세먼지 양. -1은 2번 위 아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸 이상 떨어져 있다.

출력
T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.
'''
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# 0은 위쪽, 1은 아래쪽
moves = [[(-1,0), (0,1), (1,0), (0,-1)], [(1,0), (0,1), (-1,0), (0,-1)]]

n, m, t = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
ans = sum(map(sum, g))+2
# 먼지 1초 함수
def sec1():
    global q
    gs = {}
    while q:
        h, w = q.popleft()
        cnt = 0
        if g[h][w]<5:
            continue
        for i in range(4):
            nh, nw = h+moves[0][i][0], w+moves[0][i][1]
            if 0<=nh<n and 0<=nw<m and g[nh][nw] != -1:
                cnt+=1
                if gs.get((nh, nw), 0):
                    gs[(nh, nw)] += g[h][w]//5
                else:
                    gs[(nh, nw)] = g[h][w]//5
        g[h][w] -= g[h][w]//5 * cnt
        if g[h][w]>4:
            if gs.get((h, w), 0):
                gs[(h, w)] += g[h][w]
            else:
                gs[(h, w)] = g[h][w]
            g[h][w] = 0
    for i in gs.keys():
        h, w = i
        g[h][w] += gs[i]
        if g[h][w] > 4:
            q.append((h, w))
    return

# 공청기 한바꾸. di로 위 아래 판단. dfs 형태로 할 것. 땡겨오는 방식.
def dfs0(h, w, mdep, di): # 현재 좌표, 위쪽인지 아래쪽인지, 최대 h 범위
    global ans
    nh, nw = h+moves[0][di][0], w+moves[0][di][1]
    if not (0<=nh<=mdep and 0<=nw<m):
        di = (di+1)%4
        nh, nw = h+moves[0][di][0], w+moves[0][di][1]
    if g[h][w] == -1:
        ans-=g[nh][nw]
        v[(nh, nw)] = 1
        g[nh][nw] = 0
        return dfs0(nh, nw, mdep, di)
    if g[nh][nw] != -1 and not v.get((nh, nw), 0):
        v[(nh, nw)] = 1
        g[h][w], g[nh][nw] = g[nh][nw], g[h][w]
        return dfs0(nh, nw, mdep, di)
    elif g[nh][nw] == -1:
        g[h][w] = 0
        return


def dfs1(h, w, mdep, di): # 현재 좌표, 위쪽인지 아래쪽인지, 최대 h 범위
    global ans
    nh, nw = h+moves[1][di][0], w+moves[1][di][1]
    if not (mdep<=nh<n and 0<=nw<m):
        di = (di+1)%4
        nh, nw = h+moves[1][di][0], w+moves[1][di][1]
    if g[h][w] == -1:
        v[(nh, nw)] = 1
        ans-=g[nh][nw]
        g[nh][nw] = 0
        return dfs1(nh, nw, mdep, di)
    if g[nh][nw] != -1 and not v.get((nh, nw), 0):
        v[(nh, nw)] = 1
        g[h][w], g[nh][nw] = g[nh][nw], g[h][w]
        return dfs1(nh, nw, mdep, di)
    elif g[nh][nw] == -1:
        g[h][w] = 0
        return

q = deque()
cln = []
for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            continue
        if g[i][j] == -1:
            cln.append((i, j))
            continue
        q.append((i, j))
cln.sort()
for _ in range(t):
    sec1()
    for i in g:
        print(i)
    print('===')
    v = {}
    dfs0(cln[0][0], cln[0][1], cln[0][0], 0)
    v = {}
    dfs1(cln[1][0], cln[1][1], cln[1][0], 0)
    for i in g:
        print(i)
    print('=============')

# ans = sum(map(sum, g))+2
print(ans)













