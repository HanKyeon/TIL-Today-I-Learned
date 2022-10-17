'''
택배 배송

농부 현서는 찬홍이에게 택배를 배달해야 한다. 가려는 길에 만나는 소들에게 여물 줄 것. 최소한의 소를 만날 것.
n개의 헛간, m개의 소들의 길, 각각의 길은 C_i마리의 소 존재.
소들은 두개의 떨어진 헛간인 Ai와 Bi를 잇는다. 두개의 헛간은 하나 이상의 길로 연결.
현서는 1, 찬홍이는 N
최소 여물은?

입력
n, m  제시.
m개 줄 a, b, c 제시.

출력
n, m 제시
m개줄 a, b, c 제시
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
    g[b].append((c, a))
def dij():
    global n
    dst = [int(10e9)]*(n+1)
    dst[1] = 0
    heap = [(0, 1)]
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        if nod == n:
            return dst[n]
        for co, nnod in g[nod]:
            if dst[nnod] > cost+co:
                dst[nnod] = cost+co
                heappush(heap, (cost+co, nnod))
print(dij())



