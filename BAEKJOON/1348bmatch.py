'''
주차장

r*c 크기 직사각형.
n개 차 m개 주차구역
. 빈 공간
X 벽
C 차
P 주차공간
모든 차가 주차하는데 걸리는 시간의 최솟값 계산.

입력
R, C 제시. 50이하.
R개 줄 주차장 정보 제시.
차, 주차구역 갯수는 0이상 100이하

출력
모든 차가 주차하는데 걸리는 시간의 최솟값. 차가 없다면 0 출력
'''
import sys
from collections import deque
input = sys.stdin.readline
# 거리 구하기
mov = [(-1,0),(0,1),(1,0),(0,-1)]
def bfs(sh, sw):
    global n, m, pc
    v = [[0]*m for _ in range(n)]
    dst = [3000] * pc
    v[sh][sw] = 1
    q = deque([(sh, sw)])
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and not v[nh][nw]:
                if g[nh][nw] == 0:
                    v[nh][nw] = v[h][w]+1
                    q.append((nh, nw))
                elif g[nh][nw] > 0:
                    v[nh][nw] = v[h][w]+1
                    dst[g[nh][nw]-1] = v[h][w]
                    q.append((nh, nw))
    return dst
# 이분 매칭 함수
def matching(cnum):
    global mid
    for idx, val in enumerate(dst[cnum]):
        if val > mid or v[idx]:
            continue
        v[idx] = 1
        if connect[idx] < 0 or matching(connect[idx]):
            connect[idx] = cnum
            return True
    return False
# 입력 및 그래프 설정
n, m = map(int, input().rstrip().split())
g = []
cars, pz = [], []
for i in range(n):
    s = list(input().rstrip())
    for j in range(m):
        if s[j] == '.':
            s[j] = 0
        elif s[j] == 'X':
            s[j] = -1
        elif s[j] == 'C':
            cars.append((i, j))
            s[j] = 0
        elif s[j] == 'P':
            pz.append((i, j))
            s[j] = len(pz)
    g.append(s)
cc, pc = len(cars), len(pz)
# 극단값들
if not cars:
    print(0)
    exit()
if cc > pc:
    print(-1)
    exit()
# 거리 구하기
dst = []
for h, w in cars:
    a = bfs(h, w)
    dst.append(a)
# 이분 탐색
ans = 1500
sta, end = 0, 1500
while sta <= end:
    mid = (sta+end) // 2
    # 이분 매칭
    connect = [-1] * pc # 공원idx에 차 idx가 들어감.
    for i in range(cc):
        v = [0]*pc
        a = matching(i)
        if not a:
            break
    else:
        ret = 0
        for p, c in enumerate(connect):
            if c < 0:
                continue
            dis = dst[c][p]
            if ret < dis:
                ret = dis
        if ret < ans:
            ans = ret
        end = mid-1
        continue
    sta = mid+1
# 갱신 안됐을 때 처리
if ans == 1500:
    ans = -1
print(ans)

'''
3 4
C..P
XXXX
C..P

3 5
CC..P
XXXXX
C..PP
'''



'''
# 시간초과 순열
for permu in permutations(range(len(pz)), len(cars)):
    ret = 0
    for i in range(len(cars)):
        a = permu[i]
        if ret < dst[i][a]:
            ret = dst[i][a]
    if ret < ans:
        ans = ret
if ans == 3000:
    ans = -1
print(ans)
'''



