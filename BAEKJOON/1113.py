'''
수영장 만들기

n*m 수영장 만들 것. 높이가 쓰여있는 땅이 있다.
물은 항상 높이가 더 낮은 곳으로만 흐르고, 직육면체 위의 표면에는 물이 없다.
땅의 높이는 0이고, 땅은 물을 무한대로 흡수 가능.
땅의 모양 제시, 수영장에 물이 얼마만큼 있을 수 있는지 구해라.

입력
첫째 줄에 N, M 제시. 50이하 자연수
n개 줄에 땅의높이 제시. 1이상 9이하 자연수

출력
정답 출력
'''
from collections import deque
import sys
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]

def bfs(h, w):
    global n, m
    ret = 1
    q = deque([(h, w)])
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and g[nh][nw]<ng[nh][nw] and not v[nh][nw]:
                ng[nh][nw] -= 1
                v[nh][nw] = 1
                q.append((nh, nw))
                ret += 1
    return ret

n, m = map(int, input().rstrip().split())
g = [list(map(int, list(input().rstrip()))) for _ in range(n)]
maxv = max(map(max, g))
ng = [[maxv]*m for _ in range(n)]

a = -1
while a:
    v = [[0]*m for _ in range(n)]
    a = 0
    for i in range(n):
        for j in (0, m-1):
            if g[i][j] == ng[i][j] or v[i][j]:
                continue
            v[i][j] = 1
            ng[i][j] -= 1
            a += bfs(i, j)
    for i in (0, n-1):
        for j in range(1, m-1):
            if g[i][j] == ng[i][j] or v[i][j]:
                continue
            v[i][j] = 1
            ng[i][j] -= 1
            a += bfs(i, j)
for i in ng:
    print(i)
os, ns = sum(map(sum, g)), sum(map(sum, ng))
print(ns-os)


# 테스트 용도로 해봅시다.

