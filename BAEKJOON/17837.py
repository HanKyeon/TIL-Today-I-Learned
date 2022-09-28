'''
새로운 게임2

n*n 진행. 말의 갯수 k개. 말 업을 수 있다.
체스판의 각 칸은 흰, 빨, 파 중 하나로 색칠되어 있다.
게임은 체스판 위에 말 k개를 놓고 시작. 말은 1번부터 k까지 번호, 이동 방향은 사방으로 제시.
턴 1회는 1번 말부터 k번 말까지 순서대로 이동시키는 것. 한 말이 이동 할 때, 위에 올려져 있는 말도 함께 이동.
말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르다. 턴이 진행되던 중에 말이 4개 이상 쌓이면 게임 종료. 

A번 말이 이동하려는 칸이
1. 읜색인 경우 그 칸으로 이동. 이동하려는 칸에 말이 있는 경우, 가장 위에 A번 말을 둔다.
2. 빨간색인 경우, 이동 한 뒤 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
3. 파란색의 경우, A번말의 이동 방향을 반대로 하고 한 칸 이동한다. 방향을 반대로 바꾼 후 이동하려는 칸이 파랑인 경우 이동하지 않고 가만히 있는다. -> 방향만 바꾸면 될듯x 바닥판에 따라 작동도 시켜줘야함.
4. 체스판을 벗어나려하면 방향 돌리고 이동

입력
첫째 줄에 체스판 크기 n, 말 갯수 k 제시.
체스판 정보. 0흰 1빨 2파
k줄에 말 정보 제시.
행, 열, 이동방향. 1우 2좌 3상 4하

출력 게임이 종료되는 턴의 번호 출력. 그 값이 1000보다 크거나 절대로 게임이 종료되지 않는 경우 -1 출력
'''
import sys
input = sys.stdin.readline

def move(idx, h, w, di):
    nl = [] # 업은 애들 담을 변수
    while sts[h][w][-1] != idx: # 업는다
        nl.append(sts[h][w].pop())
    nl.append(sts[h][w].pop())
    nh, nw = h+dh[di], w+dw[di]
    # 가려는 칸이 하양
    if 0<=nh<n and 0<=nw<n and g[nh][nw] == 0:
        while nl:
            num = nl.pop()
            sts[nh][nw].append(num)
            mal[num][0], mal[num][1] = nh, nw
        if len(sts[nh][nw]) >= 4:
            return True
    # 가려는 칸이 빨강
    elif 0<=nh<n and 0<=nw<n and g[nh][nw] == 1:
        while nl:
            num = nl.pop(0)
            sts[nh][nw].append(num)
            mal[num][0], mal[num][1] = nh, nw
        if len(sts[nh][nw]) >= 4:
            return True
    # 가려는 칸이 파랑
    elif 0<=nh<n and 0<=nw<n and g[nh][nw] == 2:
        # 파랑은 방향 반대
        if di % 2:
            di -= 1
        else:
            di += 1
        mal[idx][2] = di
        bh, bw = h+dh[di], w+dw[di]
        # 돌아가려는 칸이 흰/빨/파일 경우,
        if 0<=bh<n and 0<=bw<n and g[bh][bw] == 0:
            while nl:
                num = nl.pop()
                sts[bh][bw].append(num)
                mal[num][0], mal[num][1] = bh, bw
            if len(sts[bh][bw]) >= 4:
                return True
        elif 0<=bh<n and 0<=bw<n and g[bh][bw] == 1:
            while nl:
                num = nl.pop(0)
                sts[bh][bw].append(num)
                mal[num][0], mal[num][1] = bh, bw
            if len(sts[bh][bw]) >= 4:
                return True
        elif 0<=bh<n and 0<=bw<n and g[bh][bw] == 2:
            while nl:
                num = nl.pop()
                sts[h][w].append(num)
                # mal[num][0], mal[num][1] = h, w
            if len(sts[h][w]) >= 4:
                return True
        elif not (0<=bh<n and 0<=bw<n):
            while nl:
                num = nl.pop()
                sts[h][w].append(num)
                # mal[num][0], mal[num][1] = h, w
            if len(sts[h][w]) >= 4:
                return True
    # 밖으로 나갈 경우. 파랑에서 밖으로 나가는 경우는 예외처리 하지 않았다.ㅎ
    elif not (0<=nh<n and 0<=nw<n):
        # 파랑은 방향 반대
        if di % 2:
            di -= 1
        else:
            di += 1
        mal[idx][2] = di
        bh, bw = h+dh[di], w+dw[di]
        # 돌아가려는 칸이 흰/빨/파일 경우,
        if 0<=bh<n and 0<=bw<n and g[bh][bw] == 0:
            while nl:
                num = nl.pop()
                sts[bh][bw].append(num)
                mal[num][0], mal[num][1] = bh, bw
            if len(sts[bh][bw]) >= 4:
                return True
        elif 0<=bh<n and 0<=bw<n and g[bh][bw] == 1:
            while nl:
                num = nl.pop(0)
                sts[bh][bw].append(num)
                mal[num][0], mal[num][1] = bh, bw
            if len(sts[bh][bw]) >= 4:
                return True
        elif 0<=bh<n and 0<=bw<n and g[bh][bw] == 2:
            while nl:
                num = nl.pop()
                sts[h][w].append(num)
                # mal[num][0], mal[num][1] = h, w
            if len(sts[h][w]) >= 4:
                return True
        elif not (0<=bh<n and 0<=bw<n):
            while nl:
                num = nl.pop()
                sts[h][w].append(num)
                # mal[num][0], mal[num][1] = h, w
            if len(sts[h][w]) >= 4:
                return True
    return False
dh = [0, 0, -1, 1]
dw = [1, -1, 0, 0]

n, k = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
mal = {}
sts = [[[] for _ in range(n)] for _ in range(n)]

for i in range(1, k+1):
    h, w, di = map(int, input().rstrip().split())
    mal[i] = [h-1, w-1, di-1]
    sts[h-1][w-1].append(i)

for i in range(1, 1002):
    for j in range(1, k+1):
        h, w, di = mal[j]
        fla = move(j, h, w, di)
        if fla:
            break
    # for sd in sts:
    #     print(sd)
    if fla:
        break
if i > 1000:
    i = -1
print(i)














