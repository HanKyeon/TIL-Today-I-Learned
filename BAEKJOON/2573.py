'''
빙산

빙산 이외의 바다는 0.
바닷물에 많이 접촉한 부분에서 더 빨리 줄어든다. 빙산 각 부분에 해당되는 칸에 있는 높이는 1년마다 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 갯수만큼 줄어든다. 0보다 더 줄어들지 않는다.
한 덩이 빙산이 주어질 때, 두 덩이 이상으로 분리되는 최초의 시간을 구하는 프로그램 작성.

입력
n, m 제시. 3이상 300이하.
그래프 제시. 빙산 칸수는 최대 10000개. 주변은 다 0이다.

출력
빙산이 분리되는 최초의 시간 출력. 빙산이 다 녹을 때까지 분리되지 않으면 0 출력.
'''
from collections import deque
import sys
input = sys.stdin.readline

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

def year():
    global q
    nq = {}
    while q:
        h, w = q.popleft()
        nq[(h, w)] = 0
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<m and g[nh][nw] == 0:
                nq[(h, w)] -= 1
    for i in nq.keys():
        h, w = i
        g[h][w] += nq[(h, w)]
        if g[h][w] <= 0:
            g[h][w] = 0
            continue
        else:
            q.append((h, w))

def bfs():
    global q, m, n
    ret = 1
    v = [[0]*m for _ in range(n)]
    nq = deque()
    if not q:
        return 0
    nq.append((q[0][0], q[0][1]))
    v[q[0][0]][q[0][1]] = 1
    while nq:
        h, w = nq.popleft()
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<m and g[nh][nw] > 0 and not v[nh][nw]:
                v[nh][nw] = 1
                nq.append((nh, nw))
    while q:
        h, w = q.popleft()
        nq.append((h, w))
        if v[h][w] == 1:
            continue
        ret += 1
        return ret
    q = nq
    return ret

n, m = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if not g[i][j]: continue
        q.append((i, j))
i = 0
cnt = 1
while 0 < cnt < 2:
    cnt = 0
    year()
    cnt = bfs()
    i += 1
if cnt == 0:
    i = 0
print(i)




'''
# 파이썬도 됨
import sys
input=sys.stdin.readline

R,C=map(int,input().split())
Map=[]
Map.append([0]*(C+2))
for i in range(R):
    Map.append([0]+list(map(int,input().split()))+[0])

DP=[[0]*(C+2) for i in range(R+2)]#인접 얼음 개수 
survived=set()
for r in range(R):
    for c in range(C):
        if Map[r][c]:
            survived.add((r,c))
            DP[r][c]+=not Map[r-1][c]
            DP[r][c]+=not Map[r+1][c]
            DP[r][c]+=not Map[r][c+1]
            DP[r][c]+=not Map[r][c-1]


def BFS():
    if not survived:
        return 0
    r,c=survived.pop()
    survived.add((r,c))
    que=[(r,c)]
    visited={(r,c)}
    while que:
        nq=set()
        for r,c in que:
            if  Map[r-1][c]>0 and ((r-1,c) not in visited):
                nq.add((r-1,c))
                visited.add((r-1,c))
            if Map[r+1][c]>0 and ((r+1,c) not in visited):
                nq.add((r+1,c))
                visited.add((r+1,c))
            if Map[r][c+1]>0 and ((r,c+1) not in visited):
                nq.add((r,c+1))
                visited.add((r,c+1))
            if Map[r][c-1]>0 and ((r,c-1) not in visited):
                nq.add((r,c-1))
                visited.add((r,c-1))
        que=nq
    if len(visited)==len(survived):
        return 1
    else:
        return 2
year=0
Ter=BFS()
while True:
    if Ter==0:
        print(0)
        break
    elif Ter==2:
        print(year)
        break
    death=set()#새로 녹은 빙하는 나중에 처리해야해!
    for r,c in survived:
        Map[r][c]-=DP[r][c]
        if Map[r][c]<1:
            death.add((r,c))
    survived=set(survived)-death
    for r,c in death:
        DP[r-1][c]+=1
        DP[r+1][c]+=1
        DP[r][c-1]+=1
        DP[r][c+1]+=1
    if death:
        Ter=BFS()
    year+=1
'''
















