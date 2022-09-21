'''
우체국

수직선에 n개의 마을.
i번째 마을은 x[i]에 있고 A[i]명의 사람이 살고 있다.
각 사람들 까지의 거리 합이 최소가 되는 위치에 우체국을 세우기로 결정. 우체국 세울 위치 작성.
각 마을까지 거리 합이 아니라 각 사람까지의 거리 합임을 유의하라.

입력
N 제시. 1이상 10만이하. X1 A1 / X2 A2 ... 이런 식으로 한다. 범위는 X[i]는 10억이하, A[i]는 10억이하. 모든 입력은 정수이다.

출력
우체국 위치 출력. 가능한 경우가 여러가지인 경우, **더 작은 위치 출력.**
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
pn = 0
heap = []
for _ in range(n):
    x, a = map(int, input().rstrip().split())
    heappush(heap, (x, a))
    pn+=a
pc = 0
pnh = pn//2+1 if pn%2 else pn//2
while heap:
    x, a = heappop(heap)
    pc += a
    if pc >= pnh:
        break
print(x)




'''
import sys
input = sys.stdin.readline

n = int(input())
vsm, psm = 0, 0
jp = []
for _ in range(n):
    x, a = map(int, input().rstrip().split())
    vsm += x*a
    psm += a
    jp.append(x)
bst = int(vsm/psm+0.5)
ans, chai = jp[0], abs(bst-jp[0])
for i in range(1, n):
    nchai = abs(bst-jp[i])
    if nchai > chai:
        continue
    elif nchai == chai:
        ans = min(ans, jp[i])
    else:
        chai = nchai
        ans = jp[i]

print(ans)

'''