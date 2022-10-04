'''
면접보는 승범이네

승범이네 새로 사람 뽑는다.
면접자들은 서로 다른 N개 도시 거주.
거주중인 N개 도시 중 K개의 도시에 면접장 배치.
도시 끼리는 단방향 도로로 연결. 거리는 서로 다를 수 있다.
어떤 두 도시 사이에는 도로가 없을 수도, 여러개가 있을 수도 있다. 또한 어떤 도시에서든 적어도 하나의 면접장까지 갈 수 있는 경로가 항상 존재한다.
모든 면접자는 본인 도시에서 출발하여 가장 가까운 면접장으로 찾아갈 예정. 면접장까지의 거리란 그 도시에서 가장 가까운 면접장까지의 최단 거리이다.
면접장 까지의 거리 중 가장 먼 도시에서 오는 면접자에게 교통비 지원. 면접장 까지의 거리가 가장 먼 도시와 그 거리를 구해보자.

입력
도시의 수 n, 도로수 m, 면접장 수 k 제시. 도시는 1번부터 n번까지 번호.
m개줄 도시 번호 u, v 도로길이 c 제시. u에서 v로 가는 도로 존재 거리가 c 단방향.
면접장 배치 도시 k개 제시.

출력
면접장 까지 거리가 가장 먼 도시의 번호 출력.
그런 도시가 여러곳이면 가장 작은 번호를 출력한다.
해당 도시에서 면접장 까지의 거리
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dij():
    dst = [int(10e9)]*(n+1)
    heap = []
    for i in kl:
        dst[i] = 0
        heappush(heap, (0, i))
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        for co, nnod in g[nod]:
            if dst[nnod] > cost+co:
                dst[nnod] = cost+co
                heappush(heap, (cost+co, nnod))
    mx = max(dst[1:])
    nod = dst.index(mx)
    print(nod)
    print(mx)

n, m, k = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[b].append((c, a))
kl = list(map(int, input().rstrip().split()))
dij()











