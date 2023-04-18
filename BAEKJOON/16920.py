'''
확장 게임

n*m 격자판. 플레이어는 하나 이상의 성.
라운드마다 성을 확장해야 함. 1이 확장 2가 확장.
각 턴마다 성을 확장해야 한다. 자기 성에서 si만큼 이동 할 수 있는 모든 칸에 성을 동시 확장. 상하좌우 인접한 칸으로. 벽이나 다른 플레이어의 성이 있는 곳으로 이동 불가. 성을 다 건설 이후 다음 플레이어 턴.
최종 상태 구하자.

입력
n, m, p 제시.
s1, s2,sp 제시.
게임판 상태 .은 빈 칸 # 은 벽 1~9는 플레이어.

출력
1이 가진 성의 수, 2가 가진 성의 수, p가 가진 성의 수를 공백으로 구분해 추력.
'''
import sys
input = sys.stdin.readline

def turn(idx):
    global n, m, p
    linez = plyli[idx]
    if not linez:
        return False
    newLinez = []
    while linez:
        h, w = linez.pop()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and not g[nh][nw]:
                g[nh][nw] = idx
                ans[idx] += 1
                newLinez.append((nh, nw))
    plyli[idx] = newLinez
    return True

mov = [(-1,0),(0,1),(1,0),(0,-1)]
n, m, p = map(int, input().rstrip().split())
sli = [0]+list(map(int, input().rstrip().split()))
g = []
ans = [0]*(p+1)
plyli = [[] for _ in range(p+1)]
for i in range(n):
    s = list(input().rstrip())
    for j in range(m):
        if s[j] == '.':
            s[j] = 0
            continue
        elif s[j] == '#':
            s[j] = -1
            continue
        else:
            ply = int(s[j])
            ans[ply] += 1
            plyli[ply].append((i, j))
            s[j] = ply
    g.append(s)

while True:
    newFla = False
    for i in range(1, p+1):
        if not plyli[i]:
            continue
        cnt = sli[i]
        while cnt:
            if not plyli[i]:
                a = False
                break
            a = turn(i)
            cnt -= 1
        if newFla:
            continue
        if a:
            newFla = True
    if not newFla:
        break

ans.pop(0)
print(*ans)

'''
# 빠른 코드

from collections import deque
import sys

input = sys.stdin.readline
N, M, P = map(int, input().split())
S = [0] + list(map(int, input().split()))
visited = [[0] * M for _ in range(N)]
result = [0] * (P + 1)
Q = [deque([]) for _ in range(10)]

for n in range(N):
    temp = list(input())
    for m in range(M):
        if temp[m] == '#':
            visited[n][m] = 1
        elif temp[m] != '.':
            visited[n][m] = 1
            result[int(temp[m])] += 1
            Q[int(temp[m])].append((n, m))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while 1:
    flag = 1
    for p in range(1, P + 1):
        for _ in range(min(S[p], max(N, M))):
            for _ in range(len(Q[p])):
                x, y = Q[p].popleft()
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        result[p] += 1
                        Q[p].append((nx, ny))
                        flag = 0
    if flag:
        break
print(' '.join(map(str, result[1:])))
'''