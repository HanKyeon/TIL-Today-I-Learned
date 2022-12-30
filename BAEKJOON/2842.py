'''
집배원 한상덕

n*n 마을.
P 우체국
K 집
. 목초지
상덕이는 모든 집에 우편을 배달해야 한다. 배달은 하나밖에 없는 우체국 P 위치에서 시작.
수평, 수직, 대각 이동 가능. 편지 배달 이후 다시 우체국으로 돌아와야 한다.
상덕이가 배달하면서 방문한 칸 중 가장 높은 곳과 낮은 곳의 고도 차이를 피로도. 가장 작은 피로도로 모든 집에 배달을 하려면 어떻게 해야하는지 구해라.

입력
n 제시. 2이상 50이하
n개 줄 마을을 나타내는 행렬 제시. P는 한 번만 제시, K는 적어도 한 번 제시.
N개 줄 행렬로 나눠진 지역의 고도 행렬 형태 제시. 100만 이하 자연수

출력
가장 작은 피로도 출력.
'''
import sys
input = sys.stdin.readline
from collections import deque

mov = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

def bfs(mini, maxi):
    global n, hcnt, sh, sw
    if not mini<=hg[sh][sw]<=maxi:
        return False
    ret = 0
    h, w = sh, sw
    v = [[0]*n for _ in range(n)]
    v[h][w] = 1
    q = deque([(h, w)])
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<n and mini<=hg[nh][nw]<=maxi and not v[nh][nw]:
                v[nh][nw] = 1
                q.append((nh, nw))
                if g[nh][nw]:
                    ret += 1
                    if ret == hcnt:
                        return True
    return False

n = int(input())
g = []
hcnt = 0
for i in range(n):
    s = list(input().rstrip())
    for j in range(n):
        if s[j] == '.':
            s[j] = 0
        elif s[j] == 'K':
            hcnt += 1
            s[j] = hcnt
        elif s[j] == 'P':
            s[j] = 0
            sh, sw = i, j
    g.append(s)

hg = [list(map(int, input().rstrip().split())) for _ in range(n)]
hli = set()
for i in hg:
    for j in i:
        hli.add(j)
hli = list(sorted(hli))
stan = hg[sh][sw]
sta, end = 0, 0
ans = int(10e9)
while sta < len(hli):
    sth, enh = hli[sta], hli[end]
    if bfs(sth, enh):
        sta += 1
        if enh - sth < ans:
            ans = enh-sth
    else:
        if end < len(hli)-1:
            end += 1
        else:
            break

print(ans)


'''
# 빠른 코드
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
Graph = []; Height = []
for _ in range(N):
    Graph.append(list(input().rstrip()))
for _ in range(N):
    Height.append(list(map(int, input().rstrip().split())))

Post = None; House = 0
#우체국(P) 위치 찾기
for i in range(N):
    for j in range(N):
        if Graph[i][j] == 'P':
            Post = (i, j)
            C = Height[i][j]
        elif Graph[i][j] == 'K':
            House += 1

#Parameteric Search
def BFS(LB, UB):
    Q = deque(); Q.append(Post)
    Visit = [[False]*N for _ in range(N)]
    Visit[Q[0][0]][Q[0][1]]=True
    CNT = 0

    while Q:
        nR, nC = Q.popleft()
        dR = [-1,-1,-1,0,0,1,1,1]
        dC = [-1,0,1,-1,1,-1,0,1]

        for i in range(8):
            NR = nR + dR[i]; NC = nC + dC[i]
            if NR<0 or NC<0: continue
            elif NR>=N or NC>=N: continue
            elif Height[NR][NC]<LB: continue
            elif Height[NR][NC]>UB: continue
            elif Visit[NR][NC]: continue

            elif Graph[NR][NC]=='.':
                Q.append((NR, NC))
                Visit[NR][NC]=True
            elif Graph[NR][NC]=='K':
                Q.append((NR, NC))
                Visit[NR][NC]=True
                CNT += 1
    if House == CNT: return True
    else: return False

#Two Pointer
L = 1; R = C; ANS = 1000000
while L<C+1:
    Flag = BFS(L, R)   
    if not Flag: #[L, R]로 불가능
        #가능할 때까지 R 밀기(Binary Search)
        S = R; E = 1000001
        while S+1<E:
            MID = (S+E)//2
            if BFS(L, MID): E = MID
            else:
                S = MID
        R = E
        if S==1000000: break
        if R-L<ANS: ANS = R-L #답 갱신

    else: #[L, R]로 가능
        #불가능할 때까지 L 밀기(Binary Search)
        S = L; E = C+1
        while S+1<E:
            MID = (S+E)//2
            if BFS(MID, R): S = MID
            else: E = MID
        L = S
        if R-L<ANS: ANS = R-L
        L += 1

print(ANS)
'''


'''
# 시간 초과

import sys
input = sys.stdin.readline
from collections import deque

mov = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

def bfs(mini, maxi):
    global n
    h, w = homz[0]
    v = [[0]*n for _ in range(n)]
    v[h][w] = 1
    q = deque([(h, w)])
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<n and mini<=hg[nh][nw]<=maxi and not v[nh][nw]:
                v[nh][nw] = 1
                q.append((nh, nw))
    for h, w in homz:
        if v[h][w]:
            continue
        return False
    return True

n = int(input())
g = []
hcnt = 0
homz = []
for i in range(n):
    s = list(input().rstrip())
    for j in range(n):
        if s[j] == '.':
            s[j] = -1
        elif s[j] == 'K':
            hcnt += 1
            s[j] = hcnt
            homz.append((i, j))
        elif s[j] == 'P':
            s[j] = 0
            homz.insert(0, (i, j))
            sh, sw = i, j
    g.append(s)

hg = [list(map(int, input().rstrip().split())) for _ in range(n)]
stan = hg[sh][sw]
sta, end = 0, max(map(max, hg))
ans = int(10e9)
while sta <= end:
    mid = (sta+end) // 2
    fla = False
    for i in range(mid):
        if bfs(stan-i, stan+mid-i):
            fla = True
            break
    if sta == end:
        if bfs(stan, stan):
            fla = True
    if fla:
        ans = mid
        end = mid-1
    else:
        sta = mid+1
print(ans)
'''








