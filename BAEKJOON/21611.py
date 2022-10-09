'''
마법사 상어와 블리자드

블리자드 연습. n*n 격자.
N은 항상 홀 수 r,c는 r행 c열. 좌상단 1,1 0,0 우하단 n,n n-1,n-1 애기상어는 n//2 n//2에 존재. 중앙에.
칸의 벽은 달팽이 모양.
상어 있는 칸 말고 구슬 하나 존재 가능. 같은 번호를 가진 구슬이 번호가 연속하는 칸에 있으면 그 구슬은 연속하는 구슬이다.

블리자드 마법은 방향 di와 거리 si를 정해야 한다. 방향은 상1하2좌3우4로 나타낸다. 해당 방향으로 상어는 그 칸에 있는 구슬을 파괴한다. 구슬이 파괴되면 구슬이 상어쪽으로 이동.

구슬이 4개 이상 연속하면 폭발된다.
폭발된 뒤 구슬이 다시 이동한다.
폭발된다.
이동한다.
반복한다.
폭발될 구슬이 없으면 멈춘다.

붙어있는 구슬은 하나의 그룹이다. 하나의 그룹은 구슬 A와 B로 변한다. A의 번호는 그룹에 들어있는 구슬의 갯수, B는 그룹을 이루고 있는 구슬의 번호.
구슬은 다시 그룹의 순서대로 1번 만부커 A,B의 순서로 칸에 들어간다. 구슬이 칸 수보다 많아 못들어가면 파괴된다.

블리자드를 m번 시전했다. 시전한 마법 정보가 주어졌을 때, 폭발한 1번 구슬 갯수*1 폭발한 2번 갯수*2 폭발한 3번갯수*3 값을 구해라.

입력
n, m 제시.
그래프 제시
m개 줄 di, si 제시.

출력
폭발한 1번 구슬 갯수*1 폭발한 2번 갯수*2 폭발한 3번갯수*3
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
sys.setrecursionlimit(2500)
# 상하좌우
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]
# 좌 하 우 상
cdi = {2:1, 1:3, 3:0, 0:2}
# 세팅 함수 : 회전 회오리 일렬로 담아줌.
def setting(h, w, di):
    if g[h][w] == 0:
        return
    gli.append(g[h][w])
    v[h][w] = 1
    ndi = cdi[di]
    nh, nw = h+dh[ndi], w+dw[ndi]
    if 0<=nh<n and 0<=nw<n and not v[nh][nw]:
        setting(nh, nw, ndi)
    elif 0<=nh<n and 0<=nw<n and v[nh][nw]:
        setting(h+dh[di], w+dw[di], di)
# 블리자드 시전
def blizard(di, si):
    for i in range(si):
        if len(gli) > blizdic[di][i]-i:
            gli.pop(blizdic[di][i]-i)
# 폭발 시키기
def explode():
    global ans, gli
    if len(gli) < 4:
        return False
    fla = False
    sta, end = 1, 2
    cnt, val = 1, gli[1]
    heap = []
    while end < len(gli):
        if gli[end] == val:
            cnt+=1
        else:
            if cnt >= 4:
                heappush(heap, (-sta, cnt))
            sta = end
            cnt = 1
            val = gli[sta]
        end += 1
    if cnt >= 4:
        heappush(heap, (-sta, cnt))
    if heap:
        fla = True
    while heap:
        idx, cnt = heappop(heap)
        idx *= -1
        ans += gli[idx] * cnt
        while cnt:
            cnt -= 1
            gli.pop(idx)
    return fla

def splitballs():
    global gli
    if len(gli) == 2:
        gli = [int(10e9), 1, gli[1]]
        return
    if len(gli) == 1:
        return
    sta, end, val, cnt = 1, 2, gli[1], 1
    heap = []
    while end < len(gli):
        if gli[end] == val:
            cnt+=1
        else:
            heappush(heap, (sta, cnt, val))
            sta = end
            cnt = 1
            val = gli[sta]
        end += 1
    heappush(heap, (sta, cnt, val))
    gli = [int(10e9)]
    while heap and len(gli) < n**2:
        idx, cnt, val = heappop(heap)
        gli.append(cnt)
        gli.append(val)

n, m = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
v = [[0]*n for _ in range(n)]
hn = n//2
g[hn][hn] = int(10e9)
gli = []
setting(hn, hn, 0)
# 부술 칸 인덱스 모음
blizdic = {1:[7]*hn, 2:[3]*hn, 3:[1]*hn, 4:[5]*hn}
for i in blizdic:
    for j in range(1, hn):
        blizdic[i][j] = blizdic[i][j-1] + blizdic[i][0] + 8*j
ans = 0
for _ in range(m):
    di, si = map(int, input().rstrip().split())
    # 블리자드 시전
    blizard(di, si)
    # 폭발
    a = explode()
    while a:
        a = explode()
    splitballs()
print(ans)






# 상하좌우 1,2,3,4
# 상 0 7 22 45 76 115
#      7 15 23 31 39
# 하 0 3 14 33 60 95
#      3 11 19 27 35
# 좌 0 1 10 27 52 85
#      1  9 17 25 33
# 우 0 5 18 39 68 105
#      5 13 21 29 37

