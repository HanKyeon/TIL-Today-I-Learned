'''
집 구하기

맥세권 : 맥도날드와 집 사이 최단 거리가 x 이하인 집
스세권 : 스벅과 집 사이 최단 거리가 y 이하인 집
맥세권과 스세권 집 중 최단거리 합이 최소인 집

그래프로 제시. 맥날 스벅 위치가 정점 번호로 제시.
원하는 집의 최단거리 합 출력.

입력
정점 갯수 n, 도로 갯수 m 제시. 1만 30만.
E개줄 a, b, c 제시.
맥날 수 mdn, 맥세권 거리 x
mdn개 맥날 정점 번호.
스벅 수 stb, 스세권 거리 y 제시.
stb개 스벅 정점 번호
맥날/스벅 위치에는 집이 없다.
한 정점에 맥날 스벅 함께 없다.

출력
최단거리 합 출력.
집 없으면 -1 출력.
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
M = int(10e9)
def dij(li:list, mval:int)->list:
    global n
    dst = [M]*(n+1)
    heap = []
    nodc = n
    while li:
        nod = li.pop()
        heappush(heap, (0, nod))
        dst[nod] = 0
    while heap and nodc:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        nodc -= 1
        for co, nnod in g[nod]:
            costco = cost+co
            if costco > mval:
                continue
            if dst[nnod] > costco:
                dst[nnod] = costco
                heappush(heap, (costco, nnod))
    return dst

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
    g[b].append((c, a))
mdn, x = map(int, input().rstrip().split())
mdnli = list(map(int, input().rstrip().split()))
stb, y = map(int, input().rstrip().split())
stbli = list(map(int, input().rstrip().split()))

md = dij(mdnli, x)
sb = dij(stbli, y)
ans = M
for i in range(1, n+1):
    mdd, sbd = md[i], sb[i]
    if mdd == M or sbd == M or not mdd or not sbd:
        continue
    ans = min(ans, mdd+sbd)
if ans == M:
    ans = -1
print(ans)





