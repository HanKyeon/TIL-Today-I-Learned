'''
탈옥

상근이는 죄수 두 명 탈옥시켜야 한다.
문을 최소한으로 열어서 탈주 시킬 때 문의 갯수 구해라

입력
테케T
h, w  제시. 2이상 100이하
빈 공간 .
벽 *
문 #
죄수 $

죄수는 항상 둘. 경로 항상 존재.

출력
열어야 하는 문의 최솟값
'''
import sys
from collections import deque
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]
# bfs 하면서 각 dep에 bfs 처리
def bfs(ph, pw, dep):
    global n, m
    q = deque([(ph, pw)])
    v[ph][pw][dep] = 0
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m:
                if v[nh][nw][dep] < 0:
                    if g[nh][nw] == '.':
                        v[nh][nw][dep] = v[h][w][dep]
                        q.appendleft([nh, nw])
                    elif g[nh][nw] == '#':
                        v[nh][nw][dep] = v[h][w][dep] + 1
                        q.append([nh, nw])

for _ in range(int(input())):
    n, m = map(int, input().split())
    g = [['.']*(m+2)] + [['.']+list(input().strip())+['.'] for _ in range(n)] + [['.']*(m+2)]
    n, m = n+2, m+2
    v = [[[-1000000, -1000000, -1000000] for _ in range(m)] for _ in range(n)]
    js = [(0, 0)]
    for i in range(n):
        for j in range(m):
            if g[i][j] == '$':
                js.append((i, j))
                g[i][j] = '.'
    # 밖, 죄수1, 죄수2 bfs
    for i in range(3):
        h, w = js.pop()
        bfs(h, w, i)

    ans = int(10e9)
    for i in range(n):
        for j in range(m):
            fla = sum(v[i][j])
            if fla < 0:
                continue
            if g[i][j] == '#':
                fla-=2
            if ans > fla:
                ans = fla
    print(ans)




'''
# 전부 열쇠인 경우를 생각하지 못한 바보가 나다!
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]

def dij():
    global n, m
    v = [[[1000000, 1000000] for _ in range(m)] for _ in range(n)]
    di0, di1 = {}, {}
    heap = []
    h, w = js.pop()
    v[h][w][0] = 0
    heappush(heap, (0, h, w, 0, []))
    h, w = js.pop()
    v[h][w][1] = 0
    heappush(heap, (0, h, w, 1, []))
    while heap:
        brkdr, h, w, num, li = heappop(heap)
        if v[h][w][num] < brkdr:
            continue
        if h == 0 or w == 0 or h == n-1 or w == m-1:
            if num:
                if di1.get((h, w), 0) == 0:
                    di1[(h, w)] = set(li[:])
            else:
                if di0.get((h, w), 0) == 0:
                    di0[(h, w)] = set(li[:])
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and g[nh][nw] == '.':
                if v[nh][nw][num] > brkdr:
                    v[nh][nw][num] = brkdr
                    heappush(heap, (brkdr, nh, nw, num, li[:]))
            if 0<=nh<n and 0<=nw<m and g[nh][nw] == '#':
                if v[nh][nw][num] > brkdr+1:
                    v[nh][nw][num] = brkdr+1
                    heappush(heap, (brkdr+1, nh, nw, num, li[:]+[(nh, nw)]))
    zmin, omin, dmin = {i for i in range(10000)}, {i for i in range(10000)}, {i for i in range(10000)}
    for h, w in di0:
        if len(zmin) > len(di0[(h, w)]):
            zmin = set()
            for iii in di0[(h, w)]:
                zmin.add(iii)
        if v[h][w][1] != 1000000 and v[h][w][0] != 1000000:
            imsi = set()
            for iii in di0[(h, w)]:
                imsi.add(iii)
            for iii in di1[(h, w)]:
                imsi.add(iii)
            if len(imsi) < len(dmin):
                dmin = set()
                for iii in imsi:
                    dmin.add(iii)
    for h, w in di1:
        if len(omin) > len(di1[(h, w)]):
            omin = set()
            for iii in di1[(h, w)]:
                omin.add(iii)
    zmin.update(omin)
    return min(len(zmin), len(dmin))

for _ in range(int(input())):
    n, m = map(int, input().rstrip().split())
    g = [list(input().rstrip()) for _ in range(n)]
    js = []
    for i in range(n):
        for j in range(m):
            if g[i][j] == '$':
                js.append((i, j))
                g[i][j] = '.'
    print(dij())
'''
'''
5
5 5
**#**
*###*
#$.$#
*###*
*****
5 5
****#
*$..#
*...*
*$..*
*****
7 11
***********
*.........*
*.*.*.....*
#.*.*.....*
*#*#*.....*
*$.$#.....*
***********
9 13
.....#*****#*
.....#**#**#*
.....#**#**#*
.....#**.**#*
.....#*#.#*#*
....#$##*##$*
.....#*****#*
....###.#.#.*
.....********
9 9
*********
#######$*
*....****
*.......*
##......#
*.......*
*....****
#######$*
*********
'''

