'''
통나무 옮기기

가로와 세로의 길이가 같은 평지에서 벌목을한다.
그 지형은 0과 1로 나타나있다. 1은 아직 잘려지지 않은 나무를 나타내고 0은 아무것도 없음이다.
통나무는 BBB이다. BBB에서 EEE로 옮길 것이다. 통나무의 길이는 항상 3이며, B의 갯수와 E의 갯수는 같다.
U 위로 한 칸
D 아래로 한 칸
L 왼쪽으로 한 칸
R 오른쪽으로 한 칸
T 90도 회전
움직일 위치에 1이 없어야 이동 가능. 한 번에 한 칸 씩만 이동 가능.
통나무의 길이는 항상 3이다.

입력
변의 길이 n
그래프 제시. 빈칸x

출력
최소 동작 횟수. 불가능 시 0
'''
from collections import deque
import sys
input = sys.stdin.readline

# mov = [(-1,0), (0,1), (1,0), (0,-1)]
dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

def findBE():
    global n, tdi
    for i in range(n):
        for j in range(n):
            if g[i][j] == 'B':
                g[i][j] = '0'
                tnm.append((i, j))
            elif g[i][j] == 'E':
                g[i][j] = '0'
                tgp.append((i, j))
    tnm.sort()
    tgp.sort()
    h, w = tgp[1][0], tgp[1][1]
    if tgp[0][0] == h: # h가 같으면
        v[h][w][0] = -1 # 가로 v에 -1
    else:
        v[h][w][1] = -1 # 세로 v에 -1
    if tnm[0][0] == tnm[1][0]: # h가 같다면
        return 0 # 가로
    else:
        return 1 # 세로

def check(h, w): # 회전 확인
    global n
    if h-1 < 0 or w-1 < 0:
        return False
    if h+1 >= n or w+1 >= n:
        return False
    for i in (h-1, h, h+1):
        for j in (w-1, w, w+1):
            if g[i][j] == '1':
                return False
    return True

def bfs():
    global n, tdi
    h, w = tnm[1][0], tnm[1][1]
    v[h][w][tdi] = 1
    q = deque([(h, w, tdi)])
    while q:
        h, w, di = q.popleft()
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if nh<0 or nw<0 or nh>=n or nw>=n:
                continue
            if di: # 세로
                if i%2: # 세로인데 좌우 굴리기
                    fla = True
                    for r in (nh-1, nh, nh+1):
                        if r<0 or r>=n:
                            fla = False
                            break
                        if g[r][nw] != '0':
                            fla = False
                            break
                    if fla and v[nh][nw][di] <= 0:
                        if v[nh][nw][di] == -1:
                            return v[h][w][di]
                        v[nh][nw][di] = v[h][w][di]+1
                        q.append((nh, nw, di))
                else:
                    nnh, nnw = nh+dh[i], nw+dw[i]
                    if 0<=nnh<n and 0<=nnw<n and v[nh][nw][di]<=0 and g[nnh][nnw] == '0':
                        if v[nh][nw][di] == -1:
                            return v[h][w][di]
                        v[nh][nw][di] = v[h][w][di]+1
                        q.append((nh, nw, di))
            else: # 가로
                if i%2: # 가로인데 좌우 이동
                    nnh, nnw = nh+dh[i], nw+dw[i]
                    if 0<=nnh<n and 0<=nnw<n and v[nh][nw][di]<=0 and g[nnh][nnw] == '0':
                        if v[nh][nw][di] == -1:
                            return v[h][w][di]
                        v[nh][nw][di] = v[h][w][di]+1
                        q.append((nh, nw, di))
                else:
                    fla = True
                    for c in (nw-1, nw, nw+1):
                        if c<0 or c>=n:
                            fla = False
                            break
                        if g[nh][c] != '0':
                            fla = False
                            break
                    if fla and v[nh][nw][di] <= 0:
                        if v[nh][nw][di] == -1:
                            return v[h][w][di]
                        v[nh][nw][di] = v[h][w][di]+1
                        q.append((nh, nw, di))
        # 회전
        ndi = (di+1)%2
        if check(h, w) and v[h][w][ndi]<=0:
            if v[h][w][ndi] == -1:
                return v[h][w][di]
            v[h][w][ndi] = v[h][w][di]+1
            q.append((h, w, ndi))
    return 0

n = int(input())
g = [list(input().rstrip()) for _ in range(n)]
v = [[[0,0] for _ in range(n)] for _ in range(n)]
tnm, tgp = [], []
tdi = findBE() # 통나무 방향
print(bfs())




