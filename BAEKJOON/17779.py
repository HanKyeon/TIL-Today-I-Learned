'''
게리맨더링 2

크기가 n*n 격자. 각 칸은 구역
r행 c열은 r,c로 표현. 구역을 5개로 나눠야 하고, 각 구역은 다섯 선거구 중 하나에 포함되어야 한다.
선거구는 구역을 적어도 하나 포함해야하고, 한 선거구에 포함되어있는 구역은 모두 연결되어있어야 한다. 구역 a에서 인접한 구역을 통해 구역 b로 갈 수 있을 때, 두 구역은 연결되어 있다고 한다.

선거구 나누기
1. 기준점 x, y와 경계의 길이 d1, d2 정하기.
(d1, d2 >= 1, 1<=x<x+d1+d2<=n, 1<=y-d1<y<y+d2<=n)
2. 경계선은 대각선으로.
3. 경계선과 경계선 안의 구역이 5번 선거구
4. 5번 선거구가 아닌 구역 중
1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N

구역 A[r][c]가 인구. 선거구를 나누는 방법 중에서 인구 차이가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값. 최대한 비슷하게 해라.

입력
크기 n 제시.
그래프 제시.

출력
인구가 가장 많은 선거구-가장 적은 선거구 최솟값
'''
from collections import deque
import sys
input = sys.stdin.readline

# 반시계 방향으로 회전.
dh = [1, 1, -1, -1]
dw = [-1, 1, 1, -1]
moves = [(1,0),(-1,0),(0,1),(0,-1)]

def 레쓰고(bh, bw, d1, d2): # d1이 //이방향->1,3 방향 d2가 \\이 방향.-> 0,2 방향
    global ans
    v = [[0]*n for _ in range(n)]
    q = deque()
    v[bh][bw] = 5
    q.append((bh, bw, 0, 0)) # h, w, depth, direction
    while q:
        h, w, dep, di = q.popleft()
        # print(h, w, dep, di)
        if di % 2 and dep == d2:
            di += 1
            dep = 0
        elif not di%2 and dep == d1:
            di += 1
            dep = 0
        if di == 4:
            break
        # print(h, w, dep, di)
        nh, nw = h+dh[di], w+dw[di]
        # print(nh, nw, dep, di)
        v[nh][nw] = 5
        q.append((nh, nw, dep+1, di))
    # for i in v:
    #     print(i)

    v[0][0] = 1
    q = deque([(0, 0)])
    sum1 = g[0][0]
    while q:
        h, w = q.popleft()
        for ddh, ddw in moves:
            nh, nw = h+ddh, w+ddw
            # 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
            if 0<=nh<bh+d1 and 0<=nw<=bw and not v[nh][nw]:
                q.append((nh, nw))
                v[nh][nw] = 1
                sum1 += g[nh][nw]
    # for i in v:
    #     print(i)
    # print('===========')
    v[0][n-1] = 2
    q = deque([(0, n-1)])
    sum2 = g[0][n-1]
    while q:
        h, w = q.popleft()
        for ddh, ddw in moves:
            nh, nw = h+ddh, w+ddw
            # 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
            if 0<=nh<=bh+d2 and bw<nw<=n-1 and not v[nh][nw]:
                q.append((nh, nw))
                v[nh][nw] = 2
                sum2 += g[nh][nw]
    # for i in v:
    #     print(i)
    # print('===========')
    v[n-1][0] = 3
    q = deque([(n-1, 0)])
    sum3 = g[n-1][0]
    while q:
        h, w = q.popleft()
        for ddh, ddw in moves:
            nh, nw = h+ddh, w+ddw
            # 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
            if bh+d1-1<=nh<=n-1 and 0<=nw<bw-d1+d2 and not v[nh][nw]:
                q.append((nh, nw))
                v[nh][nw] = 3
                sum3 += g[nh][nw]
    # for i in v:
    #     print(i)
    # print('===========')
    v[n-1][n-1] = 4
    q = deque([(n-1, n-1)])
    sum4 = g[n-1][n-1]
    while q:
        h, w = q.popleft()
        for ddh, ddw in moves:
            nh, nw = h+ddh, w+ddw
            # 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
            if bh+d2-1<nh<=n-1 and bw-d1+d2<=nw<=n-1 and not v[nh][nw]:
                q.append((nh, nw))
                v[nh][nw] = 4
                sum4 += g[nh][nw]
    # for i in v:
    #     print(i)
    # print('===========')
    sum5 = sum(map(sum, g)) - sum((sum1, sum2, sum3, sum4))
    ans = min(ans, max(sum1, sum2, sum3, sum4, sum5)-min(sum1, sum2, sum3, sum4, sum5))

n = int(input())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
ans = int(10e9)
for i in range(n): # x
    for j in range(n): # y
        for d1 in range(1, n-1):
            for d2 in range(1, n-1):
                # 1<=x<x+d1+d2<=n, 1<=y-d1<y<y+d2<=n
                if 0<=i<i+d1+d2<n and 0<=j-d1<j<j+d2<n:
                    레쓰고(i, j, d1, d2)

print(ans)



'''
# 미친 아재
import sys; R = sys.stdin.readline
n = int(R())
map1 = [[*map(int,R().split())] for _ in range(n)]
for i in range(n):
    for j in range(1,n):
        map1[i][j] += map1[i][j-1]
tot = sum(row[-1] for row in map1)

res = float("inf")
for d1 in range(1,n-2):
    for d2 in range(1,n-1-d1):
        for x in range(n-d1-d2):
            for y in range(d1,n-d2):
                pop1,pop2,pop3,pop4 = 0,0,0,0
                for i in range(x): 
                    pop1 += map1[i][y]; pop2 += map1[i][-1]-map1[i][y]
                for i in range(x,x+d1): pop1 += map1[i][y-1-i+x]
                for i in range(x,x+d2+1): pop2 += map1[i][-1]-map1[i][y+i-x]
                for i in range(x+d1,x+d1+d2+1): pop3 += map1[i][y-d1-1+i-x-d1] if y-d1 else 0
                for i in range(x+d2+1,x+d1+d2+1): pop4 += map1[i][-1]-map1[i][y+d2-i+x+d2]
                for i in range(x+d1+d2+1,n):
                    pop3 += map1[i][y-d1+d2-1]; pop4 += map1[i][-1]-map1[i][y-d1+d2-1]
                a,_,_,_,b = sorted([pop1,pop2,pop3,pop4,tot-pop1-pop2-pop3-pop4])
                res = res if b-a>res else b-a
print(res)
'''












