'''
무엇을 아느냐가 아니라 누구를 아느냐가 문제다.

최측1 측2 비3 지4 적은 없음.
인맥 간 친밀도 합 최소화.
n명의 정치인 명단에 인맥 친밀도 제시. 최고의원을 만나기까지 친밀도 합 중 가장 작은 값.

입력
테케T 제시.
n, m 제시.
n개 줄 a, b, c 제시.
0은 본인, m-1은 최고의원

출력
f"Case #{tc}: {ans}"
ans는 만난 순서
못가면 -1
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dij(best:int) -> list:
    dst[0] = 0
    heap = [(0, 0, [0])]
    while heap:
        cost, nod, route = heappop(heap)
        if nod == best:
            return route
        if dst[nod] < cost:
            continue
        for co, nnod in g[nod]:
            costco = cost+co
            if costco < dst[nnod]:
                dst[nnod] = costco
                heappush(heap, (costco, nnod, route[:]+[nnod]))
    return [-1]

for tc in range(1, int(input())+1):
    n, m = map(int, input().rstrip().split())
    g, dst= [[] for _ in range(m)], [int(10e9)] * m
    for _ in range(n):
        a, b, c = map(int, input().rstrip().split())
        g[a].append((c, b))
        g[b].append((c, a))
    print(f"Case #{tc}: ", end="")
    print(*dij(m-1))


















