'''
2n 타일링2

1*2 2*1 2*2 타일로 2*n 타일을 채우는 방법의 수

입력
n 제시

출력
2n 크기 직사각형을 채우는 방법의 수를 10007로 나눈 나머지 출력.
'''

n = int(input())
dp = [0]*(n+1)
dp[1] = 1
if n >= 2:
    for i in range(2, n+1):
        if i%2 == 1:
            dp[i] = dp[i-1]*2-1
        else:
            dp[i] = dp[i-1]*2+1

print(dp[n]%10007)