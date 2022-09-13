'''
백조의 호수

백조 두마리.
호수를 덮고 있는 빙판때매 만나지 못한다.
호수는 차례대로 녹는데, 매일 물과 접촉한 모든 빙판 공간은 녹는다.
두개의 공간이 접촉하려면 가로나 세로로 닿아있어야 한다.

며칠 뒤에 백조들이 만날 수 있는지?

입력
R, C 제시. 1이상 1500이하
R개 줄에 C의 문자열 제시. .은 물, X는 빙판, L은 백조.

출력
백조들이 만나는데 걸리는 최소 시간.
'''
'''
백조 bfs 할 것 / 얼음 bfs 할 것 나눠서 한 줄씩 실행.
'''
from collections import deque
import sys
input=sys.stdin.readline

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

r, c = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(r)]
bj = []

for i in range(r):
    for j in range(c):
        if g[i][j] == 'L':
            bj.append((i, j))
            g[i][j] = '.'
        if len(bj) == 2:
            break
    if len(bj) == 2:
        break


ans = -1
bv = [[0]*c for _ in range(r)] # 백조 방문 처리
bq = deque([bj[0]])
nbq = deque()
while bq:
    h, w = bq.popleft()
    for k in range(4):
        nh, nw = h + dh[k], w + dw[k]
        if 0<=nh<r and 0<=nw<c and bv[nh][nw] == 0 and g[nh][nw] == '.':
            bv[nh][nw] = 1
            bq.append((nh, nw))
        elif 0<=nh<r and 0<=nw<c and nh==bj[1][0] and nw==bj[1][1]:
            ans = 0
            break
        elif 0<=nh<r and 0<=nw<c and bv[nh][nw] == 0 and g[nh][nw] == 'X':
            bv[nh][nw] = 1
            nbq.append((nh, nw))
bq = nbq
v = [[0]*c for _ in range(r)] # 얼음들 방문처리용 
ice = deque()
# ice 만들기.
for i in range(r):
    for j in range(c):
        if v[i][j] == 0 and (g[i][j] == '.' or g[i][j] == 'L'):
            q = deque()
            q.append((i, j))
            v[i][j] = 1
            while q:
                h, w = q.popleft()
                for k in range(4):
                    nh, nw = h + dh[k], w + dw[k]
                    if 0<=nh<r and 0<=nw<c and v[nh][nw] == 0 and g[nh][nw] == '.':
                        v[nh][nw] = 1
                        q.append((nh, nw))
                    elif 0<=nh<r and 0<=nw<c and v[nh][nw] == 0 and g[nh][nw] == 'X':
                        g[nh][nw] = '.'
                        v[nh][nw] = 1
                        ice.append((nh, nw))

def bjbfs(idx):
    global bq, ans
    nbq = deque()
    while bq:
        h, w = bq.popleft()
        for k in range(4):
            nh, nw = h + dh[k], w + dw[k]
            if 0<=nh<r and 0<=nw<c and bv[nh][nw] == 0 and g[nh][nw] == '.':
                bv[nh][nw] = 1
                bq.append((nh, nw))
            elif 0<=nh<r and 0<=nw<c and nh==bj[1][0] and nw==bj[1][1]:
                ans = idx+1
                return
            elif 0<=nh<r and 0<=nw<c and bv[nh][nw] == 0 and g[nh][nw] == 'X':
                bv[nh][nw] = 1
                nbq.append((nh, nw))
    bq = nbq

def icebfs():
    global ice, ans
    nice =deque()
    while ice:
        h, w = ice.popleft()
        for k in range(4):
            nh, nw = h + dh[k], w + dw[k]
            if 0<=nh<r and 0<=nw<c and v[nh][nw] == 0 and g[nh][nw] == 'X':
                v[nh][nw] = 1
                g[nh][nw] = '.'
                nice.append((nh, nw))
    ice = nice

if ans >= 0:
    pass
else:
    i = 0
    while ans == -1:
        i += 1
        icebfs()
        bjbfs(i)

print(ans)


