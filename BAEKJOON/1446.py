'''
지름길

지름길 존재. 지름길은 일방통행, 고속도로는 역주행 금지.
운전해야 하는 거리 최솟값

입력
지름길 갯수 n, 고속도로 길이 D 제시. n은 12이하 D는 1만이하.
n개 줄 시작, 도착, 지름길 제시.

출력
운전 최소거리 출력.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
dp = list(range(m+1))
heap = []
for _ in range(n):
    a, b, c = map(int, input().rstrip().split())
    heappush(heap, (b, a, c))

while heap:
    b, a, c = heappop(heap)
    if b > m:
        continue
    if dp[b] > dp[a]+c:
        dp[b] = dp[a]+c
        v = 1
        while b+v <= m and dp[b+v] > dp[b]+v:
            dp[b+v] = dp[b]+v
            v+=1

print(dp[-1])



# 처음에 150












