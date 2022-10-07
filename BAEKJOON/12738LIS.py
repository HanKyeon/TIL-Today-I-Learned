'''
가장 긴 증가하는 부분 수열 3

수열 A가 제시되었을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램 작성
'''
# 참고하여 풀었다.

from bisect import bisect_left #이진탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다

input()
A = list(map(int, input().split()))
dp = []

for i in A:
    k = bisect_left(dp, i) #자신이 들어갈 위치 k
    if len(dp) <= k: #i가 가장 큰 숫자라면
        dp.append(i)
    else:
        dp[k] = i #자신보다 큰 수 중 최솟값과 대체
print(len(dp))
