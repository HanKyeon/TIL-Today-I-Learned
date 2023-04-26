'''
쇼핑몰

쇼핑을 마친 n명의 고객들이 계산대 앞에 서있음.
계산대는 k개가 병렬 배치.
두 계산대에서 기다려야 할 시간이 같다면 번호가 작은 계산대로 안내.
고객이 나갈 때는 출구에 가까운 높은 번호 고객 먼저 나간다.
물건 계산하는데 종류 상관 없이 1분. 물건이 w개라면 w분 소요.
들어가고 나오는 시간은 없다.

입력
2개 정수 n, k 제시.
n개 줄 고객 id, 물건 수 w 제시. 고객 id는 다 다름.

출력
n명의 회원번호를 쇼핑몰 빠져나가는 순서대로 r1 r2 r3라 할 때, 회원번호 * 순서.
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
gst = [list(map(int, input().rstrip().split())) for _ in range(n)]
gsd = []
for i in range(k):
    heappush(gsd, (0, i))
al = []
while gst:
    idz, wz = gst.pop(0)
    wks, i = heappop(gsd)
    heappush(gsd, (wks+wz, i))
    al.append((wks+wz, -i, idz))
al.sort()
ans = 0
for j in range(n):
    _, i, idz = al[j]
    ans += (j+1)*idz
print(ans)


import heapq
import sys

input = sys.stdin.readline
n, k = map(int, input().split())

cus = []
wz = []
for _ in range(n):
    customer, item_cnt = map(int, input().split())
    cus.append(customer)
    wz.append(item_cnt)

gsd = []
for i in range(k):
    heapq.heappush(gsd, (0, i))

tmz = [0] * k

finished = []
for i in range(n):
    t, idx = heapq.heappop(gsd)
    tmz[idx] += wz[i]
    heapq.heappush(gsd, (tmz[idx], idx))
    finished.append((tmz[idx], -idx, i))

print(sum(cus[t[2]] * (i+1) for i, t in enumerate(sorted(finished))))


