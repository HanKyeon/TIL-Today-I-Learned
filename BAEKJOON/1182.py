'''
부분수열의 합

n개 정수 수열, 길이 1이상 부분수열 중에 해당 원소 합이 S가 되는 경우의 수 작성.

입력
n, s 제시

출력
합이 s 되는 갯수 제시
'''
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
nl = list(map(int, input().rstrip().split()))
ans = 0
for i in range(1, n+1):
    for nz in combinations(nl, i):
        if sum(nz) == m:
            ans+=1
print(ans)
