'''
불

빈 공간과 벽으로 이루어진 건물에 갇혀있다.
불이 났고 출구로 뛴다.
불은 동서남북으로 퍼져나간다. 벽에는 불x. 사방이동.
빌딩 얼마만에 탈출 가능?

입력
테케 수 제시. 최대 100
가로 세로 m, n 제시. 최대 100
h개 줄에 w개 문자 지도 제시.
. : 빈 공간
# : 벽
@ : 상근이 시작 위치
* : 불

출력
테케마다 가장 빠른 시간 출력. 불가능 시 IMPOSSIBLE 출력
'''
from collections import deque
import sys
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]

def bfs():
    global n, m
    while q:
        h, w, fla = q.popleft()
        if fla:
            if g[h][w] == '*':
                continue
            if h == 0 or h == n-1 or w == 0 or w == m-1:
                return v[h][w]
            for dh, dw in mov:
                nh, nw = h+dh, w+dw
                if 0<=nh<n and 0<=nw<m and g[nh][nw] == '.' and not v[nh][nw]:
                    g[nh][nw] = '@'
                    v[nh][nw] = v[h][w]+1
                    q.append((nh, nw, fla))
        else:
            for dh, dw in mov:
                nh, nw = h+dh, w+dw
                if 0<=nh<n and 0<=nw<m and (g[nh][nw] != '#' and g[nh][nw] != '*'):
                    g[nh][nw] = '*'
                    q.append((nh, nw, fla))
    return False

for _ in range(int(input())):
    m, n = map(int, input().rstrip().split())
    g = []
    v = [[0]*m for _ in range(n)]
    q = deque()
    for i in range(n):
        s = list(input().rstrip())
        g.append(s)
        for j in range(m):
            if s[j] == '@':
                sh, sw = i, j
                v[i][j] = 1
            elif s[j] == '*':
                q.append((i, j, 0))
                v[i][j] = 1
    q.appendleft((sh, sw, 1))
    ans = bfs()
    if ans:
        print(ans)
    else:
        print('IMPOSSIBLE')


