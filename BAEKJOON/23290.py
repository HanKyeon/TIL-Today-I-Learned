'''
마법사 상어와 복제

4*4 격자에서 연습. 1,1에서 4,4 표현
물고기 m마리. 방향 보유. 8방향 중 하나.
상어도 격자의 한 칸에 들어가 있으며, 물고기들은 같은 칸에 존재 가능, 상어와 물고기 같은 칸 공생 가능.
복제 마법 진행
1. 상어가 복제마법 시전. 5번에서 물고기 복제되어 칸에 나타난다.
2. 모든 물고기가 한 칸 이동한다. 상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동 할 수 없다. 각 물고기는 자신이 가진 이동방향이 이동 할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전. 만약 이동 할 수 있는 칸이 없다면 이동 하지 않는다. 그 외의 경우엔 해당 칸으로 이동.
3. 상어가 연속 3칸 이동. 상하좌우 이동. 이동하는 칸 중 격자를 벗어난 칸이 있으면 불가능한 이동. 연속 이동 중 상어가 물고기가 있는 같은 칸으로 이동하게 된다면 그 칸에 있는 모든 물고기는 격자에서 제외되며, 제외되는 모든 물고기는 물고기 냄새를 남긴다. 가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동. 여러개라면 사전 순으로 가장 앞서는 방법 이용.
3-1. 사전 순이란, 상1 좌2 하3 우4 기준으로 사전순.
4. 두 턴 전 연습에서 생긴 물고기 냄새 사라짐.
5. 1에서 사용한 복제 마법 완료. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 보유.
격자에 있는 물고기의 위치, 방향 정보와 상어의위치, 연습 횟수 s 제시. s번 연습을 모두 마쳤을 때 격자의 물고기 수.

입력
물고기 수 m, 마법 연습 횟수 s 제시.
m개 줄 물고기 정보 제시. x, y, d는 좌표와 방향. 방향은 8이하의 자연수 표기
좌1 좌상2 상3 우상4 우5 우하6 하7 좌하8
상어 좌표 제시.

출력
S번 연습 이후 격자에 잇는 물고기 수 출력.
'''

import sys
input = sys.stdin.readline

# 좌0 상2 우4 하6
dh = [0, -1, -1, -1, 0, 1, 1, 1]
dw = [-1, -1, 0, 1, 1, 1, 0, -1]

def shamov(h, w, cnt, val, li):
    global sh, sw, saveat, eat
    if cnt == 3:
        if val > saveat:
            saveat = val
            eat = li[:]
            sh, sw = h, w
        return
    # li = li[:]
    for i in (2,0,6,4):
        nh, nw = h+dh[i], w+dw[i]
        if 0<=nh<4 and 0<=nw<4:
            if (nh, nw) in li:
                li.append((nh, nw))
                shamov(nh, nw, cnt+1, val, li)
            else:
                li.append((nh, nw))
                shamov(nh, nw, cnt+1, val+len(g[nh][nw]), li)
            li.pop()

def lego():
    global ans, n, m, fshdata, sh, sw, saveat, eat
    # 복제 및 초기화
    cdi = {}
    for i in range(4):
        for j in range(4):
            if g[i][j]:
                cdi[(i, j)] = g[i][j][:]
                g[i][j] = []
    # 이동
    for k in cdi:
        h, w = k
        for i in cdi[k]:
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<4 and 0<=nw<4 and not v[nh][nw] and (nh != sh or nw != sw):
                g[nh][nw].append(i)
                continue
            ndi, fla = i-1, False
            if ndi == -1:
                ndi = 7
            while ndi != i:
                nh, nw = h+dh[ndi], w+dw[ndi]
                if 0<=nh<4 and 0<=nw<4 and not v[nh][nw] and (nh != sh or nw != sw):
                    g[nh][nw].append(ndi)
                    fla = True
                    break
                ndi -= 1
                if ndi == -1:
                    ndi = 7
            if not fla:
                g[h][w].append(i)
    # for i in g:
    #     print(i)
    # print('===', "물고기 이동")

    # 상어 이동.
    shamov(sh, sw, 0, 0, [])
    for h, w in eat:
        if g[h][w]:
            ans -= len(g[h][w])
            g[h][w] = []
            v[h][w] = 3
    # for i in g:
    #     print(i)
    # print('===', "상어 이동")

    # 냄새 줄이기
    for i in range(4):
        for j in range(4):
            if v[i][j]:
                v[i][j] -= 1
    # for i in v:
    #     print(i)
    # print('===', "냄새 줄이기")
    
    # 복제!
    for i in cdi:
        h, w = i
        ans += len(cdi[i])
        g[h][w] += cdi[i]
    # for i in g:
    #     print(i)
    # print('===', "복제")

