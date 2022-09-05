'''
파이프 옮기기

파이프 밀거다. 벽 닿으면 안된다. 우방향 아랫방향 우하단 아랫방향 이동 가능. 회전은 45도로만.
가로일 때 이동 방법은  우방향 우하단방향
세로일 때 이동 방법은 하방향 우하단 방향.
대각일 때 이동 방법은 우방향 하단 우하단.
초기 파이프가 1,1 1,2를 차지하고 있을 때 N, N까지 가는 방법의 갯수

입력
집크기n
그래프. 0은 빈 칸 1은 벽

출력
N,N을 이동시키는 방법의 수 출력. 이동 못시키면 0 출력.
'''

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(10e6))
# dx, dy, 이동 후 파이프 방향
moves = [[(0, 1, 0), (1, 1, 2)], [(1, 0, 1), (1, 1, 2)], [(0, 1, 0), (1, 0, 1), (1, 1, 2)]]
ans = 0
def dfs(h, w, di):
    global ans, n
    if h == n-1 and  w == n-1:
        ans+=1
        return
    for i in moves[di]:
        nh, nw, nd = h + i[0], w + i[1], i[2]
        if (nd == 0 or nd == 1) and 0 <= nh < n and 0 <= nw < n and g[nh][nw] == 0:
            dfs(nh, nw, nd)
        elif nd == 2 and 0 <= nh < n and 0 <= nw < n and g[nh][nw] == 0 and g[nh-1][nw] == 0 and g[nh][nw-1] == 0:
            dfs(nh, nw, nd)
            # print(nh, nw, nd)

n = int(input())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]

dfs(0, 1, 0)

print(ans)

'''
dfs 메모리 초과
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(10e6))
# dx, dy, 이동 후 파이프 방향
moves = [[(0, 1, 0), (1, 1, 2)], [(1, 0, 1), (1, 1, 2)], [(0, 1, 0), (1, 0, 1), (1, 1, 2)]]
ans = 0
def dfs(h, w, di):
    global ans, n
    if h == n-1 and  w == n-1:
        ans+=1
        return
    for i in moves[di]:
        nh, nw, nd = h + i[0], w + i[1], i[2]
        if nd == 2 and 0 <= nh < n and 0 <= nw < n and g[nh][nw] == 0 and g[nh-1][nw] == 0 and g[nh][nw-1] == 0:
            dfs(nh, nw, nd)
            # print(nh, nw, nd)
        elif (nd == 0 or nd == 1) and 0 <= nh < n and 0 <= nw < n and g[nh][nw] == 0:
            dfs(nh, nw, nd)

n = int(input())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
'''

'''
# BFS 시간초과
di = 0
q = deque([(0, 1, 0)])
ans = 0
while q:
    h, w, di = q.popleft()
    # print(h, w, di)
    if h == n-1 and w == n-1:
        ans+=1
        continue
    for i in moves[di]:
        nh, nw, nd = h + i[0], w + i[1], i[2]
        if nd == 2 and 0 <= nh < n and 0 <= nw < n and g[nh][nw] == 0 and g[nh-1][nw] == 0 and g[nh][nw-1] == 0:
            q.append((nh, nw, nd))
            # print(nh, nw, nd)
        elif (nd == 0 or nd == 1) and 0 <= nh < n and 0 <= nw < n and g[nh][nw] == 0:
            q.append((nh, nw, nd))

print(ans)
'''




