'''
두 용액

특성값. 산성은 1부터 10억, 알카리는 -1부터 -10억
두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.
산성과 알카리 특성 값이 주어졌을 때, 두 개의 용액을 혼합하여 특성 값이 0에 가장 가까운 용액을 만들어라.

입력
n 제시. 2이상 10만이하.
n개 정수 빈 칸 제시. -10억 to 10억 모든 용액의 특성값은 모두 다르다.

출력
두 용액의 출력값을 오름차순으로 출력 2개 이상일 경우 아무거나.
'''
import sys
input = sys.stdin.readline

def bs(idx):
    global n, hap, ans
    num1 = nl[idx]
    sta, end = idx+1, n-1
    ret, ihap = [], hap 
    while sta <= end:
        mid = (sta+end)//2
        num2 = nl[mid]
        if ihap > abs(num1+num2):
            ihap = abs(num1+num2)
            ret = [num1, num2]
        if num1+num2 < 0:
            sta = mid+1
        else:
            end = mid-1

    if ihap < hap:
        ans = ret
        hap = ihap
    return

n = int(input())
nl = list(map(int, input().rstrip().split()))
nl.sort()
hap, ans = 2000000001, []
for i in range(n-1):
    bs(i)
print(*ans)
'''
3
-10 1 2
'''
'''
# 빠른 코드

import sys

input = sys.stdin.read


def sol2470():
    n, *liq = map(int, input().split())
    liq.sort()
    if liq[0] >= 0:
        return ' '.join(map(str, [liq[0], liq[1]]))
    if liq[-1] <= 0:
        return ' '.join(map(str, [liq[-2], liq[-1]]))
    
    l, r = 0, n-1
    x, y, res = 0, 0, float('inf')
    while l < r:
        s = liq[l] + liq[r]
        if s == 0:
            x, y = l, r
            break
        if s < 0:
            if -s < res:
                x, y, res = l, r, -s
            l += 1
        else:
            if s < res:
                x, y, res = l, r, s
            r -= 1
            
            
    return ' '.join(map(str, [liq[x], liq[y]]))


if __name__ == '__main__':
    print(sol2470())
'''












