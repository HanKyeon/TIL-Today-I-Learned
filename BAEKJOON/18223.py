'''
민준이와 마산 그리고 건우

마산으로 가는 가장 짧은 길을 찾는 것이다.
양방향 그래프. 출발은 1번 마산은 v번. 건우는 p에 존재.
p를 들렀다 가는 최단 경로가 있는지 확인해라.

입력
정점 갯수 v, 간선 갯수 e, 건우 p 제시.
e개 줄 a, b, c 제시.

출력
최단 경로 위에 건우가 있다면 SAVE HIM, 아니면 GOOD BYE 출력.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dij(idx):
    global n, p
    dst = [int(10e9)]*(n+1)
    dst[idx] = 0
    heap = [(0, idx)] # 비용 노드 p 들렀는지
    while heap:
        cost, nod = heappop(heap)
        if cost > dst[nod]:
            continue
        for co, nnod in g[nod]:
            if cost+co < dst[nnod]:
                dst[nnod] = cost+co
                heappush(heap, (cost+co, nnod))
    return dst

n, m, p = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
    g[b].append((c, a))

li1 = dij(1)
li2 = dij(p)
if li1[n] == li2[1]+li2[n]:
    print('SAVE HIM')
else:
    print('GOOD BYE')

