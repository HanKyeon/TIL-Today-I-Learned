'''
나머지 합

n개 수 제ㅅㅣ.
연속된 부분 구간합이 m으로 나누어 떨어지는 구간 갯수 구해라.

입력
n, m 제시.
n개 수 제시

출력
m으로 나누어 떨어지는 구간 갯수 출력
'''
import sys
from math import factorial
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
nl = list(map(int, input().rstrip().split()))
nmz = [0]*m
hap = 0
for i in nl:
    hap+=i
    hap%=m
    nmz[hap] += 1
ans = nmz[0]
for i in nmz:
    ans += i*(i-1)//2
print(ans)





