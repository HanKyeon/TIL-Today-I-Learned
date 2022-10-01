'''
벽 k번 부수고 이동하기.
'''
from collections import deque
import sys
input = sys.stdin.readline

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

n, m, k = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]
v = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
def bfs():
    global n, m, k
    if n==1 and m==1:
        return 1
    v[0][0][k] = 1
    q = deque([(0, 0, k)])
    while q:
        h, w, dep = q.popleft()
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if nh == n-1 and nw == m-1:
                return v[h][w][dep]+1
            if 0<=nh<n and 0<=nw<m and g[nh][nw]=='0' and not v[nh][nw][dep]:
                v[nh][nw][dep] = v[h][w][dep]+1
                q.append((nh, nw, dep))
            elif 0<=nh<n and 0<=nw<m and g[nh][nw]=='1' and dep and not v[nh][nw][dep-1]:
                v[nh][nw][dep-1] = v[h][w][dep]+1
                q.append((nh, nw, dep-1))
    return -1
print(bfs())





'''
# 벽부이 최동우씨

import sys
input = sys.stdin.readline
#왠지 주기적으로 읽혀지는듯해서 각주를 덧붙여봅니다.


R, C, K = map(int,input().split())
M=[3]*(C+2)+sum([[3]+list(map(int,(input().strip())))+[3] for i in range(R)],[])+[3]*(C+2)
#맵의 가장자리에 패딩을 줍니다. 어차피 visited로 가는 것을 방지할 것이기에 어떤 값을 줘도 됩니다.
#맵은 1차원 배열로 나타내었습니다.
C+=2
#가장자리를 주어서 좌우 길이가 1씩 총 2가 늘어납니다. 그래서 C에 2를 더해줍니다.
F = (R+1) * (C) -2
#도착지점이 속한 줄의 끝자락입니다.
#다만 인덱스가 0부터 시작하므로 1을 빼주고, 우측패딩이 1개 있으므로 1을 또 뺍니다.
visited= [99999]*(C) #상단 패딩으로 가지 못하게 방지합니다.
for i in range(R):
    visited+=[99999]+[0]*(C-2)+[99999] #좌우 끝에도 방지합니다.
visited+=[99999]*(C) #하단도 방지합니다.
visited[C+1]=2 #시작점의 visited값입니다.
#visited관리는 망치를 기준으로 합니다.
#그 이유는 더 나중에 방문하더라도 망치가 더 많은 상태로 방문하면 유효한 결과를 낼 수 있기 때문입니다.
#반면에 방문한 턴 수는 턴 자체를 일괄 관리하면 되기때문에 visited에까지 추가할 필요는 없습니다.

que=[(C+1,K+1)]
#일차원 배열이지만 이차원처럼 생각한다면 
#C가 1번째줄 0번 인덱스이므로 시작점은 1번째줄 1번 인덱스인 C+1이 됩니다.
#즉 C+1이 arr[1][1]과 동일합니다. 원래는 arr[0][0]이었겠지만 상단, 좌단에 벽을 쳤기 때문
turn=1 #시작 턴 수를 관리합니다.

while visited[F]==0 and que:
    
    nq=[]
    for p, m in que:# 포지션과 망치-현재 위치와 보유 중인 망치의 수입니다.

        if visited[p-1]<m:#망치가 더 많은 상태로 뒤늦게 방문했다면
            visited[p-1]=m#방문 값을 망치로 바꿉니다. (커질 수만 있습니다.)
            nq.append((p-1,m-M[p-1])) #움직인 칸이 0이든 1이든 상관없습니다.
                                   #0이라면 -0을 하므로 망치 수가 줄지 않기 때문입니다.
                                   #더불어서 이미 visited값이 올라갔기 때문에
                                   #같은 턴 내에서 해당 지점을 또 방문 할 수 있어도
                                   #( 예를 들어 1,1과 2,2에서 동시에 1,2로 가는 경우)
                                   #nq에 중복추가되지 않습니다.
                
        if visited[p+1]<m: #같은 작업을 총 4번해줍니다.
            visited[p+1]=m
            nq.append((p+1,m-M[p+1]))
        if visited[p-C]<m:
            visited[p-C]=m
            nq.append((p-C,m-M[p-C]))
        if visited[p+C]<m:
            visited[p+C]=m
            nq.append((p+C,m-M[p+C]))

    turn += 1
    que=nq

if visited[F]==0:
    print(-1)
else:
    print(turn)
'''










