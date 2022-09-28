'''
dfs 정점1
'''
def dfs(num):
    for i in sorted(g[num]):
        if v[i]:
            continue
        v[i] = 1
        ans.append(i)
        dfs(i)

for tc in range(1, int(input())+1):
    n, m = map(int, input().rstrip().split())
    g = [[] for _ in range(n+1)]
    v = [1, 1]+[0]*(n-1)
    for _ in range(m):
        a, b = map(int, input().rstrip().split())
        g[a].append(b)
        g[b].append(a)
    ans = [1]
    dfs(1)
    print(f"#{tc}", end=' ')
    print(*ans)