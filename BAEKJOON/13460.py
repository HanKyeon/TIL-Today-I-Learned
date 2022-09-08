'''
구슬 탈출 2


보드에 빨강 파랑 넣고 빨강을 구멍을 통해 빼내는 게임. 파랑 드가믄 안됨!
세로n 가로m 가장 바깥은 항상 막혀있다.
보드에는 구멍이 하나. 중력으로 이리저리 굴려야 한다. 상하좌우 기울이기 가능.
공은 즉시 이동. 빨강이 구멍이라면 성공, 파랑이 구멍에 빠지면 실패. 빨강과 파랑이 동시에 빠져도 실패.
빨 파는 같은 위치에 존재x 빨강 파랑은 한 칸 모두 차지. 기울이는 동작을 멈추는 것은 더 이상 구슬이 움직이지 않을 때까지.

보드 상태가 제시되었을 때, 최소 몇번만에 빨강을 빼낼 수 있는가?

입력
세로 가로 n, m 3이상 10이하
보드 제시
.은 빈 칸 #은 장애물 o는 구멍 R은 빨 B는 파랑. 가장자리는 모두 # 구슬은 각 1개

출력
최소 몇 번 만에 빨강을 구멍에 빼낼 수 있는가? 10번 이하로 움직여서 빨강을 뺄 수 없다면 -1 출력.

'''
from collections import deque
import sys
input = sys.stdin.readline # 빠른 입출력 위한 코드

n, m = map(int, input().split())
g = []
for i in  range(n):
    g.append(list(input()))
    for j in range(m):
        if g[i][j] == 'R': # 빨간구슬 위치
            g[i][j] = '.'
            rx, ry = i, j
        elif g[i][j] == 'B': # 파란구슬 위치
            g[i][j] = '.'
            bx, by = i, j

# 상 하 좌 우로 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visited = [] # 방문여부를 판단하기 위한 리스트
    visited.append((rx, ry, bx, by))
    count = 0
    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if count > 10: # 움직인 횟수가 10회 초과면 -1 출력
                print(-1)
                return
            if g[rx][ry] == 'O': # 현재 빨간 구슬의 위치가 구멍이라면 count출력
                print(count)
                return 
            for i in range(4): # 4방향 탐색
                nrx, nry = rx, ry
                while True: # #일 때까지 혹은 구멍일 때까지 움직임
                    nrx += dx[i]
                    nry += dy[i]
                    if g[nrx][nry] == '#': # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if g[nrx][nry] == 'O':
                        break
                nbx, nby = bx, by
                while True: # #일 때까지 혹은 구멍일 때까지 움직임
                    nbx += dx[i]
                    nby += dy[i]
                    if g[nbx][nby] == '#': # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if g[nbx][nby] == 'O':
                        break
                if g[nbx][nby] == 'O': # 파란구슬이 먼저 구멍에 들어가거나 동시에 들어가면 안됨 따라서 이 경우 무시
                    continue
                if nrx == nbx and nry == nby: # 두 구슬의 위치가 같다면
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by): # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited: # 방문해본적이 없는 위치라면 새로 큐에 추가 후 방문 처리
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count += 1
    print(-1) # 10회가 초과하지 않았지만 10회 내에도 구멍에 들어가지 못하는 경우
bfs(rx, ry, bx, by)








'''
from collections import deque
import sys
input = sys.stdin.readline
# 상 하 좌 우
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

def di4(h, w, di):
    global blue, red
    ph, pw = dh[di], dw[di]
    nh, nw = h+ph, w+pw # h + dh[di], w + dw[di]
    if g[nh][nw] == 'O':
        # print('O를 만나다')
        g[h][w] = '.'
        return (False, (h, w)) # O를 만나면
    elif g[nh][nw] == '#':
        # print('#를 만나다')
        return (True, (h, w))
    elif g[nh][nw] == 'B' or g[nh][nw] == 'R': # B or R 바로 옆이면
        return (True, (h, w))
    else:
        # print('.를 만나다')
        pass
    while g[nh][nw] == '.':
        nh, nw = nh + ph, nw + pw
        if g[nh][nw] == 'O':
            g[h][w] = '.'
            return (False, (h, w))
        # if rb == 0 and g[nh][nw] == 'O':
        #     return 1
        # if rb == 1 and g[nh][nw] == 'O':
        #     return 0
    nh, nw = nh - ph, nw - pw
    g[h][w], g[nh][nw] = g[nh][nw], g[h][w]
    return (True, (nh, nw))
    # 이따 안되면 써보자
    if rb == 1:
        blue = [nh, nw]
    else:
        red = [nh, nw]
    return -1

def dfs(rh, rw, bh, bw, di, c):
    global ans
    if c > 10:
        return
    if c >= ans:
        return
    print(rh, rw, bh, bw, di, c)
    for i in range(4):
        if i == di: # 같은 방향이면 안할거다.
            continue
        if i == 0: # 위로 이동이면 더 위에 잇는거 먼저
            if rh > bh:
                re = di4(rh, rw, i)
                bl = di4(bh, bw, i)
                if re[0] == False and bl[0]:
                    ans = c+1
                    g[re[1][0]][re[1][1]] = 'R'
                    return
                elif bl[0] == False and re[0]:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    continue
                elif bl[0] == False and re[0] == False:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    g[re[1][0]][re[1][1]] = 'R'
                    continue
                else:
                    nrh, nrw = re[1]
                    nbh, nbw = bl[1]
                    dfs(nrh, nrw, nbh, nbw, i, c+1)
        elif i == 1: # 아래로 이동이면 더 아래 있는거 먼저
            if rh < bh:
                re = di4(rh, rw, i)
                bl = di4(bh, bw, i)
                if re[0] == False and bl[0]:
                    ans = c+1
                    g[re[1][0]][re[1][1]] = 'R'
                    break
                elif bl[0] == False and re[0]:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    continue
                elif bl[0] == False and re[0] == False:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    g[re[1][0]][re[1][1]] = 'R'
                    continue
                else:
                    nrh, nrw = re[1]
                    nbh, nbw = bl[1]
                    dfs(nrh, nrw, nbh, nbw, i, c+1)
            else:
                bl = di4(bh, bw, i)
                re = di4(rh, rw, i)
                if re[0] == False and bl[0]:
                    ans = c+1
                    g[re[1][0]][re[1][1]] = 'R'
                    return
                elif bl[0] == False and re[0]:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    continue
                elif bl[0] == False and re[0] == False:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    g[re[1][0]][re[1][1]] = 'R'
                    continue
                else:
                    nbh, nbw = bl[1]
                    nrh, nrw = re[1]
                    dfs(nrh, nrw, nbh, nbw, i, c+1)
        elif i == 2: # 왼쪽 이동이면 w가 작은 쪽 먼저
            if rw < bw:
                re = di4(rh, rw, i)
                bl = di4(bh, bw, i)
                if re[0] == False and bl[0]:
                    ans = c+1
                    g[re[1][0]][re[1][1]] = 'R'
                    return
                elif bl[0] == False and re[0]:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    continue
                elif bl[0] == False and re[0] == False:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    g[re[1][0]][re[1][1]] = 'R'
                    continue
                else:
                    nrh, nrw = re[1]
                    nbh, nbw = bl[1]
                    dfs(nrh, nrw, nbh, nbw, i, c+1)
            else:
                bl = di4(bh, bw, i)
                re = di4(rh, rw, i)
                if re[0] == False and bl[0]:
                    ans = c+1
                    g[re[1][0]][re[1][1]] = 'R'
                    return
                elif bl[0] == False and re[0]:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    continue
                elif bl[0] == False and re[0] == False:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    g[re[1][0]][re[1][1]] = 'R'
                    continue
                else:
                    nbh, nbw = bl[1]
                    nrh, nrw = re[1]
                    dfs(nrh, nrw, nbh, nbw, i, c+1)
        elif i == 3:
            if rw > bw:
                re = di4(rh, rw, i)
                bl = di4(bh, bw, i)
                if re[0] == False and bl[0]:
                    ans = c+1
                    g[re[1][0]][re[1][1]] = 'R'
                    return
                elif bl[0] == False and re[0]:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    continue
                elif bl[0] == False and re[0] == False:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    g[re[1][0]][re[1][1]] = 'R'
                    continue
                else:
                    nrh, nrw = re[1]
                    nbh, nbw = bl[1]
                    dfs(nrh, nrw, nbh, nbw, i, c+1)
            else:
                bl = di4(bh, bw, i)
                re = di4(rh, rw, i)
                if re[0] == False and bl[0]:
                    ans = c+1
                    g[re[1][0]][re[1][1]] = 'R'
                    return
                elif bl[0] == False and re[0]:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    continue
                elif bl[0] == False and re[0] == False:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    g[re[1][0]][re[1][1]] = 'R'
                    continue
                else:
                    nbh, nbw = bl[1]
                    nrh, nrw = re[1]
                    dfs(nrh, nrw, nbh, nbw, i, c+1)
        print(i)
        for j in g:
            print(*j)

n, m =  map(int, input().split())
g = [list(input().rstrip()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if g[i][j] == 'R':
            red = [i, j]
        if g[i][j] == 'B':
            blue = [i, j]
        if g[i][j] == 'O':
            hall = [i, j]

ans = int(10e9)
sets = set()
dfs(red[0], red[1], blue[0], blue[1], -1, 0) # rh, rw, bh, bw, di, c


    # for i in g:
    #     print(*i)
if ans != int(10e9):
    print(ans)
else:
    print(-1)


# if di < 2  상하이동
# if di >= 2 좌우이동 
'''







