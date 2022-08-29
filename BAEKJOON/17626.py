'''
Four Squares

모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현 할 수 있다고 증명하엿다. 어떤 자연수는 복수의 방법으로 표현이 가능.
자연수 n이 주어질 때, n을 최소 개수의 제곱수 합으로 표현하는 컴퓨터 프로그램을 작성하시오.

입력
n은 1이상 5만이하

출력
표준출력. 합이 n과 같게 되는 제곱수들의 최소 갯수를 한 줄에 출력.
'''

n = int(input())
dp = [0] + [int(10e9)]*n
zdp = [] # 최대 223
for i in range(1, int(n**(1/2))+1):
    zdp.append(i**2)
    dp[i**2] = 1


for i in range(1, n+1):
    for j in zdp:
        dp[i] = min(dp[i-1]+1, dp[i])
        if i+j <= n:
            dp[i+j] = min(dp[i+j], dp[i]+1)
print(dp[n])




'''
# 짱 빠른 코드
# 똑똑하다 진짜 ;;

from math import sqrt
from itertools import combinations_with_replacement

n = int(input())
square_num_li = [i*i for i in range(1, int(sqrt(n))+1)]
square_num_li_2 = [sum(k) for k in combinations_with_replacement(square_num_li, 2)]
square_num_set_2 = set(square_num_li_2)

def answer(n):
    if n in square_num_li: # 제곱수면
        return 1
    elif n in square_num_li_2: # 제곱수 두개를 더해서 만들 수 있는 수면
        return 2
    else:
        for square in square_num_li: # 제곱 수 중
            if n - square in square_num_set_2: # n에서 제곱수를 뺀 수가 제곱수 두개를 더해서 만들수 있는 수면
                return 3
    return 4

print(answer(n))
'''














