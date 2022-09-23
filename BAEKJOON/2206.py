'''
벽 부수고 이동하기

입력
1이상 1000이하 N, M
N개줄에 M길이 미로 제시.

출력
첫째 줄게 최단거리 출력.
'''
# 다익스트라로 해결.
# 그런데 최단거리라 dep을 기준으로 해야한다. 벽을 부수는 횟수 최소로 도달하는 것이 아니라서.
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

n, m = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]
v = [[2]*m for _ in range(n)]
heap = [(1, 0, 0, 0)]
fla = False
while heap:
    dep, cnt, h, w = heappop(heap)
    if h==n-1 and w==m-1:
        fla = True
        break
    if v[h][w] < cnt:
        continue
    for i in range(4):
        nh, nw = h+dh[i], w+dw[i]
        if 0<=nh<n and 0<=nw<m and g[nh][nw] == '0':
            if v[nh][nw] > cnt:
                v[nh][nw] = cnt
                heappush(heap, (dep+1, cnt, nh, nw))
        if 0<=nh<n and 0<=nw<m and g[nh][nw] == '1':
            if v[nh][nw] > cnt+1:
                v[nh][nw] = cnt+1
                heappush(heap, (dep+1, cnt+1, nh, nw))
if fla:
    print(dep)
else:
    print(-1)
























'''11
from collections import deque
import sys
input = sys.stdin.readline

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]
'''
'''11
def del1():
    global n, m
    v = [[0]*m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    v[0][0] = 1
    li = []
    while q:
        h, w = q.popleft()
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<m and v[nh][nw] == 0 and g[nh][nw] == '0':
                v[nh][nw] = 1
                q.append((nh, nw))
            elif 0<=nh<n and 0<=nw<m and v[nh][nw] == 0 and g[nh][nw] == '1':
                v[nh][nw] = 1
                li.append((nh, nw))
    return li
'''
'''
def bfs(): # 단순 bfs
    global n, m, ans
    v = [[0]*m for _ in range(n)]
    q = deque()
    q.append((0, 0, 1))
    v[0][0] = 1
    while q:
        h, w, nc = q.popleft()
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if nh == n-1 and nw == m-1:
                ans = min(ans, nc+1)
                return
            if 0 <= nh < n and 0 <= nw < m and v[nh][nw] == 0 and g[nh][nw] == '0':
                q.append((nh, nw, nc+1))
                v[nh][nw] = 1
'''
'''11
def nbfs():
    global n, m, ans
    v = [[0]*m for _ in range(n)]
    q = set()
    q.add((0, 0, 1, 1))
    v[0][0] = 1
    while q:
        h, w, nc, bc = q.pop()
        # v[h][w] = 1
        if h == n-1 and w == m-1:
            ans = nc
            return
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if nh == n-1 and nw == m-1:
                ans = min(ans, nc+1)
                return
            if 0 <= nh < n and 0 <= nw < m and v[nh][nw] == 0 and g[nh][nw] == '0':
                v[nh][nw] = 1
                q.add((nh, nw, nc+1, bc))
            elif 0 <= nh < n and 0 <= nw < m and v[nh][nw] == 0 and g[nh][nw] == '1' and bc == 1:
                v[nh][nw] = 1
                q.add((nh, nw, nc+1, 0))

n, m = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]

ans = int(10e9)
bw = del1() # 지울 기둥 목록
'''
'''
for i, j in bw: # 브루트 포스
    # g[i][j] = '0'
    nbfs()
    # g[i][j] = '1'

if not bw:
    nbfs()
'''
'''11
nbfs()
if ans != int(10e9):
    print(ans)
else:
    print(-1)
'''

'''
3 3
010
101
110

9 9 
010001000
010101010
010101010
010101010
010101010
010101010
010101010
010101011
000100010
'''



'''
from collections import deque
import sys
input = sys.stdin.readline

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

def del1():
    global n, m
    v = [[0]*m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    v[0][0] = 1
    li = []
    while q:
        h, w = q.popleft()
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<m and v[nh][nw] == 0 and g[nh][nw] == '0':
                v[nh][nw] = 1
                q.append((nh, nw))
            elif 0<=nh<n and 0<=nw<m and v[nh][nw] == 0 and g[nh][nw] == '1':
                v[nh][nw] = 1
                li.append((nh, nw))
    return li

def bfs():
    global n, m, ans
    v = [[0]*m for _ in range(n)]
    q = deque()
    q.append((0, 0, 1))
    v[0][0] = 1
    while q:
        h, w, nc = q.popleft()
        if nc > ans:
            break
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if nh == n-1 and nw == m-1:
                ans = min(ans, nc+1)
                return
            if 0 <= nh < n and 0 <= nw < m and v[nh][nw] == 0 and g[nh][nw] == '0':
                q.append((nh, nw, nc+1))
                v[nh][nw] = 1

n, m = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]

ans = int(10e9)
bw = del1()
for i, j in bw:
    g[i][j] = '0'
    bfs()
    g[i][j] = '1'
if ans != int(10e9):
    print(ans)
else:
    print(-1)
'''



