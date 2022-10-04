'''
로봇

많은 공장에서 로봇 이용중. 로봇은 바라보는 방향으로 궤도를 따라 움직이며 방향은 동서남북.
로봇 이동 제어 명령어는 두가지.

명령1. Go k : k는 1, 2, 3 중 하나. 현재 방향으로 k칸만큼 이동.
명령2. Turn dir : dir은 left 또는 right이며, 각각 왼쪽 또는 오른쪽으로 90도 회전.

공장 내 궤도가 설치되어 있는 그래프 입력.
0은 궤도가 깔려있어 로봇이동 가능, 1은 벽

로봇의 현재 위치와 바라보는 방향이 제시되었을 때, 로봇을 원하는 위치로 이동시키고, 원하는 방향으로 바라보도록 하는데 최소 몇 번의 명령이 필요한지 구해라.

입력
n, m 제시.
그래프 제시.
로봇 출발 지점 위치, 방향 제시.
도착지점 위치, 바라보는 방향 제시.
동1 서2 남3 북4
'''
from collections import deque
import sys
input = sys.stdin.readline

cgdi = [1, 3, 2, 0]
dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

def bfs():
    while q:
        h, w, di, dep = q.popleft()
        for i in range(1, 4):
            nh, nw = h+dh[di]*i, w+dw[di]*i
            if 0<=nh<n and 0<=nw<m and not g[nh][nw] and not v[nh][nw][di]:
                v[nh][nw][di] = dep+1
                q.append((nh, nw, di, dep+1))
            if 0<=nh<n and 0<=nw<m and g[nh][nw]:
                break
        rdi, ldi = (di+1)%4, (di-1)%4
        if not v[h][w][rdi]:
            v[h][w][rdi] = dep+1
            q.append((h, w, rdi, dep+1))
        if not v[h][w][ldi]:
            v[h][w][ldi] = dep+1
            q.append((h, w, ldi, dep+1))
        if v[eh][ew][edi]:
            return v[eh][ew][edi]-1

n, m = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
sh, sw, sdi = map(int, input().rstrip().split())
sh, sw, sdi = sh-1, sw-1, cgdi[sdi-1]
eh, ew, edi = map(int, input().rstrip().split())
eh, ew, edi = eh-1, ew-1, cgdi[edi-1]
v = [[[0,0,0,0] for _ in range(m)] for _ in range(n)]
q = deque([(sh, sw, sdi, 1)])
v[sh][sw][sdi] = 1
print(bfs())
