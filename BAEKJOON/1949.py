'''
우수 마을

n개 마을. 1~n. 트리 구조. 우수 마을 선정할 것
1. 우수 마을 선정 마을 주민 수 총 합을 최대로 해야 함.
2. 두 마을이 인접할 경우, 두 마을 모두 우수 마을 금지.
3. 선정이 안되었을 경우, 적어도 하나의 우수 마을과 인접해 있어야 함.

입력
n 제시
마을 주민 수 n개 자연수 제시.
n-1개 줄 인접한 두 마을 번호 a, b 제시.

출력
우수마을 주민 수 총합
'''
import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(111111)

def dfs(cur):
    v[cur] = 1
    for u in g[cur]:
        if not v[u]:
            dfs(u)
            dp[cur][1] += dp[u][0]
            dp[cur][0] += max(dp[u][0], dp[u][1])

n, nl = int(input().rstrip()), [0]+list(map(int, input().rstrip().split()))
v = [0 for _ in range(n+1)]
dp = [[0, nl[i]]*2 for i in range(n+1)]
g = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().rstrip().split())
    g[a].append(b)
    g[b].append(a)

dfs(1)
print(max(dp[1]))