n, m = map(int, input().rstrip().split())
g = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
v = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for _ in range(n):
    h, w, di = map(int, input().rstrip().split())
    g[h-1][w-1].append(di-1)

sh, sw = map(int, input().rstrip().split())
sh, sw = sh-1, sw-1

ans = n
while m:
    eat, saveat = [], -1
    lego()
    m -= 1

print(ans)

# ---------
'''
# 마법사 상어와 복제
# https://www.acmicpc.net/problem/23290
# 재귀함수 /


import sys
input = sys.stdin.readline

M, S = map(int, input().split())

f_board = [[[0]*8 for _ in range(4)] for __ in range(4)]

def _int(n):
    return int(n)-1

for _ in range(M):
    fx, fy, fd = map(_int, input().split())
    f_board[fx][fy][fd] += 1

sx, sy = map(_int, input().split())

dx = [0, -1, -1, -1, 0, 1, 1, 1] # @@ 9번째 항목은 제자리 방향
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

sdx = [-1, 0, 1, 0]    # 상좌하우 순
sdy = [0, -1, 0, 1]

s_board = [[-3]*4 for _ in range(4)]
def move_fish():
    tmp_board = [[[0]*8 for _ in range(4)] for __ in range(4)]
    for x in range(4):
        for y in range(4):
            for d in range(8):
                if not f_board[x][y][d]:
                    continue
                dir = d
                for dm in range(8):
                    nd = (dir-dm) % 8
                    nx, ny = x+dx[nd], y+dy[nd]
                    if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or (s_board[nx][ny] >= round-2) or (nx==sx and ny==sy):
                        continue
                    tmp_board[nx][ny][nd] += f_board[x][y][d]
                    break
                else:
                    tmp_board[x][y][d] += f_board[x][y][d]
    return tmp_board

def move_shark():
    global sx, sy
    max_path = list()
    max_cnt = -1
    check = [[0]*4 for _ in range(4)]
    def recur(x, y, path, cnt):
        nonlocal max_cnt, max_path
        if len(path) == 3:
            if max_cnt < cnt:
                max_cnt = cnt
                max_path = [x for x in path]
            return

        for i in range(4):
            nx, ny = x+sdx[i], y+sdy[i]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                continue
            add = sum(f_board[nx][ny]) if not check[nx][ny] else 0  # @@ 왔다리 갔다리하면서 중복으로 선택하면 안되기때문에 check을 확인해야해
            check[nx][ny] += 1
            recur(nx, ny, path+[i], cnt+add)
            check[nx][ny] -= 1   # @@ 다시 후진하면서 내 흔적을 지워버림

    recur(sx, sy, [], 0)

    for d in max_path:
        nx, ny = sx+sdx[d], sy+sdy[d]
        if sum(f_board[nx][ny]): s_board[nx][ny] = round     # @@ 여기서 물고기 안먹은경우 냄새 남기면 안돼
        f_board[nx][ny] = [0] * 8   # 물고기 지우기
        sx, sy = nx, ny


if __name__ == "__main__":
    for round in range(S):
        copy_board = [[col[:] for col in row] for row in f_board]
        f_board = move_fish()
        move_shark()
        # 복제 마법
        for x in range(4):
            for y in range(4):
                for d in range(8):
                    f_board[x][y][d] += copy_board[x][y][d]
    
    answer = 0
    for x in range(4):
        for y in range(4):
            answer += sum(f_board[x][y])
    
    print(answer)
'''