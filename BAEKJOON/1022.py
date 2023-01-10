'''
소용돌이 예쁘게 출력하기

크기가 무한인 정사각형 모눈종이. 행과 열로 표현. 소용돌이 모양으로 채울 것. 중앙에 숫자 적고 우측에 2 쓰고 반시계 방향으로 돌리기.
출력 할 때 공백을 이용해 글자 수를 맞춘다.

입력
r1,c1,r2,c2 제시. r1c1은 좌상단 r2c2는 우하단

출력
소용돌이 옙브게 출력
'''
import sys
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
r1,c1,r2,c2 = map(int,input().split())
g = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]
mc = (c2-c1+1) * (r2-r1+1)
di = 1
x,y,cnt,l = 0,0,1,1
while mc > 0:
    for _ in range(2):
        for _ in range(l):
            if r1 <= x <= r2 and c1 <= y <= c2:
                g[x - r1][y - c1] = cnt
                mc -= 1
                m = cnt
            x += dx[di]
            y += dy[di]
            cnt += 1
        di = (di-1) % 4
    l += 1
max_len = len(str(m))
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(g[i][j]).rjust(max_len), end=" ")
    print()


'''
짱빠름

def value(x,y):
	if abs(x) > abs(y):
		if x > 0:
			return str(pow((2*x-1),2)+x-y)
		else:
			return str(pow((2*x-1),2)+3*x+y)
	else:
		if y > 0:
			return str(pow((2*y+1),2)-y+x)
		else:
			return str(pow((2*y+1),2)-3*y-x)

y1,x1,y2,x2 = map(int,input().split())
y0 = y2 - y1 + 1
x0 = x2 - x1 + 1

A = []
for y in range(y0):
	B = []
	for x in range(x0):
		B.append(value(x1+x,y1+y))
	A.append(B)

C = []
a = 0
for y in range(y0):
	for x in A[y]:
		if a < len(x):
			a = len(x)
	C.append(a)
c = 0
for i in C:
	if c < i:
		c = i		

for y in range(y0):
	for x in range(x0):
		A[y][x] = " " * (c - len(A[y][x])) + A[y][x]

for y in range(y0):
	print(*A[y])
'''



'''
메모리 초과

import sys
from collections import deque
input = sys.stdin.readline

def lego():
    global n
    q = deque([(n//2, n//2+1, 0)])
    g[n//2][n//2], g[n//2][n//2+1] = 1, 2
    while q:
        h, w, di = q.popleft()
        if di == 3:
            nh, nw = h+mov[0][0], w+mov[0][1]
        else:
            nh, nw = h+mov[di+1][0], w+mov[di+1][1]
        if 0<=nh<n and 0<=nw<n:
            if g[nh][nw]:
                nh, nw = h+mov[di][0], w+mov[di][1]
                if 0<=nh<n and 0<=nw<n:
                    g[nh][nw] = g[h][w]+1
                    q.append((nh, nw, di))
            else:
                g[nh][nw] = g[h][w]+1
                if di+1 == 4:
                    q.append((nh, nw, 0))
                else:
                    q.append((nh, nw, di+1))
def mkstr(x):
    global mxln
    x = str(x)
    while len(x) < mxln:
        x = " "+x
    return x
mov = [(-1,0),(0,-1),(1,0),(0,1)]
r1,c1,r2,c2 = map(int, input().rstrip().split())
if not r1 and not c1 and not r2 and not c2:
    print(1)
    exit()
n = max(map(abs, [r1,c1,r2,c2]))*2+1
r1,c1,r2,c2 = map(lambda x: x+n//2, [r1,c1,r2,c2])
g = [[0]*n for _ in range(n)]
lego()
mxln = len(str(n**2))
for i in range(r1, r2+1):
    apd = g[i][c1:c2+1]
    apd = list(map(mkstr, apd))
    print(*apd)
'''