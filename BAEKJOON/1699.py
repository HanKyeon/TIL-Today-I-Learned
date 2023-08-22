'''
제곱수의 합

주어진 자연수 n을 제곱수들의 합으로 표현할 때 그 항의 최소 갯수를 구하시오

입력
n 제시

출력
제곱수 항 최소 갯수 출력
'''
n = int(input())
dp = list(range(n+1))
for i in range(1, int(n**0.5)+1):
    dp[i**2] = 1
for i in range(1, n+1):
    for j in range(1, int(i**0.5)+1):
        if dp[i] > dp[i-j**2]+1:
            dp[i] = dp[i-j**2]+1
print(dp[n])

'''
# 빠른 코드
N = int(input())
def sum_of_squares(n):
    while n%4 == 0 and n > 0:
        n = n // 4
    if n%8 == 7:
        return 4
    if n - int(n**0.5)**2 == 0:
        return 1
    for j in range(2, int(n ** (1/2))+1):
        if n%j == 0:
            factor = [j, 0]
            while n%j == 0:
                n = n//j
                factor[1] += 1
            if factor[0]%4 == 3 and factor[1]%2 == 1:
                return 3
    else:
        if n%4 == 3:
            return 3
    return 2
print(sum_of_squares(N))
'''
