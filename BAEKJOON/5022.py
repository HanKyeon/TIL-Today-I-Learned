'''
연결

전기 회로에서 두 점을 전선으로 이을 때, 길이는 짧을수록 좋다.
n*m 회로에서 a1, a2, b1,b2를 전선을 이용해 이으려 한다. 전선은 항상 그리드의 수직 수평선에 잇어야 하고, 접하면 안된다.
이 때 필요한 전선 길이의 최솟값을 구해라. 전선은 밖으론 못나감

입력
n, m 제시.
4개 줄 a1,a2,b1,b2 제시. 좌표는 두 정수쌍으로 이뤄져있고, 첫 좌표는 0이상 n이하이며 두번째 좌표는 0이상 m이하.

출력
a1-a2, b1-b2 연결하는데 필요한 전선의 길이 최솟값 출력. 불가능하다면 IMPOSSIBLE
'''
import sys
from collections import deque
input = sys.stdin.readline

mov = [(-1,0),(0,1),(1,0),(0,-1)]

def dstt(a1h,a1w,a2h,a2w,b1h,b1w,b2h,b2w):
    v = [[0]*(m+1) for _ in range(n+1)]
    path = [[(0, 0) for _ in range(m+1)] for _ in range(n+1)]
    v[b1h][b1w], v[b2h][b2w] = 1, 1
    dis1 = bfs(a1h,a1w,a2h,a2w,v,path)
    v = [[0]*(m+1) for _ in range(n+1)]
    ch, cw = a2h,a2w
    while True:
        v[ch][cw]=1
        if ch==a1h and cw==a1w:
            break
        ch,cw = path[ch][cw]
    dis2=bfs(b1h,b1w,b2h,b2w,v,path)
    return dis1+dis2 if dis1+dis2 < 11111 else 11111

def bfs(sh,sw,eh,ew,v,path):
    q = deque([(sh,sw,0)])
    v[sh][sw] = 1
    while q:
        h, w, cnt=q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<=n and 0<=nw<=m and not v[nh][nw]:
                q.append((nh,nw,cnt+1))
                v[nh][nw] = 1
                path[nh][nw] = (h,w)
                if nh == eh and nw == ew:
                    return cnt+1
    return 11111

n, m = map(int, input().rstrip().split())
a1h, a1w = map(int,input().rstrip().split())
a2h, a2w = map(int,input().rstrip().split())
b1h, b1w = map(int,input().rstrip().split())
b2h, b2w = map(int,input().rstrip().split())
ans = min(dstt(a1h, a1w, a2h, a2w, b1h, b1w, b2h, b2w), dstt(b1h, b1w, b2h, b2w, a1h, a1w, a2h, a2w), dstt(a2h, a2w, a1h, a1w, b2h, b2w, b1h, b1w), dstt(b2h, b2w, b1h, b1w, a2h, a2w, a1h, a1w))
print(ans if ans < 11111 else "IMPOSSIBLE")



'''
mov = [(-1,0),(0,1),(1,0),(0,-1)]

def bfs(f1, f2, s1,s2):
    global n, m, ans
    v = [[0]*(m+1) for _ in range(n+1)]
    a1h, a1w = f1
    a2h, a2w = f2
    if a1h > a2h:
        a1h, a2h = a2h, a1h
    if a1w > a2w:
        a1w, a2w = a2w, a1w
    for i in range(a1h, a2h+1):
        for j in range(a1w, a2w+1):
            v[i][j] = 1
    ret1 = abs(a1h-a2h)+abs(a1w-a2w)
    b1h, b1w = s1
    b2h, b2w = s2
    v[b1h][b1w] = 1
    # for i in v:
    #     print(i)
    # print(">>>>>>>1")
    q = deque([(b1h, b1w)])
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n+1 and 0<=nw<m+1 and not v[nh][nw]:
                if nh==b2h and nw==b2w:
                    # for i in v:
                    #     print(i)
                    # print(">>>>>>>2")
                    return ret1+v[h][w]
                v[nh][nw] = v[h][w]+1
                q.append((nh, nw))
    # for i in v:
    #     print(i)
    # print(">>>>>>>2")
    return 11111

n, m = map(int, input().rstrip().split())
a1, a2, b1, b2 = [list(map(int, input().rstrip().split())) for _ in range(4)]

ans = min(bfs(a1,a2,b1,b2), bfs(b1,b2,a1,a2))
print(ans if ans != 11111 else "IMPOSSIBLE")
'''