'''


while q:
    if ans:
        break
    rh, rw, bh, bw, di, c = q.popleft()
    if c > 10:
        break
    sets.add((rh, rw, bh, bw))
    for i in range(4):
        if i == di:
            continue
        if i == 0: # 위로 이동이면 더 위에 잇는거 먼저
            if rh > bh:
                re = di4(rh, rw, i)
                bl = di4(bh, bw, i)
                print(re, bl)
                if re[0] == False and bl[0]:
                    ans = c+1
                    break
                elif bl[0] == False and re[0]:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    continue
                elif bl[0] == False and re[0] == False:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    g[re[1][0]][re[1][1]] = 'R'
                    continue
                else:
                    nrh, nrw = re
                    nbh, nbw = bl
                    q.append((nrh, nrw, nbh, nbw, i, c+1))
            else:
                bl = di4(bh, bw, i)
                re = di4(rh, rw, i)
                print(re, bl)
                if re[0] == False and bl[0]:
                    ans = c+1
                    break
                elif bl[0] == False and re[0]:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    continue
                elif bl[0] == False and re[0] == False:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    g[re[1][0]][re[1][1]] = 'R'
                    continue
                else:
                    nbh, nbw = bl
                    nrh, nrw = re
                    q.append((nrh, nrw, nbh, nbw, i, c+1))
        elif i == 1: # 아래로 이동이면 더 아래 있는거 먼저
            if rh < bh:
                re = di4(rh, rw, i)
                bl = di4(bh, bw, i)
                print(re, bl)
                if re[0] == False and bl[0]:
                    ans = c+1
                    break
                elif bl[0] == False and re[0]:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    continue
                elif bl[0] == False and re[0] == False:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    g[re[1][0]][re[1][1]] = 'R'
                    continue
                else:
                    nrh, nrw = re
                    nbh, nbw = bl
                    q.append((nrh, nrw, nbh, nbw, i, c+1))
            else:
                bl = di4(bh, bw, i)
                re = di4(rh, rw, i)
                print(re, bl)
                if re[0] == False and bl[0]:
                    ans = c+1
                    break
                elif bl[0] == False and re[0]:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    continue
                elif bl[0] == False and re[0] == False:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    g[re[1][0]][re[1][1]] = 'R'
                    continue
                else:
                    nbh, nbw = bl
                    nrh, nrw = re
                    q.append((nrh, nrw, nbh, nbw, i, c+1))
        elif i == 2: # 왼쪽 이동이면 w가 작은 쪽 먼저
            if rw < bw:
                re = di4(rh, rw, i)
                bl = di4(bh, bw, i)
                print(re, bl)
                if re[0] == False and bl[0]:
                    ans = c+1
                    break
                elif bl[0] == False and re[0]:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    continue
                elif bl[0] == False and re[0] == False:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    g[re[1][0]][re[1][1]] = 'R'
                    continue
                else:
                    nrh, nrw = re
                    nbh, nbw = bl
                    q.append((nrh, nrw, nbh, nbw, i, c+1))
            else:
                bl = di4(bh, bw, i)
                re = di4(rh, rw, i)
                print(re, bl)
                if re[0] == False and bl[0]:
                    ans = c+1
                    break
                elif bl[0] == False and re[0]:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    continue
                elif bl[0] == False and re[0] == False:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    g[re[1][0]][re[1][1]] = 'R'
                    continue
                else:
                    nbh, nbw = bl
                    nrh, nrw = re
                    q.append((nrh, nrw, nbh, nbw, i, c+1))
        elif i == 3:
            if rw > bw:
                re = di4(rh, rw, i)
                bl = di4(bh, bw, i)
                print(re, bl)
                if re[0] == False and bl[0]:
                    ans = c+1
                    break
                elif bl[0] == False and re[0]:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    continue
                elif bl[0] == False and re[0] == False:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    g[re[1][0]][re[1][1]] = 'R'
                    continue
                else:
                    nrh, nrw = re
                    nbh, nbw = bl
                    q.append((nrh, nrw, nbh, nbw, i, c+1))
            else:
                bl = di4(bh, bw, i)
                re = di4(rh, rw, i)
                print(re, bl)
                if re[0] == False and bl[0]:
                    ans = c+1
                    break
                elif bl[0] == False and re[0]:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    continue
                elif bl[0] == False and re[0] == False:
                    g[bl[1][0]][bl[1][1]] = 'B'
                    g[re[1][0]][re[1][1]] = 'R'
                    continue
                else:
                    nbh, nbw = bl
                    nrh, nrw = re
                    q.append((nrh, nrw, nbh, nbw, i, c+1))
'''









