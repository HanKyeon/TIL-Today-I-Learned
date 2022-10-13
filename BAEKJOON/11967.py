'''
불켜기

n*n 헛간. 1,1에서 n,n 2이상
많은 방에 불을 밝힐 것. 1,1 출발.
어떤 방에는 다른 방의 불을 끄고 켤 수 있는 스위치 존재. 1,1 스위치로 1,2 불 조절 가능. 불이 켜져있는 방으로만 이동 가능. 상하좌우 이동.
불을 켤 수 있는 방 최대 갯수

입력
n, m 제시.
m개 줄 스위치 제시. x, y, a, b. x,y 방에서 a,b 방의 불 스위치 존재. 한 방에 여러개의 스위치 존재 가능, 하나의 불을 조절하는 스위치 역시 여러개 있을 수 있음.

출력
불을 켤 수 있는 최대 방의 갯수.
'''
from collections import deque
import sys
input = sys.stdin.readline

mov = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n, m = map(int, input().rstrip().split())
swch = {}
for _ in range(m):
    x, y, a, b = map(int, input().rstrip().split())
    x, y, a, b = x-1, y-1, a-1, b-1
    if swch.get((x, y), 0):
        swch[(x, y)].append((a, b))
    else:
        swch[(x, y)] = [(a, b)]
q = deque([(0, 0)])
g = [[0]*n for _ in range(n)]
v = [[0]*n for _ in range(n)]
g[0][0] = 1
v[0][0] = 1
ans = 1
def bfs():
    global ans, q
    fla = False
    nq = set()
    while q:
        h, w = q.popleft()
        if swch.get((h, w), 0):
            for x, y in swch[(h, w)]:
                if g[x][y]:
                    continue
                g[x][y] = 1
                ans += 1
                fla = True
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<n and g[nh][nw] and not v[nh][nw]:
                v[nh][nw] = 1
                q.append((nh, nw))
            else:
                nq.add((h, w))
    q = deque(list(nq))
    return fla
a = bfs()
while a:
    a = bfs()
print(ans)

'''
# 빠른 코드

import sys
read = sys.stdin.readline
n, m = map(int, read().split())
arr1 = [[[] for _ in range(n)] for _ in range(n)]
arr2 = [[False] * n for _ in range(n)]
arr2[0][0] = True
for _ in range(m):
    a, b, c, d = map(int, read().split())
    arr1[a-1][b-1].append((c-1, d-1))
def dist(a, b):
    yield a+1,b
    yield a-1,b
    yield a,b+1
    yield a,b-1
q = [(0, 0)]
ans = 1
arr3 = [[0] * n for _ in range(n)]
arr3[0][0] = 2
while q:
    tmp = []
    for x, y in q:
        for i, j in arr1[x][y]:
            if not arr2[i][j]:
                arr2[i][j] = True
                ans += 1
            if arr3[i][j] == 1:
                tmp.append((i, j))
                arr3[i][j] = 2
        for xx, yy in dist(x, y):
            if -1 < xx < n and -1 < yy < n and arr3[xx][yy] == 0:
                if arr2[xx][yy]:
                    arr3[xx][yy] = 2
                    tmp.append((xx, yy))
                else:
                    arr3[xx][yy] = 1
    q = tmp
print(ans)
'''