'''
for h, w in di0:
        if len(zmin) > len(di0[(h, w)]):
            zmin = set()
            for iii in di0[(h, w)]:
                zmin.add(iii)
        if v[h][w][1] != 1000000:
            imsi = set()
            for iii in di0[(h, w)]:
                imsi.add(iii)
            for iii in di1[(h, w)]:
                imsi.add(iii)
            if len(imsi) < len(dmin):
                dmin = set()
                for iii in imsi:
                    dmin.add(iii)
    for h, w in di1:
        if len(omin) > len(di1[(h, w)]):
            omin = set()
            for iii in di1[(h, w)]:
                omin.add(iii)
        if v[h][w][0] != 1000000:
            imsi = set()
            for iii in di0[(h, w)]:
                imsi.add(iii)
            for iii in di1[(h, w)]:
                imsi.add(iii)
            if len(imsi) < len(dmin):
                dmin = set()
                for iii in imsi:
                    dmin.add(iii)
# 폐기

def dij():
    global n, m
    v = [[[10001, 10001] for _ in range(m)] for _ in range(n)]
    heap = []
    h, w = js.pop()
    v[h][w][0] = 0
    heappush(heap, (0, h, w, 0, []))
    h, w = js.pop()
    v[h][w][1] = 0
    heappush(heap, (0, h, w, 1, []))
    while heap:
        brkdr, h, w, num, li = heappop(heap)
        if v[h][w][num] < brkdr:
            continue
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and g[nh][nw] == '.':
                if v[nh][nw][num] > brkdr:
                    v[nh][nw][num] = brkdr
                    heappush(heap, (brkdr, nh, nw, num, li))
            if 0<=nh<n and 0<=nw<m and g[nh][nw] == '#':
                if v[nh][nw][num] > brkdr+1:
                    v[nh][nw][num] = brkdr+1
                    heappush(heap, (brkdr+1, nh, nw, num, li+[(nh, nw)]))
    for j in v:
        print(j)
    print('===')




    print(len(zmin), len(omin), len(dmin))
    print(f"di0")
    for i in di0:
        print(f"{i} {len(di0[i])} : {di0[i]}")
    print(f"di1")
    for i in di1:
        print(f"{i} {len(di1[i])} : {di1[i]}")
    print('===')





    zmin, omin, dmin = set(), set(), set()
    for i in range(n):
        for j in (0, m-1):
            if g[i][j] == '*':
                continue
            if v[i][j][0] != 10001:
                if len(zmin) > v[i][j][0]:
                    zmin = di0[(i, j)]
                if v[i][j][1] != 10001:
                    imsi = di0[(i, j)]
                    for vv in di1[(i, j)]:
                        imsi.add(vv)
                    if len(imsi) < len(dmin):
                        dmin = imsi
            if v[i][j][1] != 10001:
                if len(omin) > v[i][j][1]:
                    omin = di1[(i, j)]
                if v[i][j][0] != 10001:
                    imsi = di1[(i, j)]
                    for vv in di0[(i, j)]:
                        imsi.add(vv)
                    if len(imsi) < len(dmin):
                        dmin = imsi
    for i in (0, n-1):
        for j in range(m):
            if g[i][j] == '*':
                continue
            if v[i][j][0] != 10001:
                if len(zmin) > v[i][j][0]:
                    zmin = di0[(i, j)]
                if v[i][j][1] != 10001:
                    imsi = di0[(i, j)]
                    for vv in di1[(i, j)]:
                        imsi.add(vv)
                    if len(imsi) < len(dmin):
                        dmin = imsi
            if v[i][j][1] != 10001:
                if len(omin) > v[i][j][1]:
                    omin = di1[(i, j)]
                if v[i][j][0] != 10001:
                    imsi = di1[(i, j)]
                    for vv in di0[(i, j)]:
                        imsi.add(vv)
                    if len(imsi) < len(dmin):
                        dmin = imsi
'''