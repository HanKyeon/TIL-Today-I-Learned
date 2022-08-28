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
from heapq import heappush
import sys
input = sys.stdin.readline


n, k = map(int, input().split()) # 보석의 총 갯수. 상덕이 가방 겟수
# bos, bag = [list(map(int, input().rstrip().split())) for _ in range(n)], [int(input().rstrip()) for _ in range(k)]
bos = []

for i in range(n): # 보석의 무게, 가치
    we, va = map(int, input().split())
    heappush(bos, (-va, we))
# for i in range(k): # 가방이 담을 수 있는 무게
#     mg = int(input())
bag = sorted([int(input().rstrip()) for _ in range(k)])

while bos and bag:
    








