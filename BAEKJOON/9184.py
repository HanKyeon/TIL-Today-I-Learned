'''
신나는 함수 실행

재귀함수 w(a, b, c)
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

시간 오래 걸린다. w(a, b, c) 출력해라.
'''
import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())
ans = 0

print(f"w({a}, {b}, {c}) = {ans}")
