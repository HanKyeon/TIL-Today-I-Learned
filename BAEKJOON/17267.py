'''
상남자

영조는 상남자라 위아래로만 간다. 위아래 자유 이동. 좌우 이동 x. 보성이가 밀어서 왼쪽으로 최대 L번 오른쪽으로 최대 R번 이동  가능. 지도 밖으로 안나감.
갈 수 있는 땅, 벽의 위치, 영조보성 출발 위치가 지도 정보로 제시 되었을 때, 영조와 보성이가 출발 위치로부터 이동해서 갈 수 있는 모든 땅의 갯수.

입력
n, m  제시.
좌우 이동 가능 횟수 l, r 제시.
n 개줄 그래프 제시.

출력
시작 위치를 포함하여 갈 수 있는 땅의 갯수 출력
'''
import sys
from collections import deque
from heapq import heappop, heappush
input = sys.stdin.readline

# def bfs():
#     global sh, sw, l, r, n, m
#     g[sh][sw] = '0'
#     v[sh][sw] = 0
#     heap = [(0, sh, sw, l, r)]
#     cnt = 0
#     while heap:
#         odr, h, w, lft, rgt = heappop(heap)
#         cnt += 1
#         for dh in (1, -1):
#             nh = h+dh
#             if 0<=nh<n and v[nh][w] < 0 and g[nh][w] == '0':
#                 v[nh][w] = odr
#                 heappush(heap, (odr, nh, w, lft, rgt))
#         if lft:
#             nw = w-1
#             if 0<=nw<m and v[h][nw] < 0 and g[h][nw] == '0':
#                 v[h][nw] = odr+1
#                 heappush(heap, (odr+1, h, nw, lft-1, rgt))
#         if rgt:
#             nw = w+1
#             if 0<=nw<m and v[h][nw] < 0 and g[h][nw] == '0':
#                 v[h][nw] = odr+1
#                 heappush(heap, (odr+1, h, nw, lft, rgt-1))
#     return cnt

def bfs2():
    global sh, sw, l, r, n, m
    g[sh][sw] = '0'
    v[sh][sw] = 1
    q = deque([(sh, sw, l, r)])
    cnt = 0
    while q:
        h, w, lft, rgt = q.popleft()
        cnt += 1
        for dh in (-1, 1):
            nh = h+dh
            if 0<=nh<n and not v[nh][w] and g[nh][w] == '0':
                v[nh][w] = 1
                q.append((nh, w, lft, rgt))
        if lft:
            nw = w-1
            if 0<=nw<m and not v[h][nw] and g[h][nw] == '0':
                v[h][nw] = 1
                q.append((h, nw, lft-1, rgt))
        if rgt:
            nw = w+1
            if 0<=nw<m and not v[h][nw] and g[h][nw] == '0':
                v[h][nw] = 1
                q.append((h, nw, lft, rgt-1))
    return cnt

n, m = map(int, input().rstrip().split())
l, r = map(int, input().rstrip().split())
v = [[0]*m for _ in range(n)]
g = []
for i in range(n):
    s = input().rstrip()
    for j in range(m):
        if s[j] == '2':
            sh, sw = i, j
    g.append(list(s))
print(bfs2())

import sys
# from collections import deque
from heapq import heappop, heappush
input = sys.stdin.readline

def bfs():
    global sh, sw, l, r, n, m
    g[sh][sw] = '0'
    v[sh][sw] = 0
    heap = [(0, sh, sw, l, r)]
    cnt = 0
    while heap:
        odr, h, w, lft, rgt = heappop(heap)
        cnt += 1
        for dh in (1, -1):
            nh = h+dh
            if 0<=nh<n and v[nh][w] < 0 and g[nh][w] == '0':
                v[nh][w] = odr
                heappush(heap, (odr, nh, w, lft, rgt))
        if lft:
            nw = w-1
            if 0<=nw<m and v[h][nw] < 0 and g[h][nw] == '0':
                v[h][nw] = odr+1
                heappush(heap, (odr+1, h, nw, lft-1, rgt))
        if rgt:
            nw = w+1
            if 0<=nw<m and v[h][nw] < 0 and g[h][nw] == '0':
                v[h][nw] = odr+1
                heappush(heap, (odr+1, h, nw, lft, rgt-1))
    return cnt            



n, m = map(int, input().rstrip().split())
l, r = map(int, input().rstrip().split())
v = [[-1]*m for _ in range(n)]
g = []
for i in range(n):
    s = input().rstrip()
    for j in range(m):
        if s[j] == '2':
            sh, sw = i, j
    g.append(list(s))

print(bfs())

'''
# 빠른 천재의 코드

"""
17267 상남자
"""
import sys
from collections import deque
input = sys.stdin.readline

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, input().split())
left, right = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x, start_y = i, j
q = deque()
q.append((start_x, start_y, left, right))
visited[start_x][start_y] = True
ans = 0
while q:
    x, y, l, r = q.popleft()
    ans += 1
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visited[nx][ny]:
            continue
        if graph[nx][ny] == 1:
            continue
        if dx in (1, -1):
            visited[nx][ny] = True
            q.appendleft((nx, ny, l, r))
        elif dy == -1:
            if l >= 1:
                visited[nx][ny] = True
                q.append((nx, ny, l - 1, r))
        elif dy == 1:
            if r >= 1:
                visited[nx][ny] = True
                q.append((nx, ny, l, r - 1))
print(ans)
'''
'''
# 원큐 패스 힙큐 스타일

import sys
# from collections import deque
from heapq import heappop, heappush
input = sys.stdin.readline

def bfs():
    global sh, sw, l, r, n, m
    g[sh][sw] = '0'
    v[sh][sw] = 0
    heap = [(0, sh, sw, l, r)]
    cnt = 0
    while heap:
        odr, h, w, lft, rgt = heappop(heap)
        cnt += 1
        for dh in (1, -1):
            nh = h+dh
            if 0<=nh<n and v[nh][w] < 0 and g[nh][w] == '0':
                v[nh][w] = odr
                heappush(heap, (odr, nh, w, lft, rgt))
        if lft:
            nw = w-1
            if 0<=nw<m and v[h][nw] < 0 and g[h][nw] == '0':
                v[h][nw] = odr+1
                heappush(heap, (odr+1, h, nw, lft-1, rgt))
        if rgt:
            nw = w+1
            if 0<=nw<m and v[h][nw] < 0 and g[h][nw] == '0':
                v[h][nw] = odr+1
                heappush(heap, (odr+1, h, nw, lft, rgt-1))
    return cnt

n, m = map(int, input().rstrip().split())
l, r = map(int, input().rstrip().split())
v = [[-1]*m for _ in range(n)]
g = []
for i in range(n):
    s = input().rstrip()
    for j in range(m):
        if s[j] == '2':
            sh, sw = i, j
    g.append(list(s))

print(bfs())
'''

