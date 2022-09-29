'''
MST 만들어라.
'''
from heapq import heappop, heappush

for tc in range(1, int(input())+1):
    n, m = map(int, input().rstrip().split())
    parent = list(range(n+1))
    g = [[] for _ in range(n+1)]
    v = [int(10e9)]*(n+1)
    heap = []
    for _ in range(m):
        a, b, c = map(int, input().rstrip().split())
        g[a].append((c, b))
        g[b].append((c, a))
    v[1] = 0
    for i in g[1]:
        heappush(heap, i)

    while heap:
        cost, nod = heappop(heap)
        if v[nod] != int(10e9):
            continue
        v[nod] = cost
        for i in g[nod]:
            heappush(heap, i)
        if v.count(int(10e9)) == 0:
            break
    ans = 0
    print(f"#{tc} {sum(v)}")