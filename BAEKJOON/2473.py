'''
세 용액

산성 용액 / 알칼리 용액. 각 용액에는 용액 특성 하나의 정수 제시.
산성 용액 특성은 1~10억 알카리는 -1~-10억
혼합물의 특성 값은 혼합에 사용된 각 용액의 특성 값의 합.
특성 값이 0에 가장 가까ㅜㅇㄴ 용액을 만들려 한다.
세 개를 혼합하여 특성 값이 0에 가장 가까운 용액을 만들어내는 세 용액을 찾아라.

입력
n 제시. 3이상 5000이하.
특성 값 n개 숫자 oneline 제시. -10억~10억사이
'''
import sys
input = sys.stdin.readline

def bs(std):
    '''
    투 포인터
    `@std` : 기준 값
    '''
    global n, ans, ali
    sta, end = std+1, n-1
    while sta < end:
        sv, mv, ev = nl[std], nl[sta], nl[end]
        pv = abs(sv+mv+ev)
        if pv < ans:
            ans = pv
            ali = [sv, mv, ev]
            if not pv:
                return True
        if sv+mv+ev > 0:
            end-=1
            continue
        sta+=1

n = int(input())
nl = list(map(int, input().rstrip().split()))
nl.sort()
ans = 3333333333
ali = []
for i in range(n-2):
    if bs(i):
        break
print(*ali)










