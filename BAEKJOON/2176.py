'''
합리적인 이동경로

그래프의 한 정점 S에서 다른 정점 T로 이동 예정. T에 가까워지며 이동하는 경우, 이를 합리적인 이동경로라 한다. 최단 경로가 아닐 수도 있다.
그래프가 주어졌을 때 가능한 합리적인 이동경로의 갯수를 구해라.
시작 노드 1, 도착 노드 2

입력
정점 간선 n, m 제시.
m개 줄 간선 정보 a, b, c 제시 양방향.

출력
합리적인 이동경로 갯수 구해라.
'''
import sys
from heapq import heappop, heappush
from math import inf
input = sys.stdin.readline

def dij():
    global n
    dst = [inf]*(n+1)
    dst[2] = 0
    heap = [(0, 2)]
    while heap:
        cost, nod = heappop(heap)
        for co, nnod in g[nod]:
            costco = cost+co
            if dst[nnod] > costco:
                dst[nnod] = costco
                heappush(heap, (costco, nnod))
    return dst

def bfs():
    global n
    dp = [0]*(n+1)
    dp[2] = 1
    heap = [(0, 1, 2)]
    while heap:
        dst, cnt, nod = heappop(heap)
        if cnt < dp[nod]:
            continue
        for _, nnod in g[nod]:
            if dst < v[nnod]:
                dp[nnod] += dp[nod]
                heappush(heap, (v[nnod], dp[nnod], nnod))
    return dp[1]

def Dij():
    dp, dst = [0]*(n+1), [inf]*(n+1)
    dp[2], dst[2] = 1, 0

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
    g[b].append((c, a))
v = dij()
print(bfs())



'''
# 메모리 초과
def bfs():
    q = deque([1])
    ret = 0
    ng = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        for _, nod in g[i]:
            if v[i] > v[nod]:
                ng[i].append(nod)
    while q:
        nod = q.popleft()
        for i in ng[nod]:
            if i == 2:
                ret += 1
                continue
            q.append(i)
    return ret
'''


'''
# 빠른 코드

import sys
input=sys.stdin.readline
import heapq

def dijkstra():
    heap=[(0, 2)]
    while heap:
        dist,node=heappop(heap)
        if distance[node]<dist:
            continue
        for next_node,next_dist in graph[node]:
            new_dist=dist+next_dist
            if new_dist<distance[next_node]:
                distance[next_node]=new_dist
                heappush(heap,(new_dist,next_node))
            if distance[node]<distance[next_node]:
                dp[next_node]+=dp[node]

if __name__=="__main__":
    n,m=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    dp=[0]* (n+1);dp[2]=1
    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    distance=[float('inf')]*(n+1); distance[2]=0
    dijkstra()
    print(dp[1])
'''






