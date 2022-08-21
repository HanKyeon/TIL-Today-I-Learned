'''
Z

2^n 2^n 배열 Z모양으로 탐색.
재귀적으로.

입력
2^N승 정사각형 1이상 15이하 N, R행 C열 찾으라고 범위 내 r, c

출력
r,c를 몇번째 방문했는지
'''
def Z((r1,c1), (r2,c2), (r3,c3), (r4,c4)):
    if r2-r1 == 1:
        

n, r, c = map(int, input().split())
g = [[0]*(2**n) for _ in range(2**n)]






'''

# 한줄만에 끝내버리신 philyai님의 풀이
# https://www.acmicpc.net/source/9479099

n,r,c=map(int,input().split());print(int(f'{c:b}',4)+2*int(f'{r:b}',4))


# 비트 연산으로 푸신 rapaeljin님의 풀이
# https://www.acmicpc.net/source/14942488

n, r, c = map(int, input().split())
s = 0
while n:
    n -= 1
    s += (r>>n<<1|c>>n)<<n+n
    r &= (1<<n)-1
    c &= (1<<n)-1
print(s)
'''