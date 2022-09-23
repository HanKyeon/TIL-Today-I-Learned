'''
다리 만들기

여러 섬으로 이뤄진 나라. 가장 짧은 다리 하나 만드는 다리 길이.

입력
지도 크기 n
n개의 숫자가 빈 칸을 사이에 두고 제시.
0은 바다, 1은 육지. 항상 두 개 이상의 섬이 있는 데이터만 제시.

출력
가장 짧은 다리 길이
'''
from collections import deque
import sys
input = sys.stdin.readline

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

def bfs(h, w):
    global n
    ret = set()
    v[h][w] = 1
    q = deque([(h, w)])
    while q:
        h, w = q.popleft()
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<n and g[nh][nw] and not v[nh][nw]:
                v[nh][nw] = 1
                q.append((nh, nw))
            if 0<=nh<n and 0<=nw<n and not g[nh][nw]:
                ret.add((h, w))
    ili.append(ret)

def check(li1, li2):
    global ans
    ret = int(10e9)
    for x1, y1 in li1:
        for x2, y2 in li2:
            ret = min(ret, abs(x1-x2) + abs(y1-y2))
    ans = min(ret, ans)

n = int(input())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
v = [[0] * n for _ in range(n)]
ili = []
for i in range(n):
    for j in range(n):
        if g[i][j] == 0:
            continue
        if v[i][j]:
            continue
        bfs(i, j)
ans = int(10e9)
for i in range(len(ili)-1):
    for j in range(i+1, len(ili)):
        check(ili[i], ili[j])
print(ans-1)





















