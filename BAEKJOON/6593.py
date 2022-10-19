'''
상범 빌딩

탈출하는 가장 빠른 길은?
단위 정육면체로 이루어져 있다. 지나갈 수 없거나, 지나갈 수 있거나.
각 칸에서 인접한 6개의 칸으로 1분 시간 이동. 대각이동 불가. 출구로만 탈출 가능.
탈출 가능? 얼마만에?

입력
테케 제시
l, r, c 제시. l은 층수, r, c는 한 층의 행과 열의 갯수.
c개의 문자로 이루어진 r개 행이 l번 제시.
각 문자는 한 칸을 나타낸다. 막혀있으면 #, 비어있으면 . 시작 지점은 S, 탈출 출구는 E. 각 층 사이에는 빈 줄이 있으며 입력의 끝은 L, R, C가 모두 0으로 표현. 시작 지접과 출구는 항상 하나만 있다.

출력
탈출 할 수 있다면
Escaped in x minute(s).
불가능하면
Trapped!
'''
from collections import deque
import sys
input = sys.stdin.readline

mov = [(0,0,1), (0,0,-1), (1,0,0), (-1,0,0), (0,1,0), (0,-1,0)]

def bfs():
    global sl, sr, sc, l, r, c, el, er, ec
    q = deque()
    q.append((sl, sr, sc))
    v = [[[0]*c for _ in range(r)] for _ in range(l)]
    v[sl][sr][sc] = 1
    while q:
        f, h, w = q.popleft()
        for df, dh, dw in mov:
            nf, nh, nw = f+df, h+dh, w+dw
            if 0<=nf<l and 0<=nh<r and 0<=nw<c and not v[nf][nh][nw] and g[nf][nh][nw] == '.':
                v[nf][nh][nw] = v[f][h][w]+1
                q.append((nf, nh, nw))
            if 0<=nf<l and 0<=nh<r and 0<=nw<c and not v[nf][nh][nw] and g[nf][nh][nw] == 'E':
                return v[f][h][w]
    return 0

while True:
    l, r, c = map(int, input().rstrip().split())
    if not l and not r and not c:
        break
    sl, sr, sc = 0, 0, 0
    el, er, ec = 0, 0, 0
    g = []
    for i in range(l):
        layer = [list(input().rstrip('\n')) for _ in range(r)]
        g.append(layer)
        for j in range(r):
            for k in range(c):
                if layer[j][k] == 'S':
                    sl, sr, sc = i, j, k
                if layer[j][k] == 'E':
                    el, er, ec = i, j, k
        input()
    ans = bfs()
    if ans:
        print(f"Escaped in {ans} minute(s).")
    else:
        print("Trapped!")





