'''
과외맨

첫 타일에서 마지막 타일로 이동하는 가장 짧은 경로를 찾아야 한다. row major order에 의해 번호가 매겨져 있으며, 첫 타일 번호는 1, 마지막 타일 번호는 n이다. 두 번째 ㅜㅈㄹ의 첫 타일 번호는 n+1이고 마지막 타일의 번호는 2*n-1이다.
첫 줄의 첫 타일로만 과외맨이 들어갈 수 있고, 마지막 타일 위에 과외 노트가 있다.
마지막 줄의 마지막 타일로 이동할 수 없는 경우에는 번호가 가장 큰 타일로 이동하면 된다.

입력
n 제시.
n*n-n//2 줄에는 a, b 제시. 타일 i의 왼쪽에 쓰여진 숫자는 a, 오른 쪽에 쓰여진 숫자는 b이다.

출력
가장 짧은 경로의 길이(타일 갯수) 출력
경로 상 타일의 번호를 공백으로 구분하여 순서대로 출력.
'''
import sys
from collections import deque
input = sys.stdin.readline

mov = [(-1,0),(0,1),(1,0),(0,-1)]

n = int(input())
maxCnt = n*n-n//2+1
g = [[] for _ in range(n)]
parsingV = [[] for _ in range(n)]
cnt = 0
for i in range(1, maxCnt):
    a, b = map(int, input().rstrip().split())
    if not cnt%2:
        if len(g[cnt]) >= 2*n:
            cnt += 1
        g[cnt].append(a)
        g[cnt].append(b)
        parsingV[cnt].append(i)
        parsingV[cnt].append(i)
    else:
        if len(g[cnt]) >= 2*n-2:
            g[cnt] = [0]+g[cnt][:]+[0]
            parsingV[cnt] = [0]+parsingV[cnt][:]+[0]
            cnt += 1
        g[cnt].append(a)
        g[cnt].append(b)
        parsingV[cnt].append(i)
        parsingV[cnt].append(i)
v = [[0]*(2*n) for _ in range(n)]
def lego():
    q = deque([(0,0)])
    v[0][0], v[0][1] = 1, 1
    while q:
        h, w1 = q.popleft()
        w2 = w1-1 if w1%2 else w1+1
        if w1 > w2:
            w1, w2 = w2, w1
        for dh, dw in mov:
            nh, nw1, nw2 = h+dh, w1+dw, w2+dw
            if 0<=nh<n:
                if 0<=nw1<n*2:
                    if not v[nh][nw1] and g[nh][w1] == g[nh][nw1]:
                        nnw = nw1-1 if nw1%2 else nw1+1
                        v[nh][nw1], v[nh][nnw] = v[h][w1]+1, v[h][w1]+1
                        q.append((nh, nw1))
                        q.append((nh, nnw))
                if 0<=nw2<n*2:
                    if not v[nh][nw2] and g[nh][w2] == g[nh][nw2]:
                        nnw = nw2-1 if nw2%2 else nw2+1
                        v[nh][nw2], v[nh][nnw] = v[h][w2]+1, v[h][w2]+1
                        q.append((nh, nw2))
                        q.append((nh, nnw))
lego()
for i in v:
    print(i)

'''
from collections import deque
import sys
input = sys.stdin.readline
dx1 = [-1, 0, 1, 1, 0, -1]
dy1 = [1, 1, 1, 0, -1, 0]
dx2 = [-1, 0, 1, 1, 0, -1]
dy2 = [0, 1, 0, -1, -1, -1]


def bfs(x, y):
    q.append([x, y])
    c[x][y] = 1
    while q:
        x, y = q.popleft()
        if x % 2 == 1:
            dx, dy = dx1, dy1
        else:
            dx, dy = dx2, dy2
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if c[nx][ny] == 0:
                    if i <= 2:
                        if a[x][y][1] == a[nx][ny][0]:
                            c[nx][ny] = c[x][y] + 1
                            dir[nx][ny] = [x, y]
                            q.append([nx, ny])
                    else:
                        if a[x][y][0] == a[nx][ny][1]:
                            c[nx][ny] = c[x][y] + 1
                            dir[nx][ny] = [x, y]
                            q.append([nx, ny])


n = int(input())
a = [[[[] for _ in range(2)] for _ in range(n)] for _ in range(n)]
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            x, y = map(int, input().split())
            a[i][j] = [x, y]
    else:
        for j in range(n-1):
            x, y = map(int, input().split())
            a[i][j] = [x, y]

label = [[[] for _ in range(n)] for _ in range(n)]
num = 0
for i in range(n):
    for j in range(n):
        if i % 2 == 1 and j == n-1:
            continue
        num += 1
        label[i][j] = num

q = deque()
c = [[0]*n for _ in range(n)]
dir = [[[] for _ in range(n)] for _ in range(n)]
bfs(0, 0)

flag, ans = 0, []
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if c[i][j]:
            print(c[i][j])
            ans.append(label[i][j])
            x, y = i, j
            while x > 0 or y > 0:
                nx, ny = dir[x][y]
                ans.append(label[nx][ny])
                x, y = nx, ny
            flag = 1
            break
    if flag:
        break
ans.reverse()
for s in ans:
    print(s, end=' ')
'''
















