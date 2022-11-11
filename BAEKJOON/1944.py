'''
복제 로봇

획기적인 로봇 개잘했따. 복제를 원하는 갯수만큼 가능하다.
미로에 풀어두었다. 열쇠 찾아야 한다.
열쇠 위치와 로봇이 출발하는 위치에 로봇이 복제 할 수 있는 장치 장착해둠.
n*n 미로와 m개의 흩어진 열쇠 갯수, 로봇 시작 위치 제시. 모든 열쇠를 찾으면서 로봇이 움직이는 쵯수의 합을 최소로 해라. 상하좌우이동하며, 로봇이 열쇠 위치 도착 했을 때 열쇠를 찾은 것. 한 칸에 동시에 여러 로봇 존재 가능. 한 번 지나간 자리를 다시 이동 가능. 복제 시간 안듬. 이동 횟수 총 합은 모든 로봇이 각각 움직인 횟수 총합. 복제된 로봇이 열쇠를 모두 찾은 후 같은 위치일 필요 x.

입력
미로 크기 n, 열쇠 갯수 m 제시.
n개 줄 그래프 제시.
1 : 벽
0 : 길
S : 시작 위치 1개
K : 열쇠 위치 m개
S와 K에서만 복제.

출력
모든 로봇이 움직인 횟수의 총 합 출력. 불가능 할 경우 -1 출력.
'''
import sys
from collections import deque
from heapq import heappop, heappush
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 해서 넣을 것.
    if x < y:
        parent[y] = x
        alive.remove(y)
    else:
        parent[x] = y
        alive.remove(x)

def bfs(tup):
    global m
    nodnum = nods[tup]
    h, w = tup
    v = [[0]*n for _ in range(n)]
    q = deque([(h, w)])
    v[h][w] = 1
    g[h][w] = '0'
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if not v[nh][nw]:
                if g[nh][nw] == '0':
                    v[nh][nw] = v[h][w]+1
                    q.append((nh, nw))
                elif g[nh][nw] == 'K':
                    v[nh][nw] = v[h][w]+1
                    q.append((nh, nw))
                    heappush(heap, (v[h][w], nodnum, nods[(nh,nw)]))

n, m = map(int, input().rstrip().split())
g = []
nods = {}
cnt = 0
for i in range(n):
    s = list(input().rstrip())
    for j in range(n):
        if s[j] == 'S':
            sh, sw = i, j
            nods[(i, j)] = 0
            s[j] = 'K'
        elif s[j] == 'K':
            cnt += 1
            nods[(i,j)] = cnt
    g.append(s)

heap = []
for i in nods:
    bfs(i)

alive = set(range(m+1))
parent = list(range(m+1))

ans = 0

while heap and len(alive) != 1:
    cost, nod1, nod2 = heappop(heap)
    r1, r2 = find(nod1), find(nod2)
    if r1 == r2:
        continue
    union(r1, r2)
    ans += cost

if len(alive) == 1:
    print(ans)
else:
    print(-1)

'''
# 짱빠른 파이썬 코드
# 아마 프림 알고리즘 응용인듯?

import sys
import heapq
input = sys.stdin.readline

inf = 2500
D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def bfs(x, y):
    global M
    Q = [[0, x, y]]
    while Q:
        dis, x, y = heapq.heappop(Q)
        if ml[y][x] == 'K':
            if vl[y][x] == inf:
                vl[y][x] = dis
                M -= 1
                for dx, dy in D:
                    tx, ty = x + dx, y + dy
                    if 0 <= tx < N and 0 <= ty < N and 1 < vl[ty][tx] and ml[ty][tx] != '1':
                        heapq.heappush(Q, [1, tx, ty])
            continue
        if vl[y][x] > dis:
            vl[y][x] = dis
            for dx, dy in D:
                tx, ty = x + dx, y + dy
                if 0 <= tx < N and 0 <= ty < N and dis + 1 < vl[ty][tx] and ml[ty][tx] != '1':
                    heapq.heappush(Q, [dis+1, tx, ty])
    s = 0
    if M:
        print(-1)
        return
    for j in range(N):
        for i in range(N):
            if ml[j][i] == 'K':
                s += vl[j][i]
    print(s)


def init():
    for j in range(N):
        for i in range(N):
            if ml[j][i] == 'S':
                bfs(i, j)
                return


N, M = map(int, input().split())
ml = [input() for _ in range(N)]
vl = [[inf for _ in range(N)] for _ in range(N)]
init()
'''