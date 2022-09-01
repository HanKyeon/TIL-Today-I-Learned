'''
조합

nCm 출력

입력
n, m 제시

출력
nCm 출력
'''
# nCr 공식 알면 끝
# n!/(n-r)!r!

from math import factorial

n, m = map(int, input().split())
print(int(factorial(n)//(factorial(n-m)*factorial(m))))
