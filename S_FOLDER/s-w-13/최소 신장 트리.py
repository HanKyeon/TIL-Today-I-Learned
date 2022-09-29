'''
MST 만들어라.
'''
from heapq import heappop, heappush

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 해서 넣기
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for tc in range(1, int(input())+1):
    n, m = map(int, input().rstrip().split())
    parent = list(range(n+1))
    heap = []
    for _ in range(m):
        a, b, c = map(int, input().rstrip().split())
        heappush(heap, (c, a, b))
    ans = 0
    while heap:
        cost, nod1, nod2 = heappop(heap)
        nod1, nod2 = find(nod1), find(nod2)
        if nod1 == nod2:
            continue
        union(nod1, nod2)
        ans += cost
    print(f"#{tc} {ans}")