'''
# 굉장히 빠른 코드!
import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
Map = [[] for _ in range(R)]
swans = []
q = deque()                               #백조1 -> 백조2를 bfs탐색
melt = []                                 #다음 날 얼음을 녹이기 위한 물의 가장자리
for r in range(R):
    data = input().rstrip()
    for c in range(C):
        x = data[c]
        if x == 'X':
            Map[r].append(1)                #얼음은 1, 물(, 백조)은0
        else:
            Map[r].append(0)
            melt.append((r, c))
            if x == "L":
                swans.append((r, c))

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
start, target = swans

q.append(start)
Map[start[0]][start[1]] = 2

day = 0
while True:

    ######탐색
    n_q = deque()                   #얼음에 막혀서, 다음 날에 bfs를 시작할 위치 저장
    while q:
        cx, cy = q.popleft()
        if target == (cx, cy):
            break

        flag = False                #n_q에 중복해서 넣지 않기 위한 flag
        for dx, dy in moves:
            nx = cx + dx
            ny = cy + dy
            if not (0 <= nx < R and 0 <= ny < C):
                continue

            tile = Map[nx][ny]

            if tile == 0:
                Map[nx][ny] = 2             #백조가 갈수 있는 것으로 확인 된 곳 -> 2 (방문 처리)
                q.append((nx, ny))
            if tile == 1 and not flag:
                n_q.append((cx, cy))        #다음 날 여기서부터 다시 탐색
                flag = True
    q = n_q
    if Map[target[0]][target[1]] == 2:
        break


    ######얼음 녹이기
    n_melt = []
    while melt:
        cx, cy = melt.pop()
        for dx, dy in moves:
            nx = cx + dx
            ny = cy + dy
            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if Map[nx][ny] == 1:
                Map[nx][ny] = 0
                n_melt.append((nx, ny))
    melt = n_melt

    day += 1

print(day)
'''



'''
# 시간초과
from collections import deque
import sys
input=sys.stdin.readline

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

r, c = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(r)]
v = [[0]*c for _ in range(r)]
# bj = []
bjsp = []

# for i in range(r):
#     for j in range(c):
#         if g[i][j] == 'L':
#             bj.append((i, j))
#         if len(bj) == 2:
#             break
#     if len(bj) == 2:
#         break

ice = deque()
grp = []
a = 0
ans = -1
for i in range(r):
    for j in range(c):
        if v[i][j] == 0 and (g[i][j] == '.' or g[i][j] == 'L'):
            a += 1
            q = deque()
            q.append((i, j))
            grp.append(set([a]))
            v[i][j] = a
            if g[i][j] == 'L':
                bjsp.append(a)
            while q:
                h, w = q.popleft()
                for k in range(4):
                    nh, nw = h + dh[k], w + dw[k]
                    if 0<=nh<r and 0<=nw<c and v[nh][nw] == 0 and g[nh][nw] == '.':
                        v[nh][nw] = a
                        q.append((nh, nw))
                    elif 0<=nh<r and 0<=nw<c and v[nh][nw] == 0 and g[nh][nw] == 'L':
                        v[nh][nw] = a
                        q.append((nh, nw))
                        bjsp.append(a)
                    elif 0<=nh<r and 0<=nw<c and v[nh][nw] == 0 and g[nh][nw] == 'X':
                        v[nh][nw] = a
                        ice.append((nh, nw))
                    elif 0<=nh<r and 0<=nw<c and v[nh][nw] != 0:
                        for gi in range(len(grp)):
                            if v[nh][nw] in grp[gi]:
                                grp[gi].add(a)

for i in grp:
    if bjsp[0] in i and bjsp[1] in i:
        ans = 1
        break

if bjsp[0] == bjsp[1]:
    ans = 0

def melt(idx):
    global ice, ans
    nice = deque()
    ret = set()
    while ice:
        h, w = ice.popleft()
        a = v[h][w]
        g[h][w] = '.'
        for k in range(4):
            nh, nw = h + dh[k], w + dw[k]
            if 0<=nh<r and 0<=nw<c and v[nh][nw] == 0 and g[nh][nw] == 'X':
                v[nh][nw] = a
                nice.append((nh, nw))
            elif 0<=nh<r and 0<=nw<c and v[nh][nw] != 0 and g[nh][nw] == 'X':
                grp[a-1].add(v[nh][nw])
                # for gi in range(len(grp)):
                #     if a in grp[gi]:
                #         grp[gi].add(v[nh][nw])
                #         break
    for i in grp:
        if bjsp[0] in i and bjsp[1] in i:
            ans = idx
            if not nice:
                ans-=1
            return
    ice = nice
    return
i = 1
while ans == -1:
    i+=1
    melt(i)
    # print(grp)
    # print(bjsp)

print(ans)
'''














