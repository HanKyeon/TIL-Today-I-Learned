'''
IOIOI

N+1개의 I와 N개의 O로 이루어져 있으면, I와 o가 교대로 나오는 문자열을 Pn이라 한다.
P1 = IoI
P2 = IoIoI
P3 = IOIOIOI
I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 Pn이 몇군데 포함되어 있는지 구하는 프로그램 작성.

입력
첫줄에 N 제시.
S의 길이 M 제시
S 제시

출력
S에 Pn이 몇군데나 포함되어 있는지 출력
'''
import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
s = input().rstrip()
ls = 2*n+1
ans = 0
i, c = 0, 0
while i < m-1:
    if s[i:i+3] == 'IOI':
        c += 1
        i += 2
        if c == n:
            ans += 1
            c -= 1
        continue
    i += 1
    c = 0
print(ans)

