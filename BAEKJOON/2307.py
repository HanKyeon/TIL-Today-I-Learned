'''
도로검문

주요지점, 도로, 도로는 비용 보유중. 양방향 도로이며 걸리는 시간은 항상 같다.
어떤 범죄 용의자가 입력 데이터에 표시된 도시로 진입하여 도시를 가장 빠른 시간 내에 빠져나가고자 한다. 어떤 하나의 도로를 선택하여 막을 것이다. 용의자는 그 도로를 피해서 가장 빠르게 탈출해야 한다.
이 때, 시간이 늘어날 수 있는데, 지연시간의 최대 시간을 정수로 표현. 무한대일 경우 -1 출력.
지연시간 계산방법
1. 두개의 지점을 직접 연결하는 도로가 있는 경우, 그 도로는 유일하다.
2. 도시의 지점은 1에서 n까지 연속 정수.
3. 용의자가 진입하는 지점은 항상 1번, 최종 탈출지는 n번 지점.
4. 용의자는 검문을 피해 가장 빨리 도시를 빠져나가고자 하고, 경찰은 용의자들의 탈출 시간을 최대한 지연시킬 것이다.
5. 각 도시 지점 간 이동 시간은 항상 양의 정수.
탈출 못하게 되면 -1 출력

입력
지점 갯수 n 간선 수 m 제시. n은 6이상 1000이하, m은 6이상 5000이하
m개 줄 a, b, c 제시. b가 a보다 크며 t는 1이상 10000이하

출력
경찰이 하나의 도로를 막음으로써 지연시킬 수 있는 최대 시간 정수로 출력. 지연시간이 무한대일 경우 -1 출력.
'''
import sys
from math import inf
from heapq import heappop, heappush
input = sys.stdin.readline

def dij(blck:int):
    global n
    dst = [inf] * (n+1)
    dst[1] = 0
    heap = [(0, 1, [])]
    while heap:
        cost, nod, be = heappop(heap)
        if dst[nod] < cost:
            continue
        if nod == n:
            return (cost, be)
        for i in g[nod]:
            co, nnod, enum = i
            if enum == blck:
                continue
            if dst[nnod] < cost+co:
                continue
            dst[nnod] = cost+co
            heappush(heap, (cost+co, nnod, be+[enum]))
    return [dst[nod]]

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for i in range(1, m+1):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b, i))
    g[b].append((c, a, i))
cost, be = dij(-1)
ans = 0
for i in be:
    a = dij(i)
    if len(a) == 1:
        ans = -1
        break
    nco, x = a
    ans = max(ans, nco-cost)
print(ans)

'''
# 가장 빠른 코드

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 10 ** 9


def sol2307():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    distance = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        u, v, d = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
        distance[u][v] = distance[v][u] = d

    # 다익스트라 최단거리 함수
    def dijkstra(short):
        dp = [INF] * (n + 1)
        q = [(0, 1)]
        dp[1] = 0
        while q:
            if dp[n] <= short:
                return -1

            dst, cur = heappop(q)
            if dst > dp[cur]:
                continue

            for nxt in g[cur]:
                ndst = dst + distance[cur][nxt]
                if ndst < dp[nxt]:
                    dp[nxt] = ndst
                    heappush(q, (ndst, nxt))
        return dp[n]

    # 기존 최단경로를 구하기 위한 다익스트라
    trace = [0] * (n + 1)
    dp = [INF] * (n + 1)
    q = [(0, 1)]
    dp[1] = 0
    while q:
        dst, cur = heappop(q)
        if dst > dp[cur]:
            continue

        for nxt in g[cur]:
            ndst = dst + distance[cur][nxt]
            if ndst < dp[nxt]:
                dp[nxt] = ndst
                trace[nxt] = cur
                heappush(q, (ndst, nxt))

    edges = []
    cur = n
    while trace[cur]:
        edges.append((cur, trace[cur]))
        cur = trace[cur]

    # 도로를 하나씩 봉쇄해가며 가장
    delayed = dp[n]
    for u, v in edges:
        d = distance[u][v]
        distance[u][v] = distance[v][u] = INF
        delayed = max(delayed, dijkstra(delayed))
        distance[u][v] = distance[v][u] = d
        if delayed == INF:
            return -1

    return delayed - dp[n]


if __name__ == '__main__':
    print(sol2307())
'''









