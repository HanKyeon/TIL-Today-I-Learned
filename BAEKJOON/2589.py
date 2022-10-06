'''
보물섬

육지 내 가장 긴 거리에 묻혀있다. 탐색해라.

입력
n, m 제시.
L W로 이뤄진 지도 제시. L은 육지 W는 물

출력
보물 사이 최단거리
'''
from collections import deque
import sys
input = sys.stdin.readline

mov = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(h, w):
    v = [[0]*m for _ in range(n)]
    q = deque([(h, w, 0)])
    v[h][w] = 1
    while q:
        h, w, cnt = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and g[nh][nw] == 'L' and not v[nh][nw]:
                v[nh][nw] = 1
                q.append((nh, nw, cnt+1))
    return cnt

n, m = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]
dp = [[] for _ in range(4)]
ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 'W':
            continue
        ans = max(ans, bfs(i, j))
print(ans)

'''
# 시간이 많이 짧다. 뭔가 아이디어가 들어간 듯
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, cnt):
    v = [[-1] * m for _ in range(n)]
    q = deque([(x, y)])
    v[x][y] = 0

    lx, ly = 0, 0
    length = 0
    while q:
        x, y = q.popleft()

        lx, ly = x, y
        length = max(length, v[x][y])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny] != cnt:
                continue
            if v[nx][ny] != -1:
                continue

            v[nx][ny] = v[x][y] + 1
            q.append((nx, ny))
    return lx, ly, length

if __name__ == '__main__':
    n, m = mis()
    MAP = [si().strip() for _ in range(n)]
    
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] or MAP[i][j] == 'W':
                continue
            
            cnt += 1
            q = deque([(i, j)])
            visited[i][j] = cnt
            
            while q:
                x, y = q.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny]:
                        continue
                    if MAP[nx][ny] == 'W':
                        continue
                    
                    visited[nx][ny] = cnt
                    q.append((nx, ny))
    
    ans = 0
    while cnt:
        for i in range(n):
            for j in range(m):
                if visited[i][j] == cnt:
                    lx, ly, _ = bfs(i, j, cnt)
                    _, _, length = bfs(lx, ly, cnt)
                    ans = max(ans, length)
                    break
        cnt -= 1
    print(ans)
'''









