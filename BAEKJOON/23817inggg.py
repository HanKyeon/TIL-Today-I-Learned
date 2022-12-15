'''
포항항

ㅋㅋ 과메기 5인분 먹으러 가야함
n*m 사이즈 최대 1000*1000
S 현위치
K 식당 최대 20개
X 벽
. 빈 칸
5개 식당 방문 최소 시간

입력
n, m 제시.
n개 줄 m길이 문자열
'''
import sys
from collections import deque
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]

def bfs():
    global n, m, sh, sw
    v = [[[0]*20 for _ in range(m)] for _ in range(n)]
    v[sh][sw] = 1
    q = deque((sh, sw))
    while q:
        h, w= q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and g[nh][nw]>=0:
                pass

n, m = map(int, input().rstrip().split())
g = []
cnt = 0
for i in range(n):
    s = list(input().rstrip())
    for j in range(m):
        if s[j] == 'S':
            sh, sw = i, j
            s[j] = 0
        elif s[j] == 'K':
            cnt += 1
            s[j] = cnt
        elif s[j] == '.':
            s[j] = 0
        elif s[j] == 'X':
            s[j] = -1
    g.append(s)
for i in g:
    print(i)
if cnt < 5:
    print(-1)
    exit()






