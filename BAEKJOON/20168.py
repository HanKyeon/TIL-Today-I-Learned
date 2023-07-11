'''
골목대장 호석 - 기능성

n개 교차로 m개 골목. 1부터 n번. 두 교차로 간선은 최대 1개
A번에서 B까지 c원을 가지고 갈 것.
최소의 수치심. 경로 상에서 가장 많이 낸 돈에 비례. 한 골목에서 가장 높게 내는 값을 최소화 하려함.
가진 돈으로 절대 갈 수 없다면 -1 출력.

입력
n, m, a, b, c 제시.
m개 줄 교차로 정보 제시.

출력
c원 이하로 가는 경로 중 지나는 골목의 요금의 최댓값의 최솟값 출력. 갈 수 없다면 -1
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dij():
    global n, m, a, b, c
    heap = [(0, 0, a)]
    dst = [10001]*(n+1)
    dst[a] = 0
    while heap:
        mco, cost, nod = heappop(heap)
        if dst[nod] < mco:
            continue
        if nod == b:
            return mco
        for co, nnod in g[nod]:
            nco = mco if mco >= co else co
            if dst[nnod] > nco and cost+co <= c:
                dst[nnod] = nco
                heappush(heap, (nco, cost+co, nnod))
    return -1

n, m, a, b, c = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, co = map(int, input().rstrip().split())
    g[x].append((co, y))
    g[y].append((co, x))
print(dij())