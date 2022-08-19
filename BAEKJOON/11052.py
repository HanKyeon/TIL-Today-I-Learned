'''
카드 구매하기

카드깡한다. 제일 쓰레기 같은 효율로 카드 N장 살거다.
패키지는 N개 있다. 1,2,3,4...N장 들어있는 카드팩이다.
1~N장 들어있는 카드팩들의 가격을 제시할거다.

카드 N개 살 때 꼭 카드 N개여야 하고, 제일 비싸게 카드 N개를 사야한다.
카드 갯수 N
Pi가 PN까지 제시.

입력
1이상 1000이하 N
1이상 10000이하 p
'''

n = int(input())
p = [0]+list(map(int, input().split())) # n가격
cn = list(range(n+1)) # 카드팩 넘버 (팩 당 장수)
dp = p[:] # 기본 dp. n장 살 때 최댓가가 현재 자신이라 생각.

for i in range(1, n+1): # dp 순회하면서 (카드 장수 보면서)
    for j in range(1, n+1): # p 순회하면서 (카드 장수 또 보면서)
        if 1 <= i-j <= n: # i-p1장의 가격, i-p2장의 가격, i-p3 ...의 가격을 보며
            dp[i] = max(dp[i-j]+p[j], dp[i]) # 그 가격에 p1원 p2원 p3원을 더한 값보다 작으면 갱신
        else : # i-j가 범위 밖이면 패스
            continue
print(dp[n]) # n장의 가격 최댓값

# 줄일 수 있다!
for i in range(2, n+1): # 1은 어차피 자기 값 고정이니 안봐도 됨.
    for j in range(1, i): # i보다 작은 수의 카드들만 보면 됨.
        dp[i] = max(dp[i-j]+p[j], dp[i]) # 그 가격에 p1원 p2원 p3원을 더한 값보다 작으면 갱신
print(dp[n]) # n장의 가격 최댓값







'''
ef = [0] + [v/pa for pa, v in enumerate(p) if pa != 0] # 팩 별 한장 당 가격
cn = list(range(n+1)) # 카드팩 넘버 (팩 당 장수)
jd = list(zip(ef, p, cn)) # 종합 데이터
jd.sort(reverse=True) # 효율 순 정렬
jd.pop()
mp = 0
print(jd)
for i in jd: # 
    while n >= i[2]:
        mp += i[1] * (n//i[2])
        n %= i[2]
    if n == 0:
        break
print(mp)
'''
#7
#7 33 52 66 57 50 86