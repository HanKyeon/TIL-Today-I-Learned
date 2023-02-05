'''
도시 건설

도시 mst 만드는데 최대 합에서 이득 보는 만큼 구해라.

입력
n, m  제시.
m개 줄 a, b, c 제시. 중복 x

출력
얼마나 절약 가능? 연결 불가능이면 -1
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().rstrip().split())
egs, parent = [], list(range(n+1))
ans = 0
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    heappush(egs, (c, a, b))
    ans += c
cnt = 0
while egs:
    c, a, b = heappop(egs)
    ra, rb = find(a), find(b)
    if ra == rb:
        continue
    union(ra, rb)
    cnt += 1
    ans -= c
    if cnt == n-1:
        break
if cnt != n-1:
    ans = -1
print(ans)



