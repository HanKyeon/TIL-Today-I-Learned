'''
공주님을 구해라!

n,m 크기 성 1,1 진입.
T시간 내로 만나야 한다. 그람 쥐면 벽 부숨.
구할 수 있는지, 구할 수 있다면 얼마나 빨리 가능한지.

입력
성 크기 제한시간 제시. n, m, t
그래프 제시. 1은 벽 2는 그람

출력
T 이내로 가능하면 최단 시간. 못하면 Fail 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global n, m, t
    v = [[0]*m for _ in range(n)]
    v[0][0] = 1
    q = deque([(0, 0)])
    swd = 10001
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and not v[nh][nw]:
                if g[nh][nw] == 1:
                    continue
                if g[nh][nw] == 2:
                    swd = v[h][w]+abs(n-nh-1)+abs(m-nw-1)
                v[nh][nw] = v[h][w]+1
                q.append((nh, nw))
    ret = v[n-1][m-1]-1 if v[n-1][m-1] else 10001
    if swd < ret:
        ret = swd
    if ret > t:
        ret = "Fail"
    return ret

mov = [(-1,0), (0,1), (1,0), (0,-1)]
n, m, t = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
ans = bfs()
print(ans)



