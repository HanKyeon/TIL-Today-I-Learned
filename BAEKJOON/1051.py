'''
숫자 정사각형

n*m 직사각형. 각 칸에는 한 자리 숫자 적혀 있음.
꼭짓점에 쓰여있는 수가 모두 같은 가장 큰 정사각형을 찾아라. 정사각형은 행열에 평행

입력
n, m 제시.
n개 줄 숫자 제시

출력
정사각형 크기 출력
'''
import sys
input = sys.stdin.readline

def check(h, w):
    global ans
    ret = 1
    nh, nw = h+1, w+1
    while 0<=nh<n and 0<=nw<m:
        if g[h][w]==g[h][nw]==g[nh][w]==g[nh][nw]: ret = (nh-h+1)**2
        nh, nw = nh+1, nw+1
    if ans < ret: ans = ret

n, m = map(int, input().rstrip().split())
g, ans = [list(map(int, list(input().rstrip()))) for _ in range(n)], 1
for i in range(n):
    for j in range(m):
        check(i, j)
print(ans)
