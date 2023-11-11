'''
떡 돌리기

떡 돌릴 것. 한 번에 하나씩만 들고갈 수 있음. m개 양방향 도로. x보다 먼 거리를 걷지 않음.
잠은 본인 집에서 자야해서 왕복할 수 없는 거리는 다음날에 감. n-1개의 이웃집 모두에게 떡을 돌리기 위해서는 최소 몇일이 필요한가
집은 0번부터 n-1번

입력
n, m, x, y 제시
m+1개줄 a,b,c 제시 도로 유일

출력
성현이집 y 이웃집에 모두 떡을 돌리기 위한 최소 일 수를 출력 방문 불가 시 -1
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
inf = sys.maxsize

def dij():
    global n, x, y
    dst = [inf]*n
    dst[y], heap = 0, [(0, y)]
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost:
            continue
        for co, nnod in g[nod]:
            if cost+co > x: continue
            if cost+co < dst[nnod]:
                dst[nnod] = cost+co
                heappush(heap, (cost+co, nnod))
    dst.sort()
    ret, stk = 1, 0
    for i in dst:
        if i*2>x: return -1
        if stk+2*i <= x: stk+=2*i; continue
        ret+=1; stk=2*i
    return ret

n, m, x, y = map(int, input().rstrip().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
    g[b].append((c, a))
print(dij())

