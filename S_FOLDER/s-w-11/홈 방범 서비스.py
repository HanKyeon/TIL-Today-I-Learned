'''
홈 방범 서비스

마름모 영역만 제공.
마름모 영역이 클 수록 운영 비용 커진다. 면적과 동일.
비용은 k**2 + (k-1)**2
도시를 벗어나도 비용 변경x

집들은 M의 비용 지불 가능 손해 보지 않는 한 최대한 많은 집에 홈 방범 서비스 제공.
도시 N과 하나의 집 비용M
손해 보지 않으면서 홈 방범 서비스를 가장 많은 집들에 제공하는 서비스 영역을 찾고, 그 때의 홈 방범 서비스를 제공 받는 집들의 수 출력

입력
테케T
도시 크기, 집 지불 비용 M

출력
#테케 손해 최소화, 많은 집, 집 수.
'''
from collections import deque
from heapq import heappop, heappush

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

def bfs():
    global q, v, m, n
    hret = 0 # 최댓값일 때 집 갯수
    hc = 0
    v[q[1][0]][q[1][1]] = 1
    if g[q[1][0]][q[1][1]] == 1:
        hc += 1
    while q:
        qpl = q.popleft()
        if len(qpl) == 3:
            siz = qpl[0]
            q.append((siz+1, 0, 0))
            if siz >= 2*n+1:
                break
            if hc*m - coz[siz] < 0:
                continue
            if hret < hc:
                hret = hc
            continue

        h, w = qpl
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<n and v[nh][nw] == 0:
                v[nh][nw] = 1
                q.append((nh, nw))
                if g[nh][nw] == 1:
                    hc+=1
    return -hret



for testcase in range(1, int(input())+1):
    n, m = map(int, input().rstrip().split())
    g = [list(map(int, input().rstrip().split())) for _ in range(n)]
    coz = [k**2+(k-1)**2 for k in range(n*2+2)]
    heap = []
    for i in range(n):
        for j in range(n):
            v = [[0]*n for _ in range(n)]
            q = deque([(1, 0, 0), (i, j)])
            heappush(heap, bfs())
    hmz = heappop(heap)
    print(f"#{testcase} {-hmz}")










'''
        if len(qpl) == 3:
            siz = qpl[0]
            if siz >= 2*n:
                break
            if ret == hc*m - coz[siz]:
                hret = max(hret, hc)
                q.append((siz+1, 0, 0))
                continue
            elif ret < hc*m - coz[siz]:
                ret = hc*m - coz[siz]
                hret = hc
                q.append((siz+1, 0, 0))
                continue
            else:
                q.append((siz+1, 0, 0))
                continue
'''
















