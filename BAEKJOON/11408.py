'''
이동하기

n*m 미로. 1,1부터 n,m까지. 하 우 대각 이동 가능. 사탕 최댓값.

입력
n,m 제시
n개 줄 그래프 제시

출력
n,m 도착했을 때 사탕 최댓값 출력
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+g[i-1][j-1]
print(dp[-1][-1])
