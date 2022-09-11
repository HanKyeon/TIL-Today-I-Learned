'''
낚시왕

r c 상어 낚시. 칸당 최대 상어 1마리. 크기/속도 보유. 한 칸에 같은 상어 존재 시 가장 큰 녀석만 살아남는다. -> 딕트로 좌표 부르면 될듯

낚시왕은 밖에서 시작.
1. 낚시왕이 오른쪽으로 한 칸 이동
2. 낚시왕이 있는 열에 있는 상어 중 땅과 가장 가까운 상어 잡아먹기. 격자판의 상어 사라짐.
3. 상어 이동

상어는 주어진 속도로 이동하고 칸/초. 이동하려는 칸이 격자판의 경계를 넘는 경우 방향을 반대로 바꿔서 속력을 유지한 채로 이동.

입력
r, c , m. 2이상 100이하 . r c r*c 이하 m
상어의 정보 m줄 제시.
r c s d z (좌표 내, 0이상 1000이하 s 1이상 4이하 d 1이상 10000이하 z)
r, c 는 좌표 s는 속력 d는 방향 z는 크기. 1상 2하 3우 4좌
같은 칸에 멈출 시 젤 큰 상어가 잡아먹음. 같은 크기는 없으며 한 칸에 상어 하나만.

출력
낚시왕이 잡은 상어 크기의 합
'''
from collections import deque
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
# 상 하 우 좌
dh = [-1, 1, 0, 0]
dw = [0, 0, 1, -1]

R, C, m = map(int, input().rstrip().split())
q = deque([[0]])
sha = {}
lisha = set()
for _ in range(m):
    r, c, s, d, z = map(int, input().rstrip().split()) # 좌표r,c 속도s 방향d 크기z
    q.append((r-1, c-1, s, d-1, z))
    if sha.get((r-1, c-1), 0):
        sha[(r-1, c-1)].append(z)
    else:
        sha[(r-1, c-1)] = [z]
    lisha.add(z)
ans = 0

def sharkmove(h, w, di, s):
    global R, C
    nh, nw = h + dh[di]*s, w + dw[di]*s
    if 0<=nh<R and 0<=nw<C:
        return (nh, nw, di)
    nh, nw = abs(nh), abs(nw)
    if di == 2 or di == 3:
        di = 2
    elif di == 1 or di == 0:
        di = 1
    nh %= (2*(R-1))
    nw %= (2*(C-1))
    if nh > R-1:
        nh = (R-1) - (nh - (R-1))
        di = 0
    if nw > C-1:
        nw = (C-1) - (nw - (C-1))
        di = 3
    
    return (nh, nw, di)

while q:
    info = q.popleft()
    # print(info, '======info======')
    if len(info) == 1: # 낚시왕 행동
        tg = info[0]
        ret = 0
        for i in range(R):
            if sha.get((i, tg), 0):
                # print(sha[(i, tg)], "=======먹을거 고를 리스트========")
                ret = max(sha[(i, tg)])
                ans += ret
                # print(ret, '이거 먹음')
                # print((i, tg), ret, "여기 있는거 먹음")
                break
        if tg == C-1:
            break
        lisha = set()
        for k, v in sha.items():
            if max(v) == ret:
                continue
            lisha.add(max(v))
        q.append([tg+1])
        sha = {}
        # print(sha, lisha, '====현재 상어 좌표, 산 상어들====')
        continue
    if len(info) == 5:
        r, c, s, d, z = info
        if not z in lisha:
            continue
        nr, nc, nd = sharkmove(r, c, d, s)
        if sha.get((nr, nc), 0):
            sha[(nr, nc)].append(z)
        else:
            sha[(nr, nc)] = [z]
        q.append((nr, nc, s, nd, z))
        # print(nr, nc, s, nd, z)

    # print(sha, lisha, '====현재 상어 좌표, 산 상어들====')

print(ans)


'''
빠른 코드


백준 17143번 낚시왕
삼성

import sys
input = sys.stdin.readline
R, C, M = map(int, input().split())
board = [[ 0 for _ in range(C)] for _ in range(R)]


def fishing(i):
    ret = 0
    for j in range(R):
        if board[j][i]:
            ret = board[j][i][-1]
            board[j][i] = 0
            break
    return ret

# new

moving_chart = []
moving_chart.append(list(range(R)) + list(range(R-2,0,-1)))
moving_chart.append(list(range(C)) + list(range(C-2,0,-1)))

for _ in range(M): 
    r,c,s,d,z = map(int, input().split())
    r -= 1
    c -= 1
    if d == 1 or d == 2:
        if d == 1:
            i = 2 * (R - 1) - r
        else:
            i = r
        d = 0
    else:
        if d == 4:
            i = 2 * (C - 1) - c
        else:
            i = c
        d = 1
    board[r][c] = (s,d,i,z)

def move():
    temp_board = [[ 0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] == 0:
                continue
            s = board[i][j][0]
            d = board[i][j][1]
            idx = board[i][j][2]
            z = board[i][j][3]

            temp_i = i
            temp_j = j
            if d == 0:
                idx = (idx + s) % len(moving_chart[d])
                temp_i = moving_chart[d][idx]
            else:
                idx = (idx + s) % len(moving_chart[d])
                temp_j = moving_chart[d][idx]
            
            if temp_board[temp_i][temp_j]:
                temp_board[temp_i][temp_j] = max((s,d,idx,z), temp_board[temp_i][temp_j], key=lambda x:x[-1])
            else:
                temp_board[temp_i][temp_j] = (s,d,idx,z)
    
    return temp_board

ans = 0
for i in range(C):
    ans += fishing(i)
    board = move()

print(ans)
'''

















