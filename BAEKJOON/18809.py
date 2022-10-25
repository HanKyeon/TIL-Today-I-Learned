'''
Gaaaaaaaaaaaaaaaaaaaaarden

초록 배양액, 빨강 배양액을 땅에 적절하게 뿌려 꽃을 피울 것.
배양액을 뿌릴 수 있는 땅은 정해져 있다.
배양액은 매 초 이전 배양액이 도달 한 적 없는 인접한 땅으로 퍼져간다.
동일한 시간에 도달한 땅에서는 두 배양액이 합쳐지며 꽃이 핀다.
꽃이 핀 땅에는 배양액이 사라지며, 더이상 퍼트리지 않는다.

배양액은 봄이 지나면 사용 할 수 없게 되므로 주어진 모든 배양액을 사용해야 한다.
초2빨2가 주어졌는데 초1빨2만 사용하는 것은 불가.
배양액은 서로 다른 곳에 뿌려야 한다.
정원가 두 배양액의 갯수가 주어져 있을 때, 피울 수 있는 꽃의 최대 갯수 구하기.

입력
n, m, g, r 제시. 세로 가로 초록수 빨강수
n개 줄에 정원의 각 행을 나타내는 M개의 정수가 한 개의 빈 칸을 사이에 두고 제시.
각 칸에 들어가는 값은 0, 1, 2이다. 0은 호수, 1은 배양액x 땅, 2는 배양액 o 땅.
배양액 뿌릴 수 있는 땅의 갯수는 r+g개 이상이고 10개 이하이다.

출력
최대 피울 수 있는 꽃의 갯수
'''
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]

def bfs():
    global n, m
    v = [[0]*m for _ in range(n)]
    c = [[0]*m for _ in range(n)]
    q = deque()
    ret = 0
    for h, w in redz:
        q.append((h, w, 1, 1)) # h, w, dep, color
        v[h][w] = 1
        c[h][w] = 1
    for h, w in grnz:
        q.append((h, w, 1, 2)) # h, w, dep, color
        v[h][w] = 1
        c[h][w] = 2
    while q:
        h, w, dep, color = q.popleft()
        if v[h][w] < 0:
            continue
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and g[nh][nw] and not v[nh][nw]:
                v[nh][nw] = dep+1
                c[nh][nw] = color
                q.append((nh, nw, dep+1, color))
            elif 0<=nh<n and 0<=nw<m and g[nh][nw] and v[nh][nw]:
                if v[nh][nw] == dep+1 and c[nh][nw] != color:
                    v[nh][nw] = -1
                    ret += 1
    return ret

n, m, grn, red = map(int, input().rstrip().split())
g = []
avIsl, avIslCnt = [], 0
for i in range(n):
    s = list(map(int, input().rstrip().split()))
    for j in range(m):
        if s[j] == 2:
            avIsl.append((i, j))
            avIslCnt += 1
    g.append(s)
ans = 0

for combi in combinations(avIsl, red+grn):
    for rez in combinations(combi, red):
        redz = rez
        grnz = []
        for i in combi:
            if i in rez:
                continue
            grnz.append(i)
        a = bfs()
        if a > ans:
            ans = a

print(ans)








'''
2의 갯수만큼 v 높이를 만들어서 bfs를 시킨다.
꽃이 피면은 도달점이 막히는걸 해결하지 못할듯.
'''
'''
DFS처럼 점을 5개 선택해서 가는것도 가능할듯 -> 대칭점 문제 해결해야 함. -> 시작점을 반만 돌면 안되는감? -> 레드 그린 값을 받아서 빼가면서 red 부분은 반만 순회하면 될듯?
'''



'''
mov = [(-1,0), (0,1), (1,0), (0,-1)]

def dfs(r, g, cnt):
    global grn, red, ans, avIslCnt
    if cnt == grn+red:
        # print(redz, grnz)
        ret = bfs()
        if ret > ans:
            ans = ret
        return
    if r:
        # if red % 2:
        for i in range(avIslCnt):
            if vstp[i]:
                continue
            vstp[i] = 1
            redz.append(avIsl[i])
            dfs(r-1, g, cnt+1)
            redz.pop()
            vstp[i] = 0
        # else:
        #     for i in range(avIslCnt):
        #         if vstp[i]:
        #             continue
        #         vstp[i] = 1
        #         redz.append(avIsl[i])
        #         dfs(r-1, g, cnt+1)
        #         redz.pop()
        #         vstp[i] = 0
    else:
        for i in range(avIslCnt):
            if vstp[i]:
                continue
            vstp[i] = 1
            grnz.append(avIsl[i])
            dfs(r, g-1, cnt+1)
            grnz.pop()
            vstp[i] = 0


def bfs():
    global n, m
    v = [[0]*m for _ in range(n)]
    c = [[0]*m for _ in range(n)]
    q = deque()
    ret = 0
    for h, w in redz:
        q.append((h, w, 1, 1)) # h, w, dep, color
        v[h][w] = 1
        c[h][w] = 1
    for h, w in grnz:
        q.append((h, w, 1, 2)) # h, w, dep, color
        v[h][w] = 1
        c[h][w] = 2
    while q:
        h, w, dep, color = q.popleft()
        if v[h][w] < 0:
            continue
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and g[nh][nw] and not v[nh][nw]:
                v[nh][nw] = dep+1
                c[nh][nw] = color
                q.append((nh, nw, dep+1, color))
            elif 0<=nh<n and 0<=nw<m and g[nh][nw] and v[nh][nw]:
                if v[nh][nw] == dep+1 and c[nh][nw] != color:
                    v[nh][nw] = -1
                    ret += 1
    return ret
'''










