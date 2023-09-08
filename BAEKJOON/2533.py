'''
사회망 서비스

친구관계 트리가 제시되었을 때, 모든 개인이 새로운 아이디어를 수용하기 위해 필요한 최소 얼리어답터의 수를 구해라.
1~n까지 트리 구조, 사이클 없음

입력
n 제시
n-1개 줄 a, b 제시

출력
얼리어탑터의 최소 수를 하나의 정수로 출력
'''
import sys
sys.setrecursionlimit(1111111)
input = sys.stdin.readline

def dfs(nod):
    v[nod] = 1
    if not g[nod]: dp[nod] = [0, 1]; return
    for i in g[nod]:
        if v[i]: continue
        dfs(i)
        dp[nod][0] += dp[i][1]
        dp[nod][1] += min(dp[i])
    dp[nod][1] += 1

n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().rstrip().split())
    g[a].append(b)
    g[b].append(a)
v, dp = [0]*(n+1), [[0, 0] for _ in range(n+1)]
dfs(1)
print(min(dp[1]))

'''
# 빠른 코드

import sys
input = sys.stdin.readline

def solve(tree):
    leaf = [i for i in range(n) if len(tree[i]) == 1]
    visited = [0]*n
    while leaf:
        node = leaf.pop()
        for par in tree[node]:
            for gra_par in tree[par]:
                tree[gra_par].remove(par)
                if len(tree[gra_par]) == 1:
                    leaf.append(gra_par)
            visited[par] = 1
            tree[par].clear()
    return sum(visited)
        
n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    u,v = map(int,input().split())
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)

print(solve(tree))
'''
