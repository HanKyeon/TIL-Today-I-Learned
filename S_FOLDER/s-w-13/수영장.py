'''
수영장

가장 적은 비용으로 수영장을 이용 할 수 있는 방법.

1일 이용권 : 1일 이용 가능
1달 이용권 : 1달 이용 가능. 매달 1일부터 시작.
3달 이용권 : 3달 이용 가능, 매달 1일부터 시작.
1년 이용권 : 1년 이용 가능. 매년 1월 1일 시작.

각 달의 이용 계획은 테이블 형태로 수립.
이용 계획에 나타나는 숫자는 해당 달에 수영장을 이용 할 날의 수.
각 이용권의 요금, 이용 계획 제시
최소 비용 수영장 사용 방법

문제
테케T
1일 요금 1달요금 3달요금 1년요금 제시.
1년 계획

출력
#테케 답
'''
from heapq import heappop, heappush

def 레쓰고(tc):
    d1, m1, m3, y1 = map(int, input().rstrip().split())
    mnth = [0] + list(map(int, input().rstrip().split()))
    heap = [(0, 0)]
    dp = [y1]*13
    dp[0] = 0
    while heap:
        cost, mth = heappop(heap)
        if mth == 12:
            break
        if dp[mth] < cost:
            continue
        co = min(mnth[mth+1]*d1, m1)
        if mth+1 <= 12 and dp[mth+1] > cost+co:
            dp[mth+1] = cost+co
            heappush(heap, (cost+co, mth+1))
        if mth+3<=12 and dp[mth+3] > cost+m3:
            dp[mth+3] = cost+m3
            heappush(heap, (cost+m3, mth+3))
    print(f"#{tc} {dp[-1]}")

for tc in range(1, int(input())+1):
    레쓰고(tc)










