'''
등산

일전에 푼 등산 문제와 같은데 등산을 노드로 한다.

A. 지도에서 임의 지점을 골라 그 지점을 목표로 정한다. 집 혹은 고려대
B. 집에서 정한 목표에 도달 할 때까지는 항상 높이가 증가하는 방향으로만 이동해야 한다.
C. 정한 목표에 도달 이후 고려대로 갈 때는 높이가 감소하는 방향으로만 이동해야한다.
D. 거리 1을 움직일 때마다 D의 체력이 소모.
E. 정한 목표에 도달하면 높이 1 당 E의 성취감 획득. 즉, 높이가 h인 목표에선 h*E의 성취감.

등산의 가치를 얻은 성취감 - 소모한 체력으로 계산 할 것이다. 가치가 가장 높은 등산 경로 지정해주기.

입력
노드 갯수, 간선 갯수, 거리 비례 체력 소비량, 높이 비례 성취감 획득량 제시. n,m,d,e
n개 정수제시. i번째 지점 높이는 hi이다.
m개 줄 a, b, c 제시.
경로 여러개 가능. 집은 1번 고려대 n번. 주환이랑 고려대 높이 1 보장.

출력
최대 가치 값 출력. 음수 가능
답 없으면 Impossible 출력
'''
import sys
from heapq import heappop, heappush
from math import inf
input = sys.stdin.readline

def dijup():
    global n
    dst = [inf] * (n+1)
    dst[1] = 0
    heap = [(0, 1)]
    cnt = 0
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        cnt+=1
        if cnt == n:
            return dst
        for co, nnod in goup[nod]:
            if cost+co < dst[nnod]:
                dst[nnod] = cost+co
                heappush(heap, (cost+co, nnod))
    return dst

def dijdown():
    global n
    dst = [inf] * (n+1)
    dst[n] = 0
    heap = [(0, n)]
    cnt = 0
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        cnt+=1
        if cnt == n:
            return dst
        for co, nnod in goup[nod]:
            if cost+co < dst[nnod]:
                dst[nnod] = cost+co
                heappush(heap, (cost+co, nnod))
    return dst

n, m, d, e = map(int, input().rstrip().split())
hli = [0]+list(map(int, input().rstrip().split()))
goup = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    ha, hb = hli[a], hli[b]
    if ha > hb:
        goup[b].append((c, a))
    elif ha < hb:
        goup[a].append((c, b))

downdp = dijdown()
updp = dijup()
ans = -inf
for i in range(2, n):
    dwn, upp = downdp[i], updp[i]
    if dwn == inf or upp == inf:
        continue
    val = (hli[i])*e - (dwn+upp)*d
    ans = max(ans, val)

if ans == -inf:
    ans = 'Impossible'
print(ans)






'''
downdp = [inf]
updp = [inf]
for i in range(1, n+1):
    if i == 1 or i == n:
        downdp.append(inf)
        updp.append(inf)
        continue
    val = dijdown(i)
    if val == inf:
        downdp.append(inf)
        updp.append(inf)
        continue
    updp.append(dijup(i))









for i in range(1, n+1):
    if i == 1 or i == n:
        downdp.append(inf)
        updp.append(inf)
        continue
    val = dijdown(i)
    if val == inf:
        downdp.append(inf)
        updp.append(inf)
        continue
    downdp.append(val)
    updp.append(dijup(i))
print(updp)
print(downdp)

ans = inf
for i in range(2, n):
    dval = dijdown(i)
    if dval == inf:
        continue
    uval = dijup(i)
    if uval == inf:
        continue
    print(i, hli[i], dval+uval)
    ans = min((hli[i]-hli[1])*e-dval-uval, ans)

print(ans)
'''