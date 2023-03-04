'''
텔레포트 3

위치 xs, ys에서 xe, ye로 이동 예정.
사방이동 or 텔포. 텔포는 고정 10초 사방이동 1초
시작점, 도착점 제시 및 텔포 구간 제시. 가장 빠르게 집 갈 수 있는 시간.
- 크기가 10억까지이고, 벽이 없다는 것을 생각하자!

입력
xs, ys 시작점
xe, ye 제시. 도착점
x1 y1 x2 y2 3번 제시. 텔포

출력
집 가는 가장 빠른 시간
'''
import sys
from heapq import heappop, heappush
from math import inf
input = sys.stdin.readline

def dij():
    dst = [inf]*8
    dst[0] = 0
    heap = [(0, 0)]
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        if nod == 7:
            return cost
        for nnod, co in enumerate(g[nod]):
            if dst[nnod] > cost+co:
                dst[nnod] = cost+co
                heappush(heap, (cost+co, nnod))

sx, sy = map(int, input().rstrip().split())
ex, ey = map(int, input().rstrip().split())
nodz = []
for _ in range(3):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    nodz.append((x1, y1))
    nodz.append((x2, y2))
nodz = [(sx, sy)] + nodz + [(ex, ey)]
# 1,2 3,4 5,6 텔포 가능.
g = [[inf]*8 for _ in range(8)]
for i in [1,3,5]:
    g[i][i+1] = 10
    g[i+1][i] = 10
for i in range(8):
    g[i][i] = 0
    x1, y1 = nodz[i]
    for j in range(i+1, 8):
        x2, y2 = nodz[j]
        cha = abs(x1-x2)+abs(y1-y2)
        if g[i][j] > cha:
            g[i][j], g[j][i] = cha, cha
print(dij())

'''
# 루비의 코드

from math import inf

matrix = [[inf] * 8 for _ in range(8)]
pos = [list(map(int, input().split())) for _ in range(2)]

for i in range(2, 8, 2):
    x1, y1, x2, y2 = map(int, input().split())
    pos.append([x1, y1])
    pos.append([x2, y2])
    matrix[i][i + 1] = matrix[i + 1][i] = 10

for i in range(8):
    matrix[i][i] = 0
    for j in range(i + 1, 8):
        matrix[i][j] = matrix[j][i] = min(matrix[i][j], abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1]))

for k in range(8):
    for i in range(8):
        for j in range(8):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

print(matrix[0][1])
'''

