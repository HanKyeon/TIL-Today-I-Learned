'''
아맞다우산

상하좌우 이동 가능. 챙겨야 할 물건들 위치를 알고 있을 ㄸㅐ, 물건을 모두 챙겨서 외출하기까지 최소 몇 걸음이 필요한지 구해라.

입력
n, m 제시.
집 구조 제시.
. 빈 곳
# 벽
S 시작
E 끝
X 물건 최대 5

출력
S에서 출발해서 모든 물건을 챙겨서 E까지 도착 할 수 있는 최소 시간 출력.
'''
'''
50*50이 최대, 물건은 5개가 최대. 시작+물건 해서 최대 6번 순회. 15000번 순회.
노드 간 거리 잡아서 최소 이동 구하기? 이거 청소 로봇 문제랑 같은거 같은뎅?
'''
import sys
from collections import deque
input = sys.stdin.readline

def dstSet(h, w, idx):
    global n, m
    q = deque([(h, w)])
    v = [[0]*m for _ in range(n)]
    v[h][w] = 1
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and not v[nh][nw]:
                if g[nh][nw] == 7: # 벽
                    continue
                if g[nh][nw] >= 0:
                    dst[idx][g[nh][nw]] = v[h][w]
                    dst[g[nh][nw]][idx] = v[h][w]
                v[nh][nw] = v[h][w] + 1
                q.append((nh, nw))

def dfs(idx, cnt, hap):
    global gdz, ans
    if cnt == gdz:
        ret = hap+dst[idx][gdz+1]
        if ans > ret:
            ans = ret
        return
    if hap >= ans:
        return
    for i in range(1, gdz+1):
        if v[i]:
            continue
        v[i] = 1
        dfs(i, cnt+1, hap+dst[idx][i])
        v[i] = 0

mov = [(-1,0), (0,1), (1,0), (0,-1)]
m, n = map(int, input().rstrip().split())
g = []
points = []
gdz = 0
for i in range(n): # 벽7 빈칸-1 시작0 물건1~5 끝점 마지막물건+1
    s = list(input().rstrip())
    for j in range(m):
        if s[j] == ".":
            s[j] = -1
        elif s[j] == "#":
            s[j] = 7
        elif s[j] == "X":
            gdz += 1
            s[j] = gdz
            points.append((i, j))
        elif s[j] == "S":
            sh, sw = i, j
            s[j] = 0
            points.insert(0, (i, j))
        elif s[j] == "E":
            eh, ew = i, j
    g.append(s)
points.append((eh, ew))
g[eh][ew] = gdz+1
dst = [[0]*(gdz+2) for _ in range(gdz+2)]
for i in range(len(points)-1):
    h, w = points[i]
    dstSet(h, w, i)

ans = 2501
v = [1]+[0]*(gdz+1)
dfs(0, 0, 0)
print(ans)

