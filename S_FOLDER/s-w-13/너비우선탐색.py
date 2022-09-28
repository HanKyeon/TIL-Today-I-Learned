'''
시작 정점1 너비우선 탐색 ㄱㄱ
'''
from collections import deque

for tc in range(1, int(input())+1):
    n, m = map(int, input().rstrip().split())
    q = deque([1])
    g = [[] for _ in range(n+1)]
    v = [1, 1]+[0]*(n-1)
    for _ in range(m):
        a, b = map(int, input().rstrip().split())
        g[a].append(b)
        g[b].append(a)
    print(f"#{tc}", end=' ')
    while q:
        num = q.popleft()
        print(f"{num}", end=' ')
        for i in sorted(g[num]):
            if v[i]:
                continue
            v[i] = 1
            q.append(i)
    print()

