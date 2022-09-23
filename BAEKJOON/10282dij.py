'''
해킹

서로 의존하는 컴퓨터들은 감염. a가 b에 의존한다면 b가 감염된 뒤 일정 시간 후 a도 감염. 이 때 b가 a에 의존하지 않으면 a가 감염되도 b는 안전. 방향성.
해킹한 컴퓨터 번호와 의존성이 주어 질 때, 해킹 당한 컴퓨터까지 포함하여 몇개의 컴퓨터가 감염되며 그에 걸리는 시간이 얼마인지 구하시오.

입력
테케T 최대100
컴퓨터 갯수n 의존성 갯수d 해킹컴 번호 c. 1이상 1만이하 1이상10만이하 1이상n이하.
d개 줄에 의존성 a, b, s. a가 b에 의존하며 b가 감염되면 s초 후 컴a도 감염됨. 중복 없음.

출력
테케마다 한 줄에 감염되는 컴퓨터 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간을 공백으로 구분지어 출력.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dij(num):
    global n
    dst = [int(10e9)]*(n+1)
    dst[num] = 0
    heap = [(0, num)]
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        for co, nnod in g[nod]:
            if dst[nnod] > cost+co:
                dst[nnod] = cost+co
                heappush(heap, (cost+co, nnod))
    cnt = 0
    tm = 0
    for i in dst:
        if i == int(10e9):
            continue
        cnt += 1
        tm = max(tm, i)
    return cnt, tm

for tc in range(int(input())):
    n, m, sta = map(int, input().rstrip().split())
    g = [[]for _ in range(n+1)]
    for _ in range(m):
        a, b, s = map(int, input().rstrip().split())
        g[b].append((s, a))
    print(*dij(sta))



















