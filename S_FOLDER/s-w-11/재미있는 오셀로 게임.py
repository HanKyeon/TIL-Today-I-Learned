'''
재미있는 오셀로 게임

보드에 돌 놔서 보드에 내 돌 많으면 승리.
돌은 중앙에 wb wb 놓고 시작함. 흑/백 번갈아가며 돌 놓기.
1. 돌과 돌 사이에 남의 돌 있어야 둘 수 있고, 남 돌 내 돌.
번갈아가며 흑, 백이 돌 놓는다.
보드에 빈 곳이 없더라 양 플레이어 모드 돌을 놓을 곳이 없으면 게임 끝.
그 때 보드에 있는 돌의 갯수가 많은 사람 승.

입력
테케T
보드 길이N 돌 놓기 횟수 M
M줄에 돌 놓을 위치, 돌 색.
1이면 흑 2면 백
3 2 1이면 3 2에 흑돌

출력
테케마다 겜 끝난 후 흑돌 백돌 갯수 출력.
'''
# 그냥 깡 계산

dh = [-1, -1, -1, 1, 1, 1, 0, 0]
dw = [1, 0, -1, 1, 0, -1, 1, -1]

def cal(h, w, bw):
    global n
    wb = 1 if bw == 2 else 2
    def way(hh, ww, di):
        li = [(hh, ww)]
        fla = False
        nh, nw = hh+dh[di], ww+dw[di]
        while 0<=nh<n and 0<=nw<n:
            if (nh,nw) not in blwh[bw] and (nh,nw) not in blwh[wb]:break
            if (nh,nw) in blwh[wb]:
                li.append((nh, nw))
            if (nh,nw) in blwh[bw]:
                fla = True
                break
            nh, nw = nh+dh[di], nw+dw[di]
        if fla:
            blwh[bw].update(li)
            while li:
                a = li.pop()
                # blwh[bw].add(a)
                if a in blwh[wb]:
                    blwh[wb].remove(a)
    blwh[bw].add((h, w))
    for i in range(8):
        nh, nw = h+dh[i], w+dw[i]
        if 0<=nh<n and 0<=nw<n and (nh, nw) in blwh[wb]:
                way(nh, nw, i)

for testcase in range(1, int(input())+1):
    n, m = map(int, input().rstrip().split())
    blwh = [0, {(n//2, n//2-1), (n//2-1, n//2)}, {(n//2, n//2), (n//2-1, n//2-1)}]
    for _ in range(m):
        a, b, bw = map(int, input().rstrip().split())
        cal(a-1, b-1, bw)
    print(f"#{testcase} {len(blwh[1])} {len(blwh[2])}")





'''
# 무난쓰 구현

dh = [-1, -1, -1, 1, 1, 1, 0, 0]
dw = [1, 0, -1, 1, 0, -1, 1, -1]

def bfs(h, w, bw):
    global n
    def way(h, w, di, bw):
        li = [(h, w)]
        fla = False
        nh, nw = h+dh[di], w+dw[di]
        while 0<=nh<n and 0<=nw<n:
            if g[nh][nw] == 0:break
            if g[nh][nw] != bw:
                li.append((nh, nw))
            if g[nh][nw] == bw:
                fla = True
                break
            nh, nw = nh+dh[di], nw+dw[di]
        if fla:
            while li:
                h, w = li.pop()
                g[h][w] = bw
    g[h][w] = bw
    for i in range(8):
        nh, nw = h+dh[i], w+dw[i]
        if 0<=nh<n and 0<=nw<n and g[nh][nw] != bw and g[nh][nw] != 0:
            way(nh, nw, i, bw)

for testcase in range(1, int(input())+1):
    n, m = map(int, input().rstrip().split())
    g = [[0]*n for _ in range(n)]
    for i in (n//2, n//2-1):
        for j in (n//2, n//2-1):
            if i-j:g[i][j] = 1
            else:g[i][j] = 2
    for _ in range(m):
        a, b, bw = map(int, input().rstrip().split())
        bfs(a-1, b-1, bw)
    cnt = [0, 0, 0]
    for i in range(n):
        for j in range(n):
            if g[i][j] == 0:continue
            cnt[g[i][j]] += 1
    print(f"#{testcase} {cnt[1]} {cnt[2]}")
'''








