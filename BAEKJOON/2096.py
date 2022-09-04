'''
내려가기

N줄에 0이상 9이하 숫자가 세개씩 적혀있다.
첫 줄에서 시작해서 마지막 줄에 끝나게 된다.
먼저 처음에 적혀있는 세개 숫자 중 하나 선택.
다음 줄로 내려가는데, 바로 아래로 넘어가거나 바로 아래의 수와 붙어있는 수로만 이동 가능.
최소점수 최대점수를 구해라.

입력
N 제시. 1이상 10만이하
숫자 3개.
'''
'''
import sys
input = sys.stdin.readline

n = int(input())
v = [[0, 0], [0, 0], [0, 0]]
# a, b, c = map(int, input().split())
# v = [[min(a, b), max(a, b)], [min(a, b, c), max(a, b, c)], [min(b, c), max(b, c)]]
# print(v)
for i in range(n):
    a, b, c = map(int, input().split())
    m1, M1 = min(v[0][0] + a, v[1][0] + a), max(v[0][1] + a, v[1][1]+ a)
    m2, M2 = min(v[0][0] + b, v[1][0] + b, v[2][0] + b), max(v[0][1] + b, v[1][1] + b, v[2][1] + b)
    m3, M3 = min(v[1][0] + c, v[2][0] + c ), max(v[1][1] + c, v[2][1] + c)
    v[0][0], v[0][1] = m1, M1
    v[1][0], v[1][1] = m2, M2
    v[2][0], v[2][1] = m3, M3
    print(v)

print(v)
'''

import sys
input = sys.stdin.readline

n = int(input())
n1, n2, n3, n4, n5, n6 = 0, 0, 0, 0, 0, 0

for i in range(n):
    a, b, c = map(int, input().split())
    m1, M1 = a + min(n1, n3), a + max(n2, n4)
    m2, M2 = b + min(n1, n3, n5), b + max(n2, n4, n6)
    m3, M3 = c + min(n3, n5), c + max(n4, n6)
    n1, n2 = m1, M1
    n3, n4 = m2, M2
    n5, n6 = m3, M3
    print(n1, n2, n3, n4, n5, n6)

print(max(n2, n4, n6), min(n1, n3, n5))

'''
4
1 1 0
2 3 3
3 2 3
1 0 1

8 5
'''