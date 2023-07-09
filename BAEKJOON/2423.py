'''
전구를 켜라

n*m 격자 회로.
90도 타일 회전 가능.
전구에 불을 켜기 위해 돌려야 하는 칸의 갯수의 최솟값

입력
n, m 제시. 회로 상태는 / or \

출력
정답 출력. 몇 칸 돌려야 켜지는지, 불가능하면 "NO SOLUTION"
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def dij():
    global n, m
    dst = [[555]*(m+1) for _ in range(n+1)]
    heap = [(0, 0, 0)]  # 가중치, h, w
    dst[0][0] = 0
    while heap:
        t, h, w = heappop(heap)
        if dst[h][w] < t:
            continue
        # if dst[n][m] != 555:
        #     return dst[n][m]
        # print(f"h: {h}, w:{w}, t: {t}, {dst[h][w]}")
        for dt, dh, dw in g[h][w]:
            nt, nh, nw = t+dt, h+dh, w+dw
            if 0 <= nh <= n and 0 <= nw <= m and dst[nh][nw] > nt:
                dst[nh][nw] = nt
                heappush(heap, (nt, nh, nw))
    return "NO SOLUTION" if dst[n][m] == 555 else dst[n][m]


n, m = map(int, input().rstrip().split())
g = [[[] for _ in range(m+1)] for _ in range(n+1)]
for i in range(n):
    s = list(input().rstrip())
    for j in range(m):
        if s[j] == "/":
            g[i][j].append((1, 1, 1))
            if 0 <= i+1 <= n and 0 <= j+1 <= m:
                g[i+1][j+1].append((1, -1, -1))
            if 0 <= j+1 <= m:
                g[i][j+1].append((0, 1, -1))
            if 0 <= i+1 <= n:
                g[i+1][j].append((0, -1, 1))
        else:
            g[i][j].append((0, 1, 1))
            if 0 <= i+1 <= n and 0 <= j+1 <= m:
                g[i+1][j+1].append((0, -1, -1))
            if 0 <= j+1 <= m:
                g[i][j+1].append((1, 1, -1))
            if 0 <= i+1 <= n:
                g[i+1][j].append((1, -1, 1))
print(dij())

'''
# 빠른 코드
import sys
input = sys.stdin.readline

dir = [[-1,-1], [-1,1], [1,-1], [1,1]]
n,m = map(int, input().split())
arr = [[0]*(m+1) for i in range(n+1)]
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == '\\':
            arr[i][j] |= 1<<3
            arr[i+1][j+1] |= 1<<0
        if s[j] == '/':
            arr[i][j+1] |= 1<<2
            arr[i+1][j] |= 1<<1
q = [(0,0)]
visited = [[0]*(m+1) for i in range(n+1)]
visited2 = [[0]*(m+1) for i in range(n+1)]
visited[0][0] = 1
res = -1
cycle = 0
while q and res == -1:
    nq = []
    while q:
        i,j = q.pop()
        if i == n and j == m:
            res = cycle
            break
        for d in range(4):
            ni,nj = i+dir[d][0], j+dir[d][1]
            
            if ni > -1 and ni <= n and nj > -1 and nj <= m and not visited[ni][nj]:
                if arr[i][j] & 1<<d == 0:
                    if not visited2[ni][nj]:                        
                        nq += [(ni,nj)]
                else:
                    visited[ni][nj] = 1
                    q += [(ni,nj)]
                visited2[ni][nj] = 1
    q = nq
    cycle += 1

print('NO SOLUTION' if res == -1 else res)
'''

'''
4 6
\\\/\/
/\\\\\
//\///
////\\
답 : 0

4 6
\\\\\\
\\\\\\
\\\///
\\\\//
답 : 1
    
1 1
\
답:0
    
2 2
/\
\/
답:2
    
1 2
/\
답: no solution

4 4
\/\/
\/\\
\///
\/\/
답: 1

7 7
\/\/\//
\/\////
\//\//\
\/\////
\//\//\
\/\////
\/\////
답: 2
'''
