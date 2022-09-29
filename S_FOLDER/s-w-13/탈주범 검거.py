'''
탈주범 검거

흉악범 탈출. 수색
지하 터널 은신중.
탈주범이 있을 수 있는 위치의 갯수 계산.
탈주범은 시간당 1 이동.
터널 종류는 7종류
1. 사방이동 가능
2. 상하이동 가능
3. 좌우이동 가능.
4. 상단 <-> 우측 이동 가능
5. 아래 - 우측 이동
6. 좌측 아래 이동
7. 좌측 위 이동
'''
# 0상 1하 2좌 3우
# 4우상단 5우하단 6좌하단 7좌상단
from collections import deque

# 상하좌우
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

'''
1 -> 0 1 2 3
2 -> 0 1
3 -> 2 3
4 -> 0 3
5 -> 1 3
6 -> 1 2
7 -> 0 2
'''


def hsg():
    global n, m, g, sh, sw, tm
    if tm == 1:
        return 1
    for i in range(n):
        for j in range(m):
            if not g[i][j]:
                continue
            # 1: 1234 -> 1234
            if g[i][j] == 1:
                continue
            # 2 : 0->1 1->0
            elif g[i][j] == 2:
                g[i][j] = {0:0, 1:1}
            # 3: 2->3 3->2
            elif g[i][j] == 3:
                g[i][j] = {2:2, 3:3}
            # 4: 하단1 -> 우측3 / 좌2 -> 상0
            elif g[i][j] == 4: # +2 %2
                g[i][j] = {1:3, 2:0}
            # 5: 상단0 -> 우측3 / 좌2 -> 하1
            elif g[i][j] == 5: # -1 %2
                g[i][j] = {0:3, 2:1}
            # 6: 우3->하1 / 상0->좌2
            elif g[i][j] == 6: # -2 %2
                g[i][j] = {3:1, 0:2}
            # 7: 우3->상0 / 하1->좌2 -> +1%2
            elif g[i][j] == 7: #
                g[i][j] = {3:0, 1:2}
    v = [[0 for _ in range(m)] for _ in range(n)]
    v[sh][sw] = 1
    q = deque()
    if g[sh][sw] == 1:
        for i in range(4):
            nh, nw = sh+dh[i], sw+dw[i]
            if 0<=nh<n and 0<=nw<m and g[nh][nw] and (g[nh][nw] == 1 or i in g[nh][nw]) and v[nh][nw] == 0:
                v[nh][nw] = 1
                q.append((nh, nw, i, 3))
    else:
        for i in g[sh][sw]:
            di = g[sh][sw][i]
            nh, nw = sh+dh[di], sw+dw[di]
            if 0<=nh<n and 0<=nw<m and g[nh][nw] and (g[nh][nw] == 1 or di in g[nh][nw]) and v[nh][nw] == 0:
                v[nh][nw] = 1
                q.append((nh, nw, di, 3))
    while q:
        h, w, di, dep = q.popleft()
        if dep > tm:
            break
        if g[h][w] == 1:
            for i in range(4):
                nh, nw = h+dh[i], w+dw[i]
                if 0<=nh<n and 0<=nw<m and g[nh][nw] and (g[nh][nw] == 1 or i in g[nh][nw]) and v[nh][nw] == 0:
                    v[nh][nw] = 1
                    q.append((nh, nw, i, dep+1))
        else:
            ndi = g[h][w][di]
            nh, nw = h+dh[ndi], w+dw[ndi]
            if 0<=nh<n and 0<=nw<m and g[nh][nw] and (g[nh][nw] == 1 or ndi in g[nh][nw]) and v[nh][nw] == 0:
                v[nh][nw] = 1
                q.append((nh, nw, ndi, dep+1))
    ret = sum(map(sum, v))
    # for i in v:
    #     print(i)
    # for i in g:
    #     print(i)
    return ret


for tc in range(1, int(input())+1):
    n, m, sh, sw, tm = map(int, input().rstrip().split())
    g = [list(map(int, input().rstrip().split())) for _ in range(n)]
    print(f"#{tc} {hsg()}")









'''
dh = [-1, 1, 0, 0, -1, 1, 1, -1]
dw = [0, 0, -1, 1, 1, 1, -1, -1]
    for i in range(n):
        for j in range(m):
            if not g[i][j]:
                continue
            if g[i][j] == 1:
                g[i][j] = [0,1,2,3]
            elif g[i][j] == 2:
                g[i][j] = [0,1]
            elif g[i][j] == 3:
                g[i][j] = [2,3]
            # 이전 방향이 하단1이라면 우하단이동, 좌2라면 좌상단 이동
            elif g[i][j] == 4:
                g[i][j] = [7, 5]
            # 이전 방향이 상단0이라면 우상단이동, 좌2라면 우하단 이동
            elif g[i][j] == 5:
                g[i][j] = [4, 6]
            # 이전 방향이 상단0이라면 좌상단 이동, 우3이라면 우하단 이동
            elif g[i][j] == 6: #
                g[i][j] = [7, 5]
            # 이전 방향이 하단1이면 좌하단 이동, 우3이라면 우상단 이동
            elif g[i][j] == 7: #
                g[i][j] = [4, 6]
    v = [[0 for _ in range(m)] for _ in range(n)]
    v[sh][sw] = 1
    for i in g[sh][sw]:
        nh, nw = 
    q = deque((sh, sw, 1, -1)) # h, w, dep, 이전 di
    while q:
        h, w, dep, bdi = q.popleft()
        for i in g[h][w]:
            if bdi
'''
