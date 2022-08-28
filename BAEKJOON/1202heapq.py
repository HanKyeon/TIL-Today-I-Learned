'''
보석 도둑

보석이 총 N개
보석은 무게 Mi와 가격 Vi
상덕이는 가방을 K개
각 가방에 담을 수 있는 최대 무게는 Ci
가방에는 최대 한 개의 보석만
상덕이가 훔칠 수 있는 보석의 최대 가격

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)
다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)
다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)

출력
상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값
'''

from heapq import heappop, heappush
import sys
input = sys.stdin.readline


n, k = map(int, input().split()) # 보석의 총 갯수. 상덕이 가방 겟수
# bos, bag = [list(map(int, input().rstrip().split())) for _ in range(n)], [int(input().rstrip()) for _ in range(k)]
bos = [] # 놀랍게도 bosuc 보석 한글로.

for i in range(n): # 보석의 무게, 가치
    we, va = map(int, input().rstrip().split())
    heappush(bos, (we, va))
# for i in range(k): # 가방이 담을 수 있는 무게
#     mg = int(input())
bag = sorted([int(input().rstrip()) for _ in range(k)])
ans = 0
avbos = [] # available bosuc
for i in bag:
    while bos and bos[0][0] <= i:
        we, val = heappop(bos) # 가방 무게보다 가벼운 보석들 전부 pop해서
        heappush(avbos, -val) # avail bos에 가치 순으로 넣어주기.
    
    if avbos: # 이후 최대 가치를 넣어준다.
        ans -= heappop(avbos)
    # 이후 다음 회전 때, 정렬된 bag를 순회하므로 다음 회전에도 available bosuc에 들어간 보석들은 담을 수 있다.
print(ans)


'''
시간초과
while bos and bag:
    vw = heappop(bos)
    for i in range(len(bag)):
        if bag[i] >= vw[1]:
            bag.pop(i)
            ans -= vw[0]
            break
'''