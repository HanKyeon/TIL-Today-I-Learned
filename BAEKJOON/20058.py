'''
마법사 상어와 파이어스톰

마법사 상어는 파이어볼과 토네이도를 조합해 파이어스톰을 시전 할 수 있다.
2**n 2**n 얼음 격자에서 진행. r, c에 각각 얼음 양 제시. 0인 경우 얼음이 없는 것.
파이어 스톰 단계 L을 결정해야 한다.
파이어스톰을 먼저 2**L 2**L 부분 격자로 나눈다. 그 후 모든 부분 격자를 시계 방향으로 90도 회전시킨다. 이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다. 인접은 사방.

파이어스톰을 Q번 시전 했을 때,
1. 남아있는 얼음의 합
2. 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 갯수
구하시오.

입력
n, q 제시.
2**n 줄에 얼음판 제시.
상어가 시전한 단계 연속 제시

출력
남아있는 얼음
가장 큰 덩어리가 차지하는 칸의 갯수. 남은게 없으면 0
'''
from collections import deque
import sys
input = sys.stdin.readline

def fireStorm(lv):
    global n, siz
    if lv == 0:
        return
    stp = 2**lv
    for i in range(0, siz, stp):
        for j in range(0, siz, stp):
            ng = [[0]*stp for _ in range(stp)]
            for k in range(stp):
                for l in range(stp):
                    ng[k][l] = g[i+stp-1-l][j+k]
            for nn in range(stp):
                g[i+nn][j:j+stp] = ng[nn]

def melt():
    global n, siz, g
    ng = []
    for i in g:
        ng.append(i[:])
    for i in range(siz):
        for j in range(siz):
            if ng[i][j] == 0:
                continue
            cnt = 0
            for k in range(4):
                nh, nw = i+dh[k], j+dw[k]
                if 0<=nh<siz and 0<=nw<siz and g[nh][nw]:
                    cnt += 1
            if cnt < 3:
                ng[i][j] -= 1
    g = []
    for i in ng:
        g.append(i[:])

def bfs():
    global n, siz, g
    v = [[0]*siz for _ in range(siz)]
    ret = 0
    for i in range(siz):
        for j in range(siz):
            if g[i][j] == 0:
                continue
            if v[i][j]:
                continue
            q = deque([(i, j)])
            v[i][j] = 1
            cnt = 1
            while q:
                h, w = q.popleft()
                for i in range(4):
                    nh, nw = h+dh[i], w+dw[i]
                    if 0<=nh<siz and 0<=nw<siz and g[nh][nw] and not v[nh][nw]:
                        v[nh][nw] += 1
                        q.append((nh, nw))
                        cnt += 1
            ret = max(ret, cnt)
    return ret
dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

n, m = map(int, input().rstrip().split())
siz = 2**n
g = [list(map(int, input().rstrip().split())) for _ in range(siz)]
ml = list(map(int, input().rstrip().split()))

for i in ml:
    fireStorm(i)
    melt()
ans1 = sum(map(sum, g))
ans2 = bfs()
print(ans1)
print(ans2)




'''
# 배열 돌리기
def turn90(g) :
    l = len(g)
    g9 = [[0] * n for _ in range(n)]
    for i in range(l) :
        for j in range(l) :
            g9[i][j] = g[l-1-j][i]
    return g9
'''
'''
# 빠름

from collections import deque
import copy

N, Q = map(int, input().split())
n = 2 ** N

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

board = [[0] * n for _ in range(n)]
L = []

for i in range(n):
    board[i] = list(map(int, input().split()))

L = list(map(int, input().split()))

def rotate(board, L):
    # 1. 90도로 회전
    l = 2 ** L
    l_board = [[0] * l for _ in range(l)]

    r, c = 0, 0
    
    for i in range(n // l):
        for j in range(n // l):
            r, c = l * i, l * j
            for l_r in range(l):
                for l_c in range(l):
                    l_board[l_r][l_c] = board[r + l_r][c + l_c]

            for l_r in range(l):
                for l_c in range(l):
                    board[r + l_c][c + l - l_r - 1] = l_board[l_r][l_c]
    
    # 2. 얼음 줄어들게
    melting_list = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                continue

            cnt = 0

            for _ in range(4):
                r = i + dr[_]
                c = j + dc[_]

                if r < 0 or c < 0 or r >= n or c >= n:
                    continue

                if board[r][c] > 0:
                    cnt += 1

            if cnt < 3:
                melting_list.append((i, j))

    for i, j in melting_list:
        board[i][j] -= 1

def max_area(board):
    visited = [[False] * n for _ in range(n)]
    ice = deque()
    ret = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] != 0:
                visited[i][j] = True
                ice.append((i, j))
                cnt = 1

                while ice:
                    r, c = ice.popleft()

                    for _ in range(4):
                        nr = r + dr[_]
                        nc = c + dc[_]

                        if nr < 0 or nc < 0 or nr >= n or nc >= n:
                            continue

                        if board[nr][nc] != 0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            ice.append((nr, nc))
                            cnt += 1

                ret = max(cnt, ret)

    return ret

for stage in L:
    rotate(board, stage)

print(sum(sum(board, [])))
print(max_area(board))
'''




