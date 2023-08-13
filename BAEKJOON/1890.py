'''
점프

n*n 게임판
각 칸에 적혀있는 수는 현재 칸에서 갈 수 있는 거리. 우측이나 하단으로만 이동. 0은 종착점. 방향 변경 불가능.
좌상단에서 우하단으로 규칙에 맞게 이동 가능한 경로의 갯수를 구하시오.

입력
n 제시
그래프 제시. 0이상 9이하 정수 우하단은 항상 0

출력
갈 수 있는 경로 갯수 출력. 2**63-1보다 작거나 같다
'''
import sys
input = sys.stdin.readline

n = int(input())
g, dp = [], [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    s = list(map(int, input().rstrip().split()))
    for j in range(n):
        if not dp[i][j] or i == n-1 and j == n-1: continue
        if i+s[j] < n:
            dp[i+s[j]][j] += dp[i][j]
        if j+s[j] < n:
            dp[i][j+s[j]] += dp[i][j]
print(dp[-1][-1])

'''
# 빠름
# 우와 일렬 dp는 상상도 못했다
n,*a=map(int,open(0).read().split())
b=[1]+[0]*n*n
for i in range(n):
 for j in range(n):
  k=i*n+j;d=a[k];e=b[k]
  if(d>0)*(e>0):
   if i+d<n:b[k+d*n]+=e
   if j+d<n:b[k+d]+=e
print(b[-2])
'''




