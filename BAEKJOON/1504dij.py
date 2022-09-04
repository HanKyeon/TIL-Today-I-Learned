'''
특정한 최단 경로

방향성이 없는 그래프 제시. 1번 노드에서 n번 노드로 최단거리 이동 할 것이다. 두 가지 조건을 만족하면서 이동 하는 최단 경로. 주어진 두 정점은 반드시 통과해야 할 것.
한 번 이동했던 정점은 물론, 한 번 이동했던 간선도 다시 이동 가능. 반드시 최단 경로로 이동해야한다.
1번에서 n을 이동할 때 두 정점을 거치면서 최단경로 이동 프로그램.

입력
노드n 간선e 2이상800이하 0이상 20만이하
a, b, c a에서 b로 가는 양방향 노드, 거리가 c
반드시 거쳐야 하는 정점 번호 v1, v2. 두 정점은 서로 다르며 목적지와 시작지가 아니다. 
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijkstra(sta, end): # 다이크스트라
    global n
    dst = [int(10e9)] * (n+1) # 거리 최댓값으로 설정
    heap = [] # 힙
    heappush(heap, (0, sta)) # 힙에 넣어줌. 최단거리 순
    dst[sta] = 0 # 자기 자신 0
    while heap:
        sumc, now = heappop(heap) # 현재 받은 노드와 그렇게 오는데까지 걸린 코스트
        if dst[now] < sumc: # 이미 코스트가 적은게 있다면 밴
            continue
        for i in g[now]: # 작다면 현재 노드의 길을 보면서
            cost, nod = i # 이동할 노드와 그까지 가는데 코스트
            if dst[nod] > sumc + cost: # 이동 할 노드의 값보다 새로 이동하는 코스트가 작다면
                dst[nod] = sumc + cost # 갱신하고
                heappush(heap, (sumc + cost, nod)) # 힙에 넣어서 검사.
    return dst[end]

n, e = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b)) # 비용이 c
    g[b].append((c, a)) # 비용이 c
v1, v2 = map(int, input().split())

r1 = dijkstra(1, v1)+dijkstra(v1, v2)+dijkstra(v2, n)
r2 = dijkstra(1, v2)+dijkstra(v2, v1)+dijkstra(v1, n)

if r1 >= int(10e9) and r2 >= int(10e9):
    print(-1)
elif r1 >= int(10e9) and r2 < int(10e9):
    print(r2)
elif r2 >= int(10e9) and r1 < int(10e9):
    print(r1)
elif r1 < int(10e9) and r1 < int(10e9):
    print(min(r1, r2))




'''
4 5
1 2 10
1 3 11
2 3 20
2 4 30
3 4 100
2 3

61 1 3 2 4
'''


