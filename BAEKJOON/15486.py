'''
퇴사 2

n+1일째 되는 날 퇴사를 하기 위해 n일동안 많은 상담을 하려 한다.
하루 하나씩 서로 다른 사람의 상담을 잡았다.
상담은 완료하는데 걸리는 기간 t, 받을 수 있는 금액 p.
상담 적절히 했을 때 얻ㅇ르 수 있는 최대 이익

입력
n 제시.
n개 줄 t, p 제시. 1일부터 n일까지 순서대로 제시.

출력
얻을 수 있는 최대 이익 출력.
'''
import sys
input = sys.stdin.readline

n = int(input())
g, dp = [], [0]*(n+1)
for i in range(n):
    t, p = map(int, input().rstrip().split())
    g.append((i, t, p))
mv = 0
ans = 0
for i, t, p in g:
    if dp[i] > mv:
        mv = dp[i]
    if i+t > n:
        continue
    if mv+p > dp[i+t]:
        dp[i+t] = mv+p
        if ans < mv+p:
            ans = mv+p
print(ans)





