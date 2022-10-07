'''
구슬 탈출

스타트 링크에서 판매하는 어린이용 장난감 중에서 가장 인기 많은 제품은 구탈
이리저리 해서 빨간 구슬을 빼내는데 파랑도 같이 빼면 안됨.
기울이기만 가능.
10번 이하로 빨간 구슬 뺄 수 있는가?

입력
n, m 제시.
그래프 제시.
.은 빈 칸
#은 벽
O는 구멍
R, B는 구슬

출력
10번 이내로 빨간 구슬만 뺄 수 있으면 1, 없으면 0
'''
from collections import deque
import sys
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]

def bfs():
    global rh, rw, bh, bw, n, m
    v = {(rh, rw, bh, bw)}
    q = deque([(rh, rw, bh, bw, 0)])
    while q:
        rh, rw, bh, bw, cnt = q.popleft()
        if cnt > 10:
            return 0
        for dh, dw in mov:
            nbh, nbw = bh+dh, bw+dw
            while g[nbh][nbw] == '.':
                nbh += dh
                nbw += dw
            if g[nbh][nbw] == 'O':
                continue
            if g[nbh][nbw] == '#':
                nbh -= dh
                nbw -= dw
            nrh, nrw = rh+dh, rw+dw
            while g[nrh][nrw] == '.':
                nrh += dh
                nrw += dw
            if g[nrh][nrw] == '#':
                nrh -= dh
                nrw -= dw
            if g[nrh][nrw] == 'O':
                if cnt < 10:
                    return 1
                else:
                    return 0
            if nrh == nbh and nrw == nbw:
                if abs(rh-nrh)+abs(rw-nrw) > abs(bh-nbh)+abs(bw-nbw):
                    nrh, nrw = nrh-dh, nrw-dw
                else:
                    nbh, nbw = nbh-dh, nbw-dw
            if (nrh,nrw,nbh,nbw) in v:
                continue
            else:
                v.add((nrh, nrw, nbh, nbw))
                q.append((nrh, nrw, nbh, nbw, cnt+1))
    return 0

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
print(bfs())

'''
6 7
#######
#R....#
#.....#
#..O..#
#..B..#
#######
3 5
#####
#OBR#
#####
5 7
#######
#.RB###
#.#.#O#
#.....#
#######

11 13
#############
#.RB#########
#.#.........#
#.#.#######.#
#.#.#.....#.#
#.#.#..O#.#.#
#.#.#####.#.#
#.#.......#.#
#.#########.#
#...........#
#############
'''