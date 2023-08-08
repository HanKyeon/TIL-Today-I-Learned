'''
소수 마을

가고 싶은 위치까지의 거리가 소수일 경우에만 간다.
즉시 가는 거리가 소수가 아닐 경우 경유해서 가야 한다.
소수 마을과 경유 가능한 마을들, 좌표로 위치 제시.
규칙 준수하며 A로 갈 수 있는 최단 거리. 마을간의 거리는 정수 부분만 취급한다.

입력
x1 y1 x2 y2 제시
경유 가능한 마을 갯수 n 제시
n개 줄 경유 가능한 마을 위치 제시

출력
규칙 준수하며 A마을까지 가는 방법 중 가장 짧은 거리로 갈 수 있는 거리 합 출력. 방법이 없을 경우 -1 출력
'''
import sys
from heapq import heappop, heappush
from math import sqrt
input = sys.stdin.readline

def check(sh, sw, eh, ew):
    return int(sqrt((sh-eh)**2 + (sw-ew)**2))

def dij():
    global n
    dst = [0] + [8888]*(n+1)
    heap = [(0, 0)]
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        if nod == n+1:
            return cost
        for i, co in enumerate(g[nod]): 
            if not co:
                continue
            if dst[i] > cost+co:
                dst[i] = cost+co
                heappush(heap, (cost+co, i))
    return -1

che = set()
sosu = [0,0]+[1]*8886
for i in range(2, 8888):
    if not sosu[i]:
        continue
    che.add(i)
    k = 1
    while i*k+i < 8887:
        if sosu[i*k+i]:
            sosu[i*k+i] = 0
        k+=1

x1, y1, x2, y2 = map(int, input().rstrip().split())
n = int(input())
nodz = [(x1, y1)] + [tuple(map(int, input().rstrip().split())) for _ in range(n)] + [(x2, y2)]
g = [[0]*(n+2) for _ in range(n+2)]
for i in range(n+2):
    a1, b1 = nodz[i]
    for j in range(i+1, n+2):
        a2, b2 = nodz[j]
        dst = check(a1, b1, a2, b2)
        if dst in che:
            g[i][j], g[j][i] = dst, dst

print(dij())
