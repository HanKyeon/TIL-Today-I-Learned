'''
A도시 E개 방향성 그래프.
0번부터 n번까지 번호.
0번에서 n까지 최소 거리 출력 모든 지점 거칠 필요 x

입력
테케T
n, m 제시
m개줄에 출발 도착 비용 제시.

출력
#테케 최소거리
'''
from heapq import heappop, heappush

def dij():
    global n
    dst = [int(10e9)]*(n+1)
    dst[0] = 0
    heap = [(0, 0)]
    while heap:
        cost, nod = heappop(heap)
        if nod == n:
            return cost
        if dst[nod] < cost:
            continue
        for co, nnod in g[nod]:
            if dst[nnod] > cost+co:
                dst[nnod] = cost+co
                heappush(heap, (cost+co, nnod))
    return dst[-1]

for tc in range(1, int(input())+1):
    n, m = map(int,input().rstrip().split())
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().rstrip().split())
        g[a].append((c, b))
    print(f"#{tc} {dij()}")
