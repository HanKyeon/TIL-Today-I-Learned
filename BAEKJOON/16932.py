'''
모양 만들기

n*m 배열.
0 하나를 1로 바꿔서 얻을 수 있는 최대 1의 연속 갯수.

입력
n, m 제시.
그래프 제시.

출력
0 하나 바꿔서 만들 수 있는 최대 1덩이
'''
from collections import deque
import sys
input = sys.stdin.readline

mov = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def bfs(h, w, cnt):
    global n, m
    v[h][w] = cnt
    q = deque([(h, w)])
    icnt = 1
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and g[nh][nw] and not v[nh][nw]:
                v[nh][nw] = cnt
                q.append((nh, nw))
                icnt+=1
    parent.append(icnt)

n, m = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
parent = [0]
zrs = []
cnt = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            zrs.append((i, j))
            continue
        if g[i][j] and not v[i][j]:
            cnt += 1
            bfs(i, j, cnt)

ans = 0
for h, w in zrs:
    sets = set()
    for dh, dw in mov:
        nh, nw = h+dh, w+dw
        if 0<=nh<n and 0<=nw<m and v[nh][nw]:
            sets.add(v[nh][nw])
    cnt = 0
    for i in sets:
        cnt += parent[i]
    if cnt>ans:
        ans = cnt

print(ans+1)


'''
# 빠름

import sys
from collections import deque
rdln = sys.stdin.readline
dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]

def bfs(n, m):
    
    group_no = 2
    group = [0, 0,]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                # print((i,j))
                queue = deque()
                # visit = [[False] * m for _ in range(n)]
                queue.append((i,j))
                arr[i][j] = group_no
                cnt = 1
                while queue:
                    y, x = queue.popleft()
                    for k in range(4):
                        ny, nx = y+dy[k], x+dx[k]
                        if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 1:
                            # visit[ny][nx] = True
                            arr[ny][nx] = group_no
                            queue.append((ny , nx))
                            cnt += 1
                
                group.append(cnt)
                group_no += 1
    return group

n, m = map(int,rdln().split())
arr = [list(map(int, rdln().split())) for _ in range(n)]

group = bfs(n, m)
# print(arr)
# print(group)

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            gr = set()
            for k in range(4):
                ny, nx = i+dy[k], j+dx[k]
                if 0 <= ny < n and 0 <= nx < m and arr[ny][nx]:
                    gr.add(arr[ny][nx])
            
            temp = 0
            for no in gr:
                temp += group[no]
            
            ans = max(ans, temp+1)

sys.stdout.write(f"{ans}\n")
'''




