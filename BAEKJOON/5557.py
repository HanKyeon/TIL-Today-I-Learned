'''
1학년

마지막은 = 넣고 +나 - 넣으면서 이란다. 중간에 나오는 수는 0~20 사이여야 한다.
만들 수 잇는 올바른 등식의 갯수 출력
'''
import sys
input = sys.stdin.readline

n, nl = int(input()), list(map(int, input().rstrip().split()))
ans, dp = nl.pop(), [[0]*21 for _ in range(n-1)]
dp[0][nl[0]] = 1
for i in range(1, n-1):
    for j in range(21):
        if not dp[i-1][j]: continue
        p, m = j+nl[i], j-nl[i]
        if p<21: dp[i][p] += dp[i-1][j]
        if 0<=m: dp[i][m] += dp[i-1][j]
print(dp[-1][ans])
