'''
가장 긴 감소하는 부분 수열

수열 A 제시, 가장 긴 감소하는 부분 수열 길이 출력

입력
n 제시
nl 제시

출력
가장 긴 감소하는 부분 수열 길이 출력
'''
n = int(input())
nl = list(map(int, input().split()))
dp = [1]*n
for i in range(n):
    for j in range(i):
        if nl[j] <= nl[i]:continue
        dp[i] = max(dp[i],dp[j]+1)
print(max(dp))