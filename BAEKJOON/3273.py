'''
두수의 합

n개 서로다른 양정수 수열 1이상 100만이하
ai, aj쌍을 구해라. 두수의 합이 x인

입력
n 제시.
수열 제시
x 제시

출력
만족하는 쌍의 갯수 출력
'''
import sys
input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().rstrip().split()))
x = int(input())
nl.sort()

sta, end = 0, n-1
ans = 0
while sta < end:
    mid = nl[sta]+nl[end]
    if x == mid:
        ans+=1
        sta+=1
    elif x > mid:
        sta += 1
    else:
        end -= 1
print(ans)



# 128메가인데 100만 배열? 메모리 초과 아닐까? 반틈이니 50만배열이긴 하다.

'''
# 카운팅 방식 안되는듯?
cnt = [0]*(nl[-1]+1)
ans = 0
for i in nl:
    cnt[i] += 1
while nl:
    num = x - nl.pop(0)
    try:
        if cnt[num]:
            cnt[num] -= 1
            ans += 1
    except:
        pass
print(ans//2)
'''


