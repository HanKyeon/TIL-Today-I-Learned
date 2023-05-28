'''
가장 큰 증가하는 부분 수열

증가하는 부분 수열 중 합이 가장 큰 것을 구해라.

입력
수열 크기 n 제시.
수열 제시.

출력
가장 큰 증가하는 부분 수열의 합 출력
'''
import sys
input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().rstrip().split()))
dp = nl[:]

for i in range(n-1):
    num = nl[i]
    for j in range(i, n):
        num2 = nl[j]
        if num < num2 and dp[j] < dp[i]+num2:
            dp[j] = dp[i]+num2

print(max(dp))


'''
# 빠른 코드

input()
dp = [0] * 1001
for i in map(int, input().split()):
    dp[i] = max(dp[:i]) + i

print(max(dp))
'''

