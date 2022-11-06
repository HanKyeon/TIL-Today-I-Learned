'''
배열에서 이동

n*n 배열 존재. 1,1에서 n,n까지 이동 예정. 상하좌우 이동.
배열에서 몇개의 수를 거쳐 이동하게 되는데, 거쳐간 수들 중 최댓값과 최솟값의 차이가 가장 작아지는 경우를 구하는 프로그램 작성.

입려ㅓㄱ
n 제시.
배열 제시

출력
최대-최소가 최소인 값 출력

    "python.jediEnabled": true,
    "python.defaultInterpreterPath": "C:\\Users\\hgh72\\AppData\\Local\\Programs\\Python\\Python310\\python.exe",
    // "python.pythonPath": "C:\\Users\\hgh72\\AppData\\Local\\Programs\\Python\\Python310\\python.exe",
    "python.autoComplete.addBrackets": true,
    "python.languageServer": "Pylance",
    '''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

mov = [(-1,0),(0,1),(1,0),(0,-1)]

def dij():
    global n
    v = [[int(10e9)]*n for _ in range(n)]
    v[0][0] = 0
    heap = [(0, g[0][0], g[0][0], 0, 0)]
    while heap:
        cha, lt, bg, h, w = heappop(heap)
        if v[h][w] < cha:
            continue
        if h==n-1 and w==n-1:
            # for i in v:
            #     print(i)
            return cha
        for dh ,dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<n:
                val = g[nh][nw]
                if lt<=val<=bg:
                    if v[nh][nw] > cha:
                        v[nh][nw] = cha
                        heappush(heap, (cha, lt, bg, nh, nw))
                elif val < lt:
                    if v[nh][nw] > bg-val:
                        v[nh][nw] = bg-val
                        heappush(heap, (bg-val, val, bg, nh, nw))
                elif val > bg:
                    if v[nh][nw] > val-lt:
                        v[nh][nw] = val-lt
                        heappush(heap, (val-lt, lt, val, nh, nw))

n = int(input())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
print(dij())



'''
다익스트라 반례
3
2 4 9
1 2 2
9 2 4

def dij():
    global n
    v = [[int(10e9)]*n for _ in range(n)]
    v[0][0] = 0
    heap = [(0, g[0][0], g[0][0], 0, 0)]
    while heap:
        cha, lt, bg, h, w = heappop(heap)
        if v[h][w] < cha:
            continue
        if h==n-1 and w==n-1:
            # for i in v:
            #     print(i)
            return cha
        for dh ,dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<n:
                val = g[nh][nw]
                if lt<=val<=bg:
                    if v[nh][nw] > cha:
                        v[nh][nw] = cha
                        heappush(heap, (cha, lt, bg, nh, nw))
                elif val < lt:
                    if v[nh][nw] > bg-val:
                        v[nh][nw] = bg-val
                        heappush(heap, (bg-val, val, bg, nh, nw))
                elif val > bg:
                    if v[nh][nw] > val-lt:
                        v[nh][nw] = val-lt
                        heappush(heap, (val-lt, lt, val, nh, nw))
'''
'''
from collections import deque
import sys

input = sys.stdin.readline
dh = [1, -1, 0, 0]
dw = [0, 0, 1, -1]

def bfs():
    q = deque()
    c = [[0]*n for _ in range(n)]
    q.append([0, 0])
    c[0][0] = 1
    while q:
        h, w = q.popleft()
        if h == n-1 and w == n-1:
            return 1
        for i in range(4):
            nx = h + dh[i]
            ny = w + dw[i]
            if 0 <= nx < n and 0 <= ny < n:
                if ll <= a[nx][ny] <= rr and not c[nx][ny]:
                    c[nx][ny] = 1
                    q.append([nx, ny])
    return 0

n = int(input())

a, rM, lm = [], 0, sys.maxsize
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    lm = min(lm, min(row))
    rM = max(rM, max(row))

lM = min(a[0][0], a[n-1][n-1])
rm = max(a[0][0], a[n-1][n-1])

ll, rr = lm, rm
ans = sys.maxsize
while lm <= ll <= lM and rm <= rr <= rM:
    lf, rf = 0, 0
    if bfs():
        ans = min(ans, rr - ll)
        ll += 1
        lf = 1
    else:
        if lf and rf:
            ll += 1
            rr += 1
        else:
            rr += 1
            rf = 1
print(ans)
'''