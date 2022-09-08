'''
구간 합 구하기

n n 크기 표.
x1 y1부터 x2 y2 까지의 합을 구하는 프로그램 작성.

입력
1이상 1024이하 n 10만이하 m
그래프
x1 y1 <= 만족. x2 y2

출력
M개 줄에 걸쳐 구간합 출력
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[0]*(n+1) for _ in range(n + 1)]
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j] - dp[i][j]) + g[i][j]
for i in range(m):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    print(dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1] - dp[x1-1][y1-1]))





