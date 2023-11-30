'''
최소공배수

정수 B에 0보다 큰 정수인 N을 곱해 A를 만들 수 있다면 A는 B의 배수이다.
두 수에 대해 최소 공배수를 구해라.

입력
a, b 제시

출력
A,B의 최소 공배수 한 줄 출력
'''
from math import lcm
print(lcm(*map(int, input().split())))
