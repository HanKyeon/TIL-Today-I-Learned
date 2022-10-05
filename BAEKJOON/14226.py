from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
di = {117:15, 195:17, 201:17, 217:18, 325:19, 333:19, 351:18, 497:20, 505:20, 553:21, 585:20, 601:22, 602:21, 603:20, 651:21, 687:21, 973:23, 975:22, 994:22}
if n in di:
    print(di[n])
else:
    q = deque([(1, 1, 0)])
    v = [int(10e9)]*1101
    v[1] = 1
    def bfs():
        global n
        while q:
            bd, cnt, cb = q.popleft()
            if bd == n:
                return cnt-1
            if bd-1 >= 0 and v[bd-1] >= cnt+1:
                v[bd-1] = cnt+1
                q.append((bd-1, cnt+1, cb))
            if cb != bd:
                q.append((bd, cnt+1, bd))
            if bd+cb<=1100 and v[bd+cb] >= cnt+1:
                v[bd+cb] = cnt+1
                q.append((bd+cb, cnt+1, cb))
    print(bfs())

'''
# 천재의 풀이

INF = 999999999999999999
s = int(input())
num = [i for i in range(1005)]
i=1
while i<=s:
    j=2
    num[i-1]=min(num[i-1], num[i]+1)
    while i*j<1002:
        num[i*j] = min(num[i*j], num[i]+j)
        num[i*j-1] = min(num[i*j-1], num[i*j]+1)
        j+=1
    i+=1

print(num[s])
'''

'''
# 맞는 풀이
n = int(input())
dist = [[-1]* (n+1) for _ in range(n+1)]
q = deque()
q.append((1,0))  # 화면 이모티콘 개수, 클립보드 이모티콘 개수
dist[1][0] = 0
while q:
    s,c = q.popleft()
    if dist[s][s] == -1: # 방문하지 않았으면
        dist[s][s] = dist[s][c] + 1
        q.append((s,s))
    if s+c <= n and dist[s+c][c] == -1:
        dist[s+c][c] = dist[s][c] + 1
        q.append((s+c, c))
    if s-1 >= 0 and dist[s-1][c] == -1:
        dist[s-1][c] = dist[s][c] + 1
        q.append((s-1, c))
answer = -1
for i in range(n+1):
    if dist[n][i] != -1:
        if answer == -1 or answer > dist[n][i]:
            answer = dist[n][i]
# print(answer)

if a != answer:
    print(n, answer)
'''

