'''
포도주 시식

포도주 일렬 배치. 규칙은 둘
1. 포도주 잔 고르면 다 마시고 제자리.
2. 연속 3잔 마실 수 없음
최대한 많은 포도주를 맛보려 함.
1~n개의 포도주잔이 일렬로 주어졌을 때 가장 많이 마실 수 있는 포도주의 양은?

n은 1부터 만, 포도주 양은 1000이하 음x정수
'''
n = int(input())
nl = [int(input()) for _ in range(n)]
g = [0] * n
if n == 1 or n == 2:
    print(sum(nl))
elif n == 3 :
    print(max(nl[0] + nl[2], nl[1]+nl[2], nl[0]+nl[1]))
else :
    # 첫번째와 두번째의 최솟값은 고정
    g[0], g[1] = nl[0], nl[0]+nl[1]
    g[2], g[3] = max(nl[0] + nl[2], nl[1]+nl[2], nl[0]+nl[1]), max(g[1] + nl[3], g[0] + nl[2] + nl[3], nl[1]+nl[2])
    # 한칸 띄고 i잔을 마시는 경우
    # 바로 앞 i-1잔과 함께 i잔을 마시는 경우
    # 자신 i잔을 마시지 않는 경우
    # 위 세가지 중 최댓값으로 설정.
    for i in range(4, n):
        g[i] = max(g[i-3] + nl[i-1] + nl[i], g[i-2] + nl[i], g[i-4] + nl[i-2] + nl[i-1])
    print(max(g))

# 아래는 남의 풀이
'''
import sys
n, *score = [*map(int,open(0).read().split())]
if n<=2: print(sum(score)); sys.exit(0)
partsum = [score[0]+score[1],score[1],score[0],0]
for i in range(2,n):
    partsum = [partsum[1]+score[i],max(partsum[2:])+score[i],
               max(partsum[:2]),partsum[2]]
print(max(partsum))
'''

'''
N = int(input())
wines = [int(input()) for _ in range(N)]

dp = [0] * 10001

# 초기화
if N > 0:
  dp[1] = wines[0] 
if N > 1:
  dp[2] = dp[1] + wines[1]
if N > 2:
  dp[3] = max(dp[1], wines[1]) + wines[2]
if N > 3:
  dp[4] = max(dp[2], dp[1]+wines[2]) + wines[3] 
if N > 4:
  for n in range(5, N+1):
    # 직전 와인을 마신 경우 => (두 칸, 세 칸 건너 뜀 비교) + 직전 와인의 양
    # 직전 와인을 마시지 않은 경우 => 한 칸 건너 뜀
    # 위의 경우를 모두 비교
    dp[n] = max(dp[n-2], max(dp[n-4], dp[n-3]) + wines[n-2]) + wines[n-1]

print(max(dp[N-1], dp[N]) if N > 1 else dp[N])
'''