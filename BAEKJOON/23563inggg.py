'''
벽 타기

H, W 격자 이동 할 것. 한 칸에 하나.
벽에 인접한 칸 to 벽에 인접한 칸은 벽 타고 이동.

힙큐 쓰자.

입력
H, W 제시.
#은 벽
.은 빈 칸
s는 시작점
E는 도착점
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

n, m = map(int, input().rstrip().split())
g = []
v = [[255555]*m for _ in range(n)]
eh, ew = 0, 0
heap = []
for i in range(n):
    s = list(input().rstrip())
    g.append(s)
    for j in range(m):
        if s[j] == 'S':
            v[i][j] = 0
            heappush(heap, (0, 0, i, j))
        elif s[j] == 'E':
            eh, ew = i, j
            g[i][j] = '.'
        elif s[j] == '#':
            pass




'''
# 하나 동떨어진거 고려를 안했다.

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

mov = [(-1,0),(0,1),(1,0),(0,-1)]

n, m = map(int, input().rstrip().split())
g = []
v = [[255555]*m for _ in range(n)]
eh, ew = 0, 0
heap = []
for i in range(n):
    s = list(input().rstrip())
    g.append(s)
    for j in range(m):
        if s[j] == 'S':
            v[i][j] = 0
            heappush(heap, (0, 0, i, j))
        elif s[j] == 'E':
            eh, ew = i, j
            g[i][j] = '.'
while heap:
    cnt, fla, h, w = heappop(heap)
    if v[h][w] < cnt:
        continue
    lfl = False
    
    for dh, dw in mov:
        nh, nw = h+dh, w+dw
        if 0<=nh<n and 0<=nw<m and g[nh][nw] == '#' and v[nh][nw] > cnt:
            v[nh][nw] = cnt
            heappush(heap, (cnt, -1, nh, nw))
        elif 0<=nh<n and 0<=nw<m and g[nh][nw] == '.' and fla and v[nh][nw] > cnt:
            v[nh][nw] = cnt
            heappush(heap, (cnt, 0, nh, nw))
        elif 0<=nh<n and 0<=nw<m and g[nh][nw] == '.' and not fla and v[nh][nw] > cnt+1:
            v[nh][nw] = cnt+1
            heappush(heap, (cnt+1, 0, nh, nw))
for i in v:
    print(i)
print(cnt)

'''
