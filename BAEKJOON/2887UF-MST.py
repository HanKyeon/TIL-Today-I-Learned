'''
행성 터널

n개의 행성. 터널 만들 것. 최소값.
두 행성 x1 y1 z1, x2 y2 z2를 만들 때 비용은 차이 절댓값 중 최솟값.
min(abs(x1-x2), abs(y1-y2), abs(z1-z2))
터널 n-1개 지을 예정. 최소비용 제시.

입력
행성 갯수 n 제시.
행성의 x, y, z 제시. -1억이상 1억이하.

출력
최소비용 출력
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find해서 넣기
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def findlength(x, y):
    x1, y1, z1 = pinfo[x]
    x2, y2, z2 = pinfo[y]
    return min(abs(x1-x2), abs(y1-y2), abs(z1-z2))

n = int(input())
parent = list(range(n+1))
pinfo = [[]]
xl, yl, zl = [], [], []
for i in range(1, n+1):
    x, y, z = map(int, input().rstrip().split())
    xl.append((x, i))
    yl.append((y, i))
    zl.append((z, i))
    pinfo.append([x, y, z])
xl.sort()
yl.sort()
zl.sort()

willSort = []
for i in range(1, n):
    p1, p2 = xl[i][1], xl[i-1][1]
    p3, p4 = yl[i][1], yl[i-1][1]
    p5, p6 = zl[i][1], zl[i-1][1]
    willSort.append((-findlength(p1, p2), p1, p2))
    willSort.append((-findlength(p3, p4), p3, p4))
    willSort.append((-findlength(p5, p6), p5, p6))
del xl, yl, zl

willSort.sort()

ans = 0
while willSort:
    ml, p1, p2 = willSort.pop()
    p1, p2 = find(p1), find(p2)
    if p1 == p2:
        continue
    union(p1, p2)
    ans += ml

print(-ans)




'''
import sys


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n = int(sys.stdin.readline())
planets = []
parent = [_ for _ in range(n)]

for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    planets.append((i, x, y, z))

x_sort = sorted(planets, key=lambda x: x[1])
y_sort = sorted(planets, key=lambda x: x[2])
z_sort = sorted(planets, key=lambda x: x[3])

edgs = []
# a 행성에서 a+1 행성으로 x 축으로 이동하는 간선, 비용
for a in range(n - 1):
    edge = (abs(x_sort[a + 1][1] - x_sort[a][1]), x_sort[a][0], x_sort[a + 1][0])
    edgs.append(edge)

# a 행성에서 a+1 행성으로 y 축으로 이동하는 간선, 비용
for a in range(n - 1):
    edge = (abs(y_sort[a + 1][2] - y_sort[a][2]), y_sort[a][0], y_sort[a + 1][0])
    edgs.append(edge)

# a 행성에서 a+1 행성으로 z 축으로 이동하는 간선, 비용
for a in range(n - 1):
    edge = (abs(z_sort[a + 1][3] - z_sort[a][3]), z_sort[a][0], z_sort[a + 1][0])
    edgs.append(edge)

# 간선들 거리순 정렬
edgs.sort(key=lambda x: x[0])

answer = 0
for cost, a, b in edgs:
    if find(a) != find(b):
        union(a, b)
        answer += cost

print(answer)
'''











