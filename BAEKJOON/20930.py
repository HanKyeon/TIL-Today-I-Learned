'''
우주 정거장

우주 정거장은 하나의 선분으로 구성되어 있으며, 좌표 평면 상에 N개의 우주 정거장이 있다.
각 우주 정거장은 1번부터 n번까지 번호가 붙어있다.

비행선은 무조건 우주 정거장에서만 출발 가능하며, 이동하면서 만나는 우주 정거장에서만 멈출 수 있다. 경계도 포함. 우주선은 x축과 평행, y축과 평행, 우주정거장 내에서 이동 가능하다. 서로 다른 두 정거장이 주어졌을 때, 두 정거장 사이를 오갈 수 있는지 알아보자.

입력
우주 정거장 갯수 N과 질문 갯수 Q. 2이상 20만이하 N 1이상 20만이하 Q
양 끝점 xi1 yi1 xi2 yi2 제시. 모든 좌표 절댓값은 1억이하 정수.
문제 제시

출력
각 줄마다 문제 대답. 오갈 수 있다면 1, 그렇지 않다면 0
'''
import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(222222)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    # x, y = find(x), find(y)
    if x < y:
        parent[y] = x
        return x
    else:
        parent[x] = y
        return y

n, q = map(int, input().rstrip().split())
parent = list(range(n+1))
xheap, yheap = [], []
for i in range(1, n+1):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    if x2 < x1:
        x1, x2 = x2, x1
    if y2 < y1:
        y1, y2 = y2, y1
    # x1, y1, x2, y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    xheap.append((x1, x2, i))
    yheap.append((y1, y2, i))
xheap.sort()
yheap.sort()
x1, x2, xidx = xheap[0]
y1, y2, yidx = yheap[0]
for i in range(1, n):
    a1, a2, nxidx = xheap[i]
    nxidx = find(nxidx)
    if xidx == nxidx:
        pass
    elif x1 <= a1 <= x2:
        if a2 > x2:
            x2 = a2
        xidx = union(xidx, nxidx)
    else:
        x1, x2, xidx = a1, a2, nxidx
    
    b1, b2, nyidx = yheap[i]
    nyidx = find(nyidx)
    if yidx == nyidx:
        continue
    if y1 <= b1 <= y2:
        if b2 > y2:
            y2 = b2
        yidx = union(yidx, nyidx)
    else:
        y1, y2, yidx = b1, b2, nyidx

for _ in range(q):
    a, b = map(int, input().rstrip().split())
    if find(a) == find(b):
        print('1\n')
    else:
        print('0\n')



'''
# 메모리 절약
import sys
input = sys.stdin.readline
print = sys.stdout.write

def find(u):
    if u != unionfind[u]:
        unionfind[u] = find(unionfind[u])
    return unionfind[u]
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    unionfind[root2] = root1

n, q = map(int, input().split())
unionfind = [i for i in range(n)]
l = []
for i in range(n):
    a, b, c, d = map(int, input().split())
    l.append([[a, b, c, d], [c, d, a, b]][(a, b) > (c, d)] + [i])
l_x = sorted(l, key = lambda x : (x[0], x[2]))
l_y = sorted(l, key = lambda x : (x[1], x[3]))
px1, _, px2, _, pidx = l_x[0]
for i in range(1, n):
    x1, _, x2, _, idx = l_x[i]
    if px1 <= x1 <= px2:
        union(pidx, idx)
    if x2 >= px2:
        px1, px2, pidx = x1, x2, idx
_, py1, _, py2, pidx = l_y[0]
for i in range(1, n):
    _, y1, _, y2, idx = l_y[i]
    if py1 <= y1 <= py2:
        if find(pidx) != find(idx): union(pidx, idx)
    if y2 >= py2:
        py1, py2, pidx = y1, y2, idx
for _ in range(q):
    a, b = map(int, input().split())
    print(f"{int(find(a-1) == find(b-1))}\n")
'''






'''
# 시간 초과
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10**9)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    # x, y = find(x), find(y)
    if x == y:
        return x
    if x < y:
        parent[y] = x
        return x
    else:
        parent[x] = y
        return y

n, q = map(int, input().rstrip().split())
parent = list(range(n+1))
xheap, yheap = [], []
for i in range(1, n+1):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    x1, y1, x2, y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    heappush(xheap, (x1, x2, i))
    heappush(yheap, (y1, y2, i))

x1, x2, xidx = heappop(xheap)
while xheap:
    a1, a2, nxidx = heappop(xheap)
    # if find(xidx) == find(nxidx):
    #     continue
    if x1 <= a1 <= x2:
        if a2 > x2:
            x2 = a2
        xidx = union(xidx, nxidx)
    else:
        x1, x2, xidx = a1, a2, nxidx

y1, y2, yidx = heappop(yheap)
yidx = find(yidx)
while yheap:
    b1, b2, nyidx = heappop(yheap)
    nyidx = find(nyidx)
    if yidx == nyidx:
        continue
    if y1 <= b1 <= y2:
        if b2 > y2:
            y2 = b2
        yidx = union(yidx, nyidx)
    else:
        y1, y2, yidx = b1, b2, find(nyidx)

for _ in range(q):
    a, b = map(int, input().rstrip().split())
    if find(a) == find(b):
        print('1\n')
    else:
        print('0\n')
'''





