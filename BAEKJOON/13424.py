'''
비밀 모임

n개 방 중 하나를 모임 장소로 쓸 것.
처음 위치에서 모임까지 이동하는 비밀통로 길이의 합
비밀통로의 길이 합이 최소인 방에서 모인을 할 것이다.
총합이 최소가 되는 모임 장소를 찾아 출력해라.

입력
테케T
n, m 제시. 방 갯수/통로갯수
m개 줄 a, b, c 제시. a에서 b b에서 a 비용 c
모임에 참여하는 친구 수 k 제시.
k개 친구 있는 방 번호 제시.

출력
이동거리 총합이 최소가 되도록 하는 모임 장소의 방 번호 출력. 여러개일 경우 번호가 가장 작은 방의 번호 출력.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dij2(tg):
    global n
    dst = [int(10e9)]*(n+1)
    dst[tg] = 0
    heap = [(0, tg)]
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        for co, nnod in g[nod]:
            if dst[nnod] > cost+co:
                dst[nnod] = cost+co
                heappush(heap, (cost+co, nnod))
    ret = 0
    for i in kl:
        ret += dst[i]
    return (ret, tg)

def dij():
    global n, k
    if k == 1:
        return kl[0]
    if k == 2:
        dst = [int(10e9)]*(n+1)
        a, b = kl
        dst[a] = 0
        heap = [(0, a, a)]
        while heap:
            cost, nod, mnod = heappop(heap)
            if cost > dst[nod]:
                continue
            if nod == b:
                return mnod
            for co, nnod in g[nod]:
                if dst[nnod] > cost+co:
                    dst[nnod] = cost+co
                    if nnod < mnod:
                        heappush(heap, (cost+co, nnod, nnod))
                    else:
                        heappush(heap, (cost+co, nnod, mnod))
    else:
        ret = []
        for i in range(1, n+1):
            heappush(ret, dij2(i))
        dst, nod = heappop(ret)
        return nod

for _ in range(int(input())):
    n, m = map(int, input().rstrip().split())
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().rstrip().split())
        g[a].append((c, b))
        g[b].append((c, a))
    k = int(input())
    kl = list(map(int, input().rstrip().split()))
    print(dij())


'''
# 빠른 코드

import sys
input = sys.stdin.readline
INF = int(1e9)
for _ in range(int(input())):
    n,m = map(int,input().split())
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a][b]=c
        graph[b][a]=c
    k = int(input())
    friend = list(map(int,input().split()))
    for i in range(1,n+1):
        graph[i][i]=0 
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
        
    ans = []
    for i in range(1,n+1):
        cnt = 0
        for f in friend:
            cnt+=graph[f][i]
        ans.append((cnt,i))
        
    print(sorted(ans)[0][1])
'''
