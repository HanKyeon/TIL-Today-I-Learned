'''
택배

그리디.
우측으로 진행하며 작은 마을에 내리고 받고 해서 최대로 배송이 가능한 갯수는?

입력
마을수 n, 용량c 2이상 2000이하 정수/ 1이상 10000이하 정수
보내는 박스의 정보 m 1이상 10000이하
보내는 마을번호, 받는 마을 번호, 박스 갯수를 나타내는 양의 정수가 빈 칸을 사이에 두고 제시.
박스를 받는 마을 번호는 보내는 마을 번호보다 크다.

출력
트럭 한 대로 배송 할 수 있는 최대 박스 수를 한 줄에 출력
'''

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, sto = map(int, input().split())
m = int(input())
cc = [0] * (n+2)
heap = []
for _ in range(m):
    sta, end, val = map(int, input().rstrip().split())
    heappush(heap, (end-sta, end, sta, val))
print('========')
while heap:
    chai, end, sta, val = heappop(heap)
    print(sta, end, val)
    mval = max(cc[sta:end])
    print(mval)
    if val > sto:
        val = sto
    if val-mval > 0:
        cc[end] += sto-(val-mval)
    print(cc)

print(sum(cc))




'''
import sys
input = sys.stdin.readline

n, sto = map(int, input().split())
m = int(input())
g = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: [x[1]])
box = [sto]*(n+1) # 트럭이 실을 수 있는 용량
cc = [0]*(n+1) # 받는 박스 수
for i in range(m):
    sta, end, val = g[i]
    tak = min(val, min(box[sta:end]))
    # print(tak)
    # print(box)
    for j in range(sta, end):
        box[j] -= tak
    cc[end] += tak
print(sum(cc))
'''













