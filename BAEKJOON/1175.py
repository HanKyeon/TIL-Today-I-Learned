'''
배달

선물 배달 할 것이다.
n*m 배열
이동에 1분 사방이동.
S : 민식이
C 배달 할 곳. 2개
# 벽
. 공간
매 시간마다 방향을 바꿔야 한다. 같은 방향으로 연속 이동 할 수 없다. 선물을 모두 배달하는데 걸리는 시간의 최솟값을 구해라.

입력
n, m 제시.
n개줄 그래프 제시.

출력
선물 배달하는데 걸리는 시간의 최솟값 출력. 불가능 하다면 -1 출력.
'''
from collections import deque
import sys
input = sys.stdin.readline

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

def inputdata():
    global n, m, sh, sw
    cnt = 0
    for i in range(n):
        s = list(input().rstrip())
        for j in range(m):
            if s[j] == 'S':
                sh, sw = i, j
                s[j] = 0
            elif s[j] == 'C':
                cnt+=1
                s[j] = cnt
            elif s[j] == '#':
                s[j] = -1
            else:
                s[j] = 0
        g.append(s)

def bfs(h, w):
    global n, m
    v = [[[[0,0,0,0] for _ in range(m)] for _ in range(n)] for _ in range(3)]
    v[0][h][w] = [1,1,1,1] # 열쇠, 세로, 가로, 방향
    q = deque()
    q.append((0, h, w, -1, 0)) # 열쇠 보유 여부. 세로 가로 방향, 시간
    while q:
        kyz, h, w, di, dep = q.popleft()
        for i in range(4):
            if i == di:
                continue
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<m and g[nh][nw] == -1:
                continue
            elif 0<=nh<n and 0<=nw<m and g[nh][nw] == 0 and not v[kyz][nh][nw][i]:
                v[kyz][nh][nw][i] = 1
                q.append((kyz, nh, nw, i, dep+1))
            elif 0<=nh<n and 0<=nw<m and g[nh][nw] == 1:
                if kyz == 1:
                    v[kyz][nh][nw][i] = 1
                    q.append((kyz, nh, nw, i, dep+1))
                    continue
                if kyz+1 == 3:
                    return dep+1
                v[kyz+1][nh][nw][i]=1
                q.append((kyz+1, nh, nw, i, dep+1))
            elif 0<=nh<n and 0<=nw<m and g[nh][nw] == 2:
                if kyz == 2: # 해당 방향으로 다시 갈 때 방문처리가 되어야 함
                    v[kyz][nh][nw][i] = 1
                    q.append((kyz, nh, nw, i, dep+1))
                    continue
                if kyz+2 == 3:
                    return dep+1
                v[kyz+2][nh][nw][i]=1
                q.append((kyz+2, nh, nw, i, dep+1))
    return -1


n, m = map(int, input().rstrip().split())
g = []
parsing = {}
sh, sw = 0, 0
inputdata()
print(bfs(sh, sw))


'''
폐기
def bfs(h, w):
    global n, m
    v = [[[[0,0,0,0] for _ in range(m)] for _ in range(n)] for _ in range(n)]
    v[0][h][w] = [1,1,1,1]
    q = deque()
    q.append((h, w, -1, 1, 0)) # h, w, di, cnt, dep(v 배열에 남길 것. cnt가 v보다 더 크다면 방문 시작한다.)
    while q:
        h, w, di, cnt, dep = q.popleft()
        if cnt < gcnt:
            continue
        for i in range(4):
            if i == di:
                continue
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<m and g[nh][nw] != '#' and v[nh][nw][i] < cnt:
                if g[nh][nw] == 'C':
                    if gcnt == 2:
                        return dep+1
                    g[nh][nw] = '.'
                    gcnt+=1
                    gli = set()
                    for j in range(4):
                        nnh, nnw = nh+dh[j], nw+dw[j]
                        if 0<=nnh<n and 0<=nnw<m:
                            for k in range(4):
                                if k == i:
                                    continue
                                if v[nnh][nnw][k] == 1:
                                    gli.add(k)
                    print(gli)
                    if len(gli) >= 2:
                        v[nh][nw] = [2,2,2,2]
                        q.append((nh, nw, -1, 2, dep+1))
                    else:
                        imsi = [2,2,2,2]
                        imsi[i] = 1
                        v[nh][nw] = imsi
                        q.append((nh, nw, i, 2, dep+1))
                else:
                    v[nh][nw][i] = cnt
                    q.append((nh, nw, i, cnt, dep+1))
'''

'''
# 잘 하면 짤 수 있을거 같은데 시간낭비라 패스
from collections import deque
import sys
input = sys.stdin.readline

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

def bfs(oh, ow):
    global n, m
    # ret = [set(), set(), set()]
    # dst = [0, 0, 0]
    v = [[[0]*4 for _ in range(m)] for _ in range(n)]
    q = deque()
    v[oh][ow] = [1,1,1,1]
    for i in range(4):
        nh, nw = oh+dh[i], ow+dw[i]
        if 0<=nh<n and 0<=nw<m and g[nh][nw] == '#':
            continue
        elif 0<=nh<n and 0<=nw<m and g[nh][nw] == '.':
            v[nh][nw][i] = 1
            q.append((nh, nw, i))
        elif 0<=nh<n and 0<=nw<m and (g[nh][nw] == 'S' or g[nh][nw] == 'C'):
            v[nh][nw][i] = 1
            q.append((nh, nw, i))
            # dst[parsing[(nh, nw)]] = 1
            # ret[parsing[(nh, nw)]].add(i)
    while q:
        h, w, di = q.popleft()
        for i in range(4):
            if i == di:
                continue
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<m and g[nh][nw] == '#':
                continue
            elif 0<=nh<n and 0<=nw<m and g[nh][nw] == '.' and not v[nh][nw][i]:
                v[nh][nw][i] = v[h][w][di]+1
                q.append((nh, nw, i))
            elif 0<=nh<n and 0<=nw<m and (g[nh][nw] == 'S' or g[nh][nw] == 'C') and not v[nh][nw][i]:
                v[nh][nw][i] = v[h][w][di]+1
                q.append((nh, nw, i))
                # dst[parsing[(nh, nw)]] = 1
                # ret[parsing[(nh, nw)]].add(i)
    ret = [[], [], []]
    for h, w in parsing:
        a = parsing[(h, w)]
        if h == oh and w == ow:
            ret[a] = [0, 0, 0, 0]
            continue
        ap = v[h][w]
        for i in range(4):
            if not ap[i]:
                ap[i] = int(10e9)
        ret[a] = ap
    return ret

n, m = map(int, input().rstrip().split())
g = []
nodz = []
parsing = {}
cnt = 0
for i in range(n):
    s = list(input().rstrip())
    g.append(s)
    for j in range(m):
        if s[j] == 'S':
            nodz = [(i, j)] + nodz
            sh, sw = i, j
            parsing[(i, j)] = 0
        elif s[j] == 'C':
            nodz.append((i, j))
            cnt += 1
            parsing[(i, j)] = cnt

edgz = []
for h, w in nodz:
    a = bfs(h, w)
    if a:
        edgz.append(a)
v = [0, 0, 0]
v[parsing[(sh, sw)]] = 1
elz = []
for h, w in parsing:
    a = parsing[(h, w)]
    if v[a]:
        continue
    elz.append(a)

'''
