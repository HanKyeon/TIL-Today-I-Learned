'''
군대 탈출하기

칸마다 제한 레벨 있고, 한 번 렙 무시 가능. 최소 필요 레벨 구해라.

입력
n, m  제시.
그래프 제시. 레벨

출력
최소레벨 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]
def bfs(maxlv):
    if g[0][0] > maxlv:
        return False
    q = deque([(0, 0, 1)])
    v[0][0][1] = 1
    while q:
        h, w, cnt = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m:
                if g[nh][nw] <= maxlv and not v[nh][nw][cnt]:
                    if nh == n-1 and nw == m-1:
                        return True
                    v[nh][nw][cnt] = 1
                    q.append((nh, nw, cnt))
                elif g[nh][nw] > maxlv and cnt:
                    nh, nw = nh+dh, nw+dw
                    if 0<=nh<n and 0<=nw<m and not v[nh][nw][cnt-1] and g[nh][nw] <= maxlv:
                        if nh == n-1 and nw == m-1:
                            return True
                        v[nh][nw][cnt-1] = 1
                        q.append((nh, nw, cnt-1))
    return False

n, m = map(int, input().rstrip().split())
g = []
sta, end = 0, 0
for _ in range(n):
    s = list(map(int, input().rstrip().split()))
    for i in s:
        if i > end:
            end = i
    g.append(s)
ans = end
while sta <= end:
    mid = (sta+end)//2
    v = [[[0,0] for _ in range(m)] for _ in range(n)]
    if bfs(mid):
        if ans > mid:
            ans = mid
        end = mid-1
    else:
        sta = mid+1
print(ans)

'''
# 힙으로 한 번만 훑은듯?
# 14948
import sys
from heapq import *
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cost_unused = [[float('inf') for _ in range(m)] for _ in range(n)]
cost_used = [[float('inf') for _ in range(m)] for _ in range(n)]
cost_unused[0][0] = graph[0][0]
cost_used[0][0] = graph[0][0]
def dijkstra() :
    hq = [(cost_unused[0][0], False, 0, 0)]
    while hq :
        cost, used, x, y = heappop(hq)
        if (not used) and cost_unused[x][y] < cost :
            continue
        elif used and cost_used[x][y] < cost :
            continue
        for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
            nx, ny = x+a, y+b
            if not (0 <= nx < n and 0 <= ny < m) :
                continue
            ncost = max(cost, graph[nx][ny])
            if (not used) and cost_unused[nx][ny] > ncost:
                cost_unused[nx][ny] = ncost
            elif used and cost_used[nx][ny] > ncost:
                cost_used[nx][ny] = ncost
            else :
                continue
            heappush(hq, (ncost, used, nx, ny))
        if used :
            continue
        for a, b in [(2, 0), (-2, 0), (0, 2), (0, -2)] :
            nx, ny = x+a, y+b
            if not (0 <= nx < n and 0 <= ny < m) :
                continue
            ncost = max(cost, graph[nx][ny])
            if cost_used[nx][ny] > ncost:
                cost_used[nx][ny] = ncost
                heappush(hq, (ncost, True, nx, ny))
    return min(cost_unused[n-1][m-1], cost_used[n-1][m-1])
print(dijkstra())
'''



'''
10 10
0 0 0 0 0 9 9 9 9 9
9 9 9 9 0 9 9 9 9 9
0 0 0 9 0 9 9 9 9 9
0 9 0 9 0 9 9 9 9 9
0 9 0 0 0 9 9 9 9 9
0 9 9 9 0 9 9 9 9 9
0 9 9 9 9 9 9 9 9 9
0 0 0 0 0 0 0 0 0 0
0 9 9 9 0 9 9 9 9 9
9 9 9 9 0 9 9 9 9 0

5 6 
5 5 5 5 7 100
7 7 7 7 5 7
7 7 7 7 5 7
7 7 7 7 5 7
7 7 7 7 5 5
'''