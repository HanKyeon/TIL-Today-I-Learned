'''
예산

정해진 총액 이하에서 가능한 최대의 예산.

모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정
없는 경우에는 특정한 정수 상한액을 계산하여 그 이상에는 모두 상한액을 배정.
상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정.
예를 들어 예산이 475이고 요청이 120 110 140 150일 경우 120 110 127 127 배정.

입력
지방의 갯수 N 3이상 10000이하
지방의 예산 요청이 빈 칸을 두고 제시. 1이상 10만 이하.
총예산 M N이상 10억 이하.

출력
배정된 예산들 중 최댓값인 정수.
'''
import sys
input = sys.stdin.readline

def 예산합(num):
    ret = 0
    for i in nl:
        if i <= num:
            ret+=i
        else:
            ret += num
    return ret

n = int(input())
nl = list(map(int, input().split()))
m = int(input())

sta, end = 0, max(nl)
ans = 0
while sta <= end:
    mid = (sta + end) // 2
    bud = 예산합(mid)
    if bud == m:
        ans = mid
        break
    elif bud > m:
        end = mid-1
    elif bud <= m:
        ans = mid
        sta = mid+1
print(ans)








