'''
분수합

분수 A/B는 분자 A 분모 B인 분수 의미
두 분수의 합 또한 분수로 표현 가능. 분수 합을 기약분수 형태로 구해라.

입력
a, b
c, d

출력
분자 분모 뜻하는 자연수 빈 칸 두고 출력
'''
from math import gcd

a, b = map(int, input().split())
c ,d = map(int, input().split())
ja, mo = a*d+c*b, b*d
go = gcd(ja, mo)
print(ja//go, mo//go)

