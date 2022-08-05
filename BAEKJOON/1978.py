'''
소수 찾기

에라토스테네스의 체
'''
# 입력
n = int(input())
nl = list(map(int, input().split()))
# 에라토스테네스의 체 테이블
dp = [True for x in range(1001)]
# 0과 1은 소수가 아님
dp[0], dp[1] = False, False
# 체
for i in range(2, int(1001 ** (1/2))+1) : # 1000 제곱근까지 봄
    # 제일 작은 수부터 본다.
    if dp[i] == True : # 소수면
        j = 2
        while i * j < 1001 : #곱한거 다 빼라
            dp[i*j] = False
            j += 1
# 카운트 및 출력
c = 0
for num in nl :
    if dp[num] != 0 :
        c += 1
print(c)