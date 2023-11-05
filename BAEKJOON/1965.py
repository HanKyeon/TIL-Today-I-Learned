'''
상자 넣기

상자가 일렬로 늘어서 있다. 앞의 상자가 뒤에 있는 상자보다 작으면 안에 넣을 수 있다.
한 번에 넣을 수 있는 최대 상자의 갯수 출력

입력
n 제시
상자 순서 제시

출력
최대 상자 갯수 출력
'''
import sys
input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().rstrip().split()))
dp = [1 for i in range(n)]

for i in range(1,n):
    m, mi = 0, i
    for j in range(i):
        if nl[i] > nl[j] and dp[j] > m:
            m, mi = dp[j], j
    if nl[mi] < nl[i]:
        dp[i] += m

print(max(dp))