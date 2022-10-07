'''
구슬 탈출3

구슬탈출 1, 2와 같다.
단, 최소 몇 번만에 빼낼 수 있는지, 어떻게 기울여야 하는지 구해야 한다.

'''
from collections import deque
import sys
input = sys.stdin.readline

# mov = [(-1,0), (0,1), (1,0), (0,-1)]
dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]
dct = {0:'U', 1:'R', 2:'D', 3:'L'}

def bfs():
    global rh, rw, bh, bw, n, m
    v = {(rh, rw, bh, bw)}
    q = deque([(rh, rw, bh, bw, '')])
    while q:
        rh, rw, bh, bw, cnt = q.popleft()
        if len(cnt) > 10:
            return '-1'
        for i in range(4):
            nbh, nbw = bh+dh[i], bw+dw[i]
            while g[nbh][nbw] == '.':
                nbh += dh[i]
                nbw += dw[i]
            if g[nbh][nbw] == 'O':
                continue
            if g[nbh][nbw] == '#':
                nbh -= dh[i]
                nbw -= dw[i]
            nrh, nrw = rh+dh[i], rw+dw[i]
            while g[nrh][nrw] == '.':
                nrh += dh[i]
                nrw += dw[i]
            if g[nrh][nrw] == '#':
                nrh -= dh[i]
                nrw -= dw[i]
            if g[nrh][nrw] == 'O':
                if len(cnt)+1 > 10:
                    return '-1'
                return cnt+dct[i]
            if nrh == nbh and nrw == nbw:
                if abs(rh-nrh)+abs(rw-nrw) > abs(bh-nbh)+abs(bw-nbw):
                    nrh, nrw = nrh-dh[i], nrw-dw[i]
                else:
                    nbh, nbw = nbh-dh[i], nbw-dw[i]
            if (nrh,nrw,nbh,nbw) in v:
                continue
            else:
                v.add((nrh, nrw, nbh, nbw))
                q.append((nrh, nrw, nbh, nbw, cnt+dct[i]))
    return '-1'

n, m = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]
rh, rw, bh, bw = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if g[i][j] == '#' or g[i][j] == '.':
            continue
        if g[i][j] == 'R':
            rh, rw = i, j
            g[i][j] = '.'
        elif g[i][j] == 'B':
            bh, bw = i, j
            g[i][j] = '.'
ans = bfs()
if ans == '-1':
    print(ans)
else:
    print(len(ans))
    print(ans)