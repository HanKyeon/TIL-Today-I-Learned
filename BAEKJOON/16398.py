'''
행성 연결

중심은 행성 T이다. n개 행성 간 플로우 설치 할 것이다.
플로우 관리 비용 최소한으로 할 것이다.
n개 행성은 정수 1~n으로, i, j 간 관리 비용은 cij이다.
유지비용 최소화 해라.

입력
행성 수 n 제시.
n*n 행렬 제시.

출력
모든 행성을 연결 했을 때, 최소 플로우 관리 비용 출력
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y: return 0
    elif x < y: parent[y] = x
    else: parent[x] = y
    return 1

n = int(input())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
egs, parent = [], list(range(n))
for i in range(n-1):
    for j in range(i+1, n):
        heappush(egs, (g[i][j], i, j))
ans, egcnt = 0, 0
while egs:
    cost, i, j = heappop(egs)
    if union(i, j):
        ans += cost
        egcnt += 1
    if egcnt == n-1: break
print(ans)



'''
# 프림 쓴 짱 빠른 사람

N    = int(input())
csts = [list(map(int,input().split())) for _ in range(N)]


def prim(W):
    dists   = [int(1e9)] * N
    nearest = [int(1e9)] * N
    edges   = []
    # 시작 노드 : 0
    dists[0],nearest[0] = -1,-1
    for i in range(1,N):
        dists[i],nearest[i] = W[0][i],0
    # N-1 개의 노드 추가적 선택
    for _ in range(N-1):
        mDist,mIdx = int(1e9),-1
        for i in range(N):
            if dists[i] > 0 and dists[i] < mDist :
                mDist,mIdx = dists[i],i
        edges.append((mDist,mIdx,nearest[mIdx]))
        dists[mIdx] = -1
        for i in range(N):
            if dists[i] > 0 and dists[i] > W[mIdx][i] :
                dists[i] = W[mIdx][i]
                nearest[i] = mIdx
    return edges

edges = prim(csts)
print(sum(edge[0] for edge in edges))
'''









