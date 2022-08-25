'''
Z

2^n 2^n 배열 Z모양으로 탐색.
재귀적으로.

입력
2^N승 정사각형 1이상 15이하 N, R행 C열 찾으라고 범위 내 r, c

출력
r,c를 몇번째 방문했는지
'''
# 그냥 숫자로만 계산한 방법.
def Z(nh, nw, ln):
    global c, h, w, ans
    if nh == h and nw == w:
        ans = c
        return
    nn = ln//2
    # 책 읽는 순서대로
    if nh <= h < nh + nn and nw <= w < nw + nn:
        # print(c, "1")
        Z(nh, nw, nn) # 1 0 c = c + ln**2 * 0
    elif nh <= h < nh+nn and nw + nn <= w < nw+nn*2:
        c = c + (nn**2)
        # print(c, "2")
        Z(nh, nw+nn, nn) # 2 c = c + ln**2 * 1
    elif nh+nn <= h < nh + nn*2 and nw <= w < nw+nn:
        c = c + (nn**2) * 2
        # print(c, "3")
        Z(nh+nn, nw, nn) # 3 c = c + ln**2 * 2
    elif nh+nn <= h < nh + nn*2 and nw + nn <= w < nw+nn*2:
        c = c + (nn**2) * 3
        # print(c, "4")
        Z(nh+nn, nw+nn, nn) # 4 c = c + ln**2 * 3

n, h, w = map(int, input().split())
ans = 0
c = 0
Z(0, 0, 2**n)
print(ans)
# for i in g:
#     print(*i)

'''
# 하나하나 찍어가는 방법
def Z(nh, nw, ln):
    global c, h, w
    if g[h][w] != 0:
        return g[h][w]
    if ln == 1:
        g[nh][nw] = c
        c+=1
        return
    nn = ln//2
    # 책 읽는 순서대로
    Z(nh, nw, nn) # 1 0 c = c + ln**2 * 0
    Z(nh, nw+nn, nn) # 2 c = c + ln**2 * 1
    Z(nh+nn, nw, nn) # 3 c = c + ln**2 * 2
    Z(nh+nn, nw+nn, nn) # 4 c = c + ln**2 * 3

n, h, w = map(int, input().split())
g = [[0]*(2**n) for _ in range(2**n)]
c = 0
Z(0, 0, 2**n)
for i in g:
    print(*i)
'''


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