'''
외판원 순회

1부터 n까지 도시들. 도시 사이엔 길. 길이 ㅇ벗을 수 있다.
한 도시에서 출발해 n개의 도시를 모두 거쳐 다시 원래 도시로 돌아오는 경로 계획. 한 번 갔던 도시로는 갈 수 없음. 첫 도시로는 올 수 있다.
가장 적은 비용을 들이는 여행 계획 짤 것.
비용은 w[i][j] 형태로 제시.
n과 비용 행렬 제시. 가장 적은 비용 들이는 외판원 순회 경로 구해라.

입력
n 제시
n개 줄 비용 행렬 제시. 갈 수 없다면 0

입력
최소 비용 출력
'''


import sys
input = sys.stdin.readline
N = int(input())
dp = [list(map(int, input().rstrip().split())) for _ in range(N)]
v = [[-1 for _ in range(1 << N)] for _ in range(N)]

def dfs(cur, visit, s, cnt):
    if cnt == N:
        return 0
    if v[cur][visit] != -1:
        return v[cur][visit]
    ret = 10000000
    for i in range(N):
        if visit & (1 << i) != 0 or dp[cur][i] == 0:
            continue
        if (cnt == N - 1 and i != s) or (cnt != N - 1 and i == s):
            continue
        ret = min(ret, dfs(i, visit | (1 << i), s, cnt + 1) + dp[cur][i])
    v[cur][visit] = ret
    return v[cur][visit]

print(dfs(0, 0, 0, 0))

'''
import sys
input = sys.stdin.readline

def dfs(cur, v):
    global n
    if v == (1 << n) - 1:     # 모든 도시를 방문했다면
        if g[cur][0]:             # 출발점으로 가는 경로가 있을 때
            return g[cur][0]
        else:                       # 출발점으로 가는 경로가 없을 때
            return 20000000

    if dp[cur][v] != 20000000:       # 이미 최소비용이 계산되어 있다면
        return dp[cur][v]

    for i in range(1, n):           # 모든 도시를 탐방
        if not g[cur][i] or v & (1 << i):         # 가는 경로가 없거나 방문 했다면
            continue

        dp[cur][v] = min(dp[cur][v], dfs(i, v | (1 << i)) + g[cur][i])
    return dp[cur][v]

n = int(input())
dp = [[20000000] * (1 << n) for _ in range(n)]
g = [list(map(int, input().rstrip().split())) for _ in range(n)]

print(dfs(0, 1))
'''

'''
# dfs

import sys
input = sys.stdin.readline

def dfs(s: int, cur: int, val: int, cnt:int):
    global ans
    if val >= ans:
        return
    if cnt == n:
        if val+g[cur][s] < ans:
            ans = val+g[cur][s]
        return
    for i in range(n):
        if v[i] or not g[cur][i]:
            continue
        v[i] = 1
        dfs(s, i, val+g[cur][i], cnt+1)
        v[i] = 0

n = int(input())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
ans = 20000000
v = [0]*n
for i in range(n):
    v[i] = 1
    dfs(i, i, 0, 1)
    v[i] = 0
print(ans)
'''


'''
# 빠른 코드
# 조합에 비트마스킹까지 쓰는거 보면 똑똑한듯하다...

from itertools import combinations

def set_to_int(l):
    res = 0
    for item in l:
        res = res | 1<<(item - 1)
    return res

N = int(input())
adj = [[0]*(N+1)]
for _ in range(N):
    adj.append([0]+list(map(int, input().split())))
memo = [[16777216] * N for _ in range(1<<(N-1))]

for i in range(1, N):
    if adj[N][i] :
        memo[1<<(i-1)][i] = adj[N][i] 

for i in range(2, N):
    for combi in combinations(range(1, N), i):
        bitset = set_to_int(combi)
        for v in combi:
            min_dist = 16777216
            bitset = bitset ^ (1<<(v-1))
            for u in combi:
                tmp = memo[bitset][u] + adj[u][v]
                if adj[u][v] != 0 and min_dist > tmp :
                    min_dist = tmp
            bitset = bitset | (1<<(v-1))
            memo[bitset][v] = min_dist

bitset = set_to_int([i for i in range(1, N)])
for i in range(1, N):
    final_cost = 16777216 if adj[i][N] == 0 else memo[bitset][i] + adj[i][N]
    memo[bitset][i] = final_cost

print(min(memo[bitset]))
'''

