'''
최단경로

평범한 다익스트라.
방향 그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 모든 간선의 가중치는 10 이하 자연수.

입력
정점의 갯수 V와 간선의 갯수E 제시. 1이상 2만이하B 1이상 30만이하E 정점 번호는 1~V
시작 정점의 번호K
간선을 나타내는 u v w. u에서 v로 가는 비용 w인 간선이 존재한다는 뜻. w는 10이하.
서로 다른 두 정점 사이에 여러 간선이 존재 할 수 있다.

출력
각 노드에 대한 최단 경로값 출력. 시작점 자기 자신은 0
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

v, e = map(int, input().split()) # 노드 간선
k = int(input()) # 시작점
dst = [int(10e9)] * (v+1) # 최단거리 테이블
vis = [False] * (v+1) # 방문 테이블
g = [[] for _ in range(v+1)] # 간선 정보 그래프
for _ in range(e):
    u, V, w = map(int, input().split())
    g[u].append((V, w))

def func(): # 방문 안한 거리가 가장 짧은 노드 번호를 리턴 할 것이다.
    global vis, dst
    ml = min([i for i, x in zip(dst, vis) if x == False]) # False 중 가장 짧은 거리값
    for i in range(1, v+1):
        if dst[i] == ml and vis[i] == 0:
            return i

def 다익스트라(sta):
    dst[sta], vis[sta] = 0, True
    for i in g[sta]: # 출발점에서 거리 기록
        dst[i[0]] = min(i[1], dst[i[0]])
    for _ in range(v-1):
        i = func()
        vis[i] = True
        for j in g[i]:
            dst[j[0]] = min(dst[j[0]], dst[i]+j[1])

def 다익스트라힙큐(sta):
    q = []
    heappush(q, (0, sta))
    dst[sta] = 0
    while q:
        dist, now = heappop(q)
        if dst[now] < dist:
            continue
        for i in g[now]:
            c = dist + i[1]
            if c < dst[i[0]]:
                dst[i[0]] = c
                heappush(q, (c, i[0]))

다익스트라힙큐(k)

for i in range(1, v+1):
    if dst[i] != int(10e9):
        print(dst[i])
    else:
        print("INF")




'''
# 기본 다익스트라. 기본이라서 시간초과가 나는듯하다.
import sys
input = sys.stdin.readline

v, e = map(int, input().split()) # 노드 간선
k = int(input()) # 시작점
dst = [int(10e9)] * (v+1) # 최단거리 테이블
vis = [False] * (v+1) # 방문 테이블
g = [[] for _ in range(v+1)] # 간선 정보 그래프
for _ in range(e):
    u, V, w = map(int, input().split())
    g[u].append((V, w))

def func(): # 방문 안한 거리가 가장 짧은 노드 번호를 리턴 할 것이다.
    global vis, dst
    ml = min([i for i, x in zip(dst, vis) if x == False]) # False 중 가장 짧은 거리값
    for i in range(1, v+1):
        if dst[i] == ml and vis[i] == 0:
            return i

def 다익스트라(sta):
    dst[sta], vis[sta] = 0, True
    for i in g[sta]: # 출발점에서 거리 기록
        dst[i[0]] = min(i[1], dst[i[0]])
    for _ in range(v-1):
        i = func()
        vis[i] = True
        for j in g[i]:
            dst[j[0]] = min(dst[j[0]], dst[i]+j[1])

다익스트라(k)

for i in range(1, v+1):
    if dst[i] != int(10e9):
        print(dst[i])
    else:
        print("INF")
'''




