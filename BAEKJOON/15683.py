'''
감시

n*m 직사각형. k개의 cctv.
cctv 종류 5개.
1번 : 한쪽만
2번 : 한쪽과 반대측만
3번 : 한쪽과 바로 90도쪽만.
4번 : 한쪽 빼고 다.
5번 : 상하좌우

cctv는 감시 할 수 있는 방향에 있는 칸 전체를 감시 할 수 있다. cctv는 벽 통과 못한다.
cctv가 감시 할 수 없는 지역이 사각지대.
cctv는 회전이 가능. 회전은 90도로만.

사무실 크기, 상태, cctv 정보가 주어졌을 때, cctv의 방향을 적절히 정해서 사각지대의 최소 크기를 구하는 프로그램을 작성하시오.

입력
n, m 제시. 1이상 8이하.
사무실 정보 제시. cctv는 최대 8대. 6은 벽.
'''
import sys
input = sys.stdin.readline

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

def cl(h, w, di, pm):
    global n, m, v, g
    nh, nw = h+dh[di], w+dw[di]
    if 0<=nh<n and 0<=nw<m and g[nh][nw]!=6:
        v[nh][nw] += pm
        cl(nh, nw, di, pm)

def setcam(idx):
    global ans
    if idx == len(cam):
        ret = 0
        for i in v:
            ret += i.count(0)
        ans = min(ans, ret)
        return
    h, w, typ = cam[idx]
    if typ == 5:
        for i in range(4):
            cl(h, w, i, 1)
        setcam(idx+1)
    elif typ == 4:
        for i in range(4):
            cl(h, w, i, 1)
        for i in range(4):
            cl(h, w, i, -1)
            setcam(idx+1)
            cl(h, w, i, 1)
        for i in range(4):
            cl(h, w, i, -1)
    elif typ == 3:
        for i, j in ((0,1), (1,2), (2,3), (3,0)):
            cl(h, w, i, 1)
            cl(h, w, j, 1)
            setcam(idx+1)
            cl(h, w, i, -1)
            cl(h, w, j, -1)
    elif typ == 2:
        for i, j in ((0,2), (1,3)):
            cl(h, w, i, 1)
            cl(h, w, j, 1)
            setcam(idx+1)
            cl(h, w, i, -1)
            cl(h, w, j, -1)
    else:
        for i in range(4):
            cl(h, w, i, 1)
            setcam(idx+1)
            cl(h, w, i, -1)

n, m = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
cam = []
for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            continue
        if g[i][j] == 6:
            v[i][j] = 1000
            continue
        cam.append((i, j, g[i][j]))
        v[i][j] = 1000
ans = int(10e9)
setcam(0)
print(ans)














