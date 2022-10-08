'''
로봇 조종하기

n*m 배열.
0,0에서 n-1,m-1로 이동시켜야 한다.
좌, 우, 하 이동 가능.
한 번 탐사한 곳은 탐사하지 않는다.
지역마다 가치가 존재. 가치 합 최대가 되도록 만든다.
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [[0]*m for _ in range(n)]
dp[0][0] = g[0][0]
# 첫 줄 dp
for i in range(m-1):
    dp[0][i+1] = dp[0][i]+g[0][i+1]
# dp
for i in range(1, n):
    ddp = [dp[i-1][k]+g[i][k] for k in range(m)] # 아랫방향 dp
    rdp = ddp[:] # 우방향 dp
    ldp = ddp[:] # 좌방향 dp
    for j in range(m-1):
        rdp[j+1] = max(rdp[j+1], rdp[j]+g[i][j+1])
    for j in range(m-1, 0, -1):
        ldp[j-1] = max(ldp[j-1], ldp[j]+g[i][j-1])
    if i != n-1:
        dpl = list(map(max, zip(ddp, rdp, ldp)))
    else:
        dpl = list(map(max, zip(ddp, rdp)))
    dp[i] = dpl

print(dp[-1][-1])


'''
# 빠른 코드
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
mars = [[*map(int,input().split())] for _ in range(n)]
dp = [0]*m
dp[0] = mars[0][0]
for i in range(1,m):
    dp[i] = dp[i-1] + mars[0][i]

def sol():
    l2r = [0]*m
    r2l = [0]*m
    for i in range(1,n):
        l2r[0] = dp[0] + mars[i][0]
        for j in range(1,m):
            l2r[j] = max(l2r[j-1], dp[j]) + mars[i][j]
        r2l[m-1] = dp[m-1] + mars[i][m-1]
        for j in range(m-2,-1,-1):
            r2l[j] = max(r2l[j+1], dp[j]) + mars[i][j]
        for j in range(m):
            dp[j] = max(r2l[j], l2r[j])
    return dp[m-1]

print(sol())
'''







'''
heap = [(g[0][0], 0, 0, 1)]
while heap:
    cost, h, w, cnt = heappop(heap)
    if dst[h][w] > cost:
        continue
    # if h==n-1 and w==m-1:
    #     break
    v[h][w] = 1
    for dh, dw in mov:
        nh, nw = h+dh, w+dw
        if 0<=nh<n and 0<=nw<m and dst[nh][nw] > cost-g[nh][nw] and not v[nh][nw]:
            dst[nh][nw] = cost-g[nh][nw]
            heappush(heap, (cost-g[nh][nw], nh, nw, cnt+1))
for i in dst:
    print(i)
'''









