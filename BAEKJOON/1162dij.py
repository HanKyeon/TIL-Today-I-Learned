'''
도로 포장

서울 포천 출퇴근. 지각 일쑤. K개의 도로를 포장해 시간 단축 예정.
N개 도시 제시. 그 사이 도로와 걸리는 시간 제시. 최소 시간이 걸리도록 하는 k개 이하의 도로를 포장.
도로는 이미 있는 도로만 포장 가능, 포장하면 도로를 지나는데 걸리는 시간이 0이 된다. 또한 편의상 서울은 1번 도시, 포천은 N번 도시. 1에서 N까지 갈 수 있는 데이터만 제시.

입력
n, m, k 제시. 도시 수 도로 수 포장 제한 수
m개 줄 도로가 연결하는 두 도시, 시간 제시. a,b,c. 양방향 도로.

출력
k개 이하의 도로를 포장하여 얻을 수 있는 최소 시간 출력.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
    g[b].append((c, a))

def dij():
    global n
    dst = [[int(10e9)]*(k+1) for _ in range(n+1)]
    heap = [(0, 1, k)]
    dst[1] = [0]*(k+1)
    while heap:
        cost, nod, cnt = heappop(heap)
        if dst[nod][cnt] < cost:
            continue
        if nod == n:
            return min(dst[n])
        for co, nnod in g[nod]:
            if cost+co < dst[nnod][cnt]:
                dst[nnod][cnt] = cost+co
                heappush(heap, (cost+co, nnod, cnt))
            if cnt > 0 and dst[nnod][cnt-1] > cost:
                dst[nnod][cnt-1] = cost
                heappush(heap, (cost, nnod, cnt-1))

print(dij())









