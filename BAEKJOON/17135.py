'''
캐슬 디펜스

캐디는 몰려오는 애들 잡는거다.
격자판 맨 아래는 성.
성에서는 3궁수 배치 예정. 하나 칸에 최대 1궁수 가능.
턴마다 궁수는 적 하나 공격. 공격하는 적은 거리가 D 이하인 적 중에서 가장 가까운 적. 여럿일 경우 가장 왼쪽. 같은 적이 동시에 공격 받을 수 있다. 공격 받은 적은 게임에서 제외된다.
궁수 공격 이후, 적이 이동. 한 칸 아래로 이동하며, 성이 있는 칸으로 이동한 경우 게임에서 제외된다.
모든 적이 격자판에서 제외되면 게임 끝.
구수 배치 이후 게임 진행은 정해져 있다. 격자판 상태가 주어졌을 때, 궁수의 공격으로 제거 할 수 있는 적의 최대 수를 계산.

입력
n, m 행 열 궁수 공격거리제한 D 둘째 줄부터 N개의 줄에는 격자판의 상태 제시. 0은 빈칸, 1은 적이 있는 칸.
n, m은 3이상 15이하. D는 1이상 10이하.

출력
궁수 공격으로 제거 할 수 있는 적의 최대 수.
'''
from itertools import combinations
import sys
input = sys.stdin.readline

def check(h, w):
    val = int(10e9)
    ah, aw = -1, -1
    for i in q:
        dst = abs(h-i[0])+abs(w-i[1])
        if dst < val and dst <= d:
            ah, aw = i[0], i[1]
            val = dst
    if ah>=0 and aw>=0:
        return (ah, aw)
    return

def moves():
    nq = []
    for h, w in q:
        if (h, w) in atkd:
            continue
        if h+1<n:
            nq.append((h+1, w))
    return nq

n, m, d = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
heap = []
nbr = 0
rq = []
for j in range(m):
    for i in range(n):
        if g[i][j] == 1:
            rq.append((i, j))
combi = list(range(m))
ans = 0
for ac1, ac2, ac3 in combinations(combi, 3): # 궁수 좌표는 ac1, n ac2, n ac3, n
    cnt = 0
    q = rq[:]
    while q:
        atkd = {check(n, ac1), check(n, ac2), check(n, ac3)}
        while None in atkd:
            atkd.remove(None)
        q = moves()
        cnt += len(atkd)
    ans = max(ans, cnt)
print(ans)























