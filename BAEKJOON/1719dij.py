'''
택배

택배 사업. 집하장 == 노드. 어떤 경로를 거쳐갈 지 결정 못함
어떤 경로를 거칠 지 정해서 경로표로 정리해야한다.

경로표는 한 집하장에서 다른 집하장으로 최단 경로로 화물을 이동시키기 위해 가장 먼저 거쳐야 하는 집하장을 나타낸 것이다. ex 4번 집하장에서 5번 집하장으로 가는 가장 최단 거리는 우선 6번 집하장으로 이동해야 한다는 의미.
경로표 구해라.

입력
n, m 제시. n은 집하장 갯수 200이하 자연수 m은 1만이하 자연수 경로 수.
m개 줄 집하장 경로 제시. 노드1 노드2 비용 제시. 소요시간 1000이하 자연수.

출력
경로표로 출력
'''
# 다익스트라로 하되, 처음 시작점을 기억해야 한다.
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dij(sta):
    dst = [int(10e9)] * n
    vst = [0]*n
    dst[sta] = 0
    heap = [(0, sta, 0)]
    while heap:
        cost, nod, fnod = heappop(heap)
        for co, nnd in g[nod]:
            if nod == sta: # 핵심 아이디어. 처음 뻗는 노드를 기억하기 위한 조건.
                fnod = nnd+1
            if dst[nnd] > cost + co:
                vst[nnd] = fnod
                dst[nnd] = cost + co
                heappush(heap, (cost+co, nnd, fnod))
    vst[sta] = '-'
    return vst

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a-1].append((c, b-1))
    g[b-1].append((c, a-1))
dij(0)
for i in range(n):
    print(*dij(i))


'''
# 이사람 빠르네 파이썬 1100

from cmath import inf
import heapq
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b,a))
    graph[b].append((c,a,b))

matrix=[]
for i in range(1,N+1):
    q=[(0,i)]
    dist=[inf]*(N+1)
    chart=[0]*(N+1)
    dist[i]=0
    while q:
        Z,X=heapq.heappop(q)
        if dist[X]<Z:
            continue
        for cost,next,now in graph[X]:
            cost=cost+Z
            if cost<dist[next]:
                dist[next]=cost
                chart[next]=now
                heapq.heappush(q,[cost,next])
    matrix.append(chart)
for i in range(1,N+1):
    for j in range(N):
        if i-1==j:
            print('-', end=' ')
        else:
            print(matrix[j][i],end=' ')
    print()
'''









