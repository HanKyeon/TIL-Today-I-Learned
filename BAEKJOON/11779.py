'''
최소비용 구하기2

1이상 1000이하 도시 존재. 한 도시 출발 다른 도시 도착 1이상 10만이하 버스 존재.
A에서 B로 가는 비용 최소화. A번째 도시에서 B번째 도시까지 가는데 드는 최소비용과 경로를 출력해라.
항상 시작점에서 도착점으로의 경로가 존재.

입력
도시 갯수 1이상 1000이하 n 제시.
버스 갯수 1이상 10만이하 m 제시.
출발지 도착지 비용 m번 제시
출발점 도착점

출력
최소비용
경로 갯수
도시 루트
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dij(fst, tg): # 다익스트라
    global n
    dst = [[int(10e9), []] for _ in range(n+1)] # 거리인데 오는 루트도 기록 할 것.
    dst[fst] = [0, [fst]] # 시작 점 초기화
    heap = [[0, fst, [fst]]]
    while heap:
        cost, idx, roots = heappop(heap)
        if dst[idx][0] < cost:
            continue
        for i in g[idx]:
            co, mj = i
            if cost + co < dst[mj][0]:
                dst[mj][0] = cost + co
                dst[mj][1] = roots + [mj]
                heappush(heap, [cost+co, mj,  dst[mj][1]])
    return dst[tg]

n, m = int(input()), int(input())
g =  [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
sta, end = map(int, input().rstrip().split())
ans = dij(sta, end)
print(ans[0])
print(len(ans[1]))
print(*ans[1])


'''
# 빠른 코드
from collections import defaultdict
from heapq import heappop, heappush
from sys import stdin, maxsize

input = stdin.readline
INF = maxsize

nodes = int(input())
buses = int(input())

graph = defaultdict(list)

for _ in range(buses):
    fr, to, cost = map(int, input().split())
    graph[fr].append((to, cost))

fr, to = map(int, input().split())

# 경유, 비용
dists = [INF]*(nodes+1)
paths = [i for i in range(nodes+1)]
dists[fr] = 0
queue = [(0, fr, 1)]

while queue:
    cost_sum, node, been = heappop(queue)
    if node == to:
        break

    for city, cost in graph[node]:
        if dists[city] > cost+cost_sum:
            dists[city] = cost+cost_sum
            paths[city] = node
            heappush(queue, (cost+cost_sum, city, been+1, ))

# been이 갯수, cost_sum이 최소 비용

node = to
cities_been = [to]
while paths[node] != node:
    cities_been.append(paths[node])
    node = paths[node]
    pass

print(cost_sum)
print(been)
print(*reversed(cities_been))
'''
