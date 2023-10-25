import sys
sys.setrecursionlimit(2000)

def dfs(x):
    v[x] = True
    if not v[nl[x]]:
        dfs(nl[x])

for _ in range(int(input())):
    n = int(input())
    nl = [0]+list(map(int, input().split()))
    v = [True]+[False]*n
    ans = 0
    for i in range(1, n+1):
        if v[i]: continue
        dfs(i)
        ans += 1
    print(ans)