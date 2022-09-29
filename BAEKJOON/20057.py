'''
마법사 상어와 토네이도

토네이도 익힘.
n*n 격자 모래밭. r,c에 있는 숫자는 잇는 모래 양
토네이도 시전 시 중앙부터 토네이도 이동 시작. 토네이도는 한 번에 한 칸 이동.
토네이도가 한 칸 이동 할 때마다 모래는 일정한 비율로 흩날리게 된다.

75퍼센트가 다음칸이지만 나머지로 계산해야한다.
       2%
   10% 7% 1%
5% A%  Y <-X
   10% 7% 1%
       2%
A는 나머지. 숫자%는 // 연산자로 보내고, 그 값들을 Y에서 뺀 나머지가 A% 자리에 들어간다.
모래는 그때 그때 더해진다.

입력
격자 크기 n 제시. 3이상 499이하 홀수
그래프 제시.
시작점은 언제나 0

출력
격자 밖으로 나간 모래의 양 출력.
'''
from collections import deque
import sys
input = sys.stdin.readline

dh = [0, 1, 0, -1]
dw = [-1, 0, 1, 0]

def 슈우우우웃(sh, sw, di):
    global n, g
    if di == 0:
        didi = {(-1, 0):7, (1,0):7, (-1, 1):1, (1,1):1, (-1,-1):10, (1,-1):10, (0,-2):5, (2,0):2, (-2,0):2}
    elif di == 1:
        didi = {(0,1):7, (0,-1):7, (0,2):2, (0,-2):2, (-1, -1):1, (-1,1):1, (1,1):10, (1,-1):10, (2,0):5}
    elif di == 2:
        didi = {(-1,-1):1, (1,-1):1, (1,0):7, (-1,0):7, (2,0):2, (-2,0):2, (-1,1):10, (1,1):10, (0,2):5}
    elif di == 3:
        didi = {(1,1):1, (1,-1):1, (0,1):7, (0,-1):7, (0,2):2, (0,-2):2, (-1,1):10, (-1,-1):10, (-2,0):5}
    
    ret = 0
    val = g[sh][sw]
    for i in didi:
        ddh, ddw = i
        pct = didi[i]
        pval = int(g[sh][sw]*pct//100)
        nh, nw = sh+ddh, sw+ddw
        if 0<=nh<n and 0<=nw<n:
            g[nh][nw] += pval
        else:
            ret += pval
        val -= pval
    # 알파 처리
    nh, nw = sh+dh[di], sw+dw[di]
    if 0<=nh<n and 0<=nw<n:
        g[nh][nw] += val
    else:
        ret += val
    g[sh][sw] = 0
    # for kkk in g:
    #     print(kkk)
    # print('=======')
    return ret

def 회전회오리(mdh, mdw):
    global n, g, mid
    k = 1
    q = deque([(mdh, mdw, 0, 0)])
    ret = 0
    while q:
        h, w, cnt, di = q.popleft()
        if cnt == k:
            if di % 2:
                di = (di+1) % 4
                k += 1
            else:
                di += 1
            cnt = 0
        nh, nw = h+dh[di], w+dw[di]
        if 0<=nh<n and 0<=nw<n:
            if g[nh][nw]:
                ret += 슈우우우웃(nh, nw, di)
            q.append((nh, nw, cnt+1, di))
    return ret

n = int(input())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
mid = n//2
ans = 회전회오리(mid, mid)
print(ans)



'''
# 워메 빠른거

N = int(input())
left = [ (-2, 0, 0.02), (-1, 0, 0.07), (+1, 0, 0.07), (+2, 0, 0.02),(-1, +1, 0.01), (+1, +1, 0.01), (-1, -1, 0.1),
        (+1, -1, 0.1), (0, -2, 0.05)]
down = [(0, -2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (0, 2, 0.02), (-1, -1, 0.01), (-1, 1, 0.01), (1, -1, 0.1),
        (1, 1, 0.1), (2, 0, 0.05)]
right = [(-2, 0, 0.02), (-1, 0, 0.07), (1, 0, 0.07), (2, 0, 0.02), (-1, -1, 0.01), (1, -1, 0.01), (-1, 1, 0.1),
         (1, 1, 0.1), (0, 2, 0.05)]
up = [(0, -2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (0, 2, 0.02), (1, -1, 0.01), (1, 1, 0.01), (-1, -1, 0.1),
        (-1, 1, 0.1), (-2, 0, 0.05)]
def move(step, dx, dy, cnt):
    global x, y, flag
    for i in range(cnt):
        x += dx
        y += dy
        original = Map[x][y]
        Map[x][y] = 0
        temp = 0
        for ddx, ddy, ratio in step:
            nx, ny = x + ddx , y + ddy
            temp += int(original*ratio)
            if 0 <= nx < N and 0 <= ny < N:
                Map[nx][ny] += int(original*ratio)
        nx, ny = x +dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            Map[nx][ny] += (original - temp)
        if x == 0 and y == 0:
            flag = 1
            return

Map = [list(map(int, input().split())) for _ in range(N)]
total = sum([sum(x) for x in Map])
x, y = N // 2, N // 2
cnt = 1
flag = 0
while 1:
    # 왼쪽이동
    dx, dy = 0, -1
    move(left,dx, dy,cnt)
    if flag:
        break
    # 아래이동
    dx, dy = 1, 0
    move(down, dx, dy, cnt)
    #
    cnt += 1
    # 오른쪽이동
    dx, dy = 0, 1
    move(right, dx, dy, cnt)
    # 위이동
    dx, dy = -1, 0
    move(up, dx, dy, cnt)
    #
    cnt += 1
print(total - sum([sum(x) for x in Map]))
'''


















