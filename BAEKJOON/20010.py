'''
악덕 영주 혜유

교역료 양방향 이동. MST 제작. 최소 비용 연결, 최소 비용 제시. 최대 비용 연결, MST 일 때 최대 비용 경로 제시.

입력
마을 수 N 1000, 설치 가능한 교역로 수 K 제시.
K개 줄 a, b, c 제시.
최소 비용 연결 유일.
서로 다른 두 마을 건설 교역료 최대 1
마을은 0부터 n-1 번호 보유.

출력
MST 비용
MST 내에서 가장 많이 드는 비용.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 해서 넣기
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def lego():
    global n, k
    ret1 = 0
    idx = 0
    g = [[] for _ in range(n)]
    mval = [0]*n
    while heap and idx != n-1:
        cost, nod1, nod2 = heappop(heap)
        r1, r2 = find(nod1), find(nod2)
        if r1 == r2:
            continue
        ret1 += cost
        union(r1, r2)
        idx += 1
        mval[idx] = ret1
        g[nod1].append((cost, nod2))
        g[nod2].append((cost, nod1))

    # dfs 부분
    v = [0]*n
    def dfs(nod, val):
        global ret2
        fla = False
        for cost, nnod in g[nod]:
            if v[nnod]:
                continue
            if not fla:
                fla = True
            v[nnod] = 1
            dfs(nnod, val+cost)
            v[nnod] = 0
        if not fla:
            ret2 = max(ret2, val)
    for i in range(n):
        v[i] = 1
        dfs(i, 0)
        v[i] = 0
    return ret1

n, k = map(int, input().rstrip().split())
parent = list(range(n))
heap = []
ret2 = 0
for _ in range(k):
    a, b, c = map(int, input().rstrip().split())
    heappush(heap, (c, a, b))

ans1 = lego()

print(ans1)
print(ret2)







