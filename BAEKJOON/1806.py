'''
부분합

10000 이하 자연수로 이루어진 길이 N 수열 제시. 연속된 수의 부분합 중 S이상 되는 것 중 가장 짧은 것의 길이를 구하시오.

입력
첫째 줄에 10이상 10만이하 n, 0이상 1억이하 s 제시.
수열 제시. 각 원소는 1만 이하 자연수.

출력
구하고자 하는 최소의 길이 출력. 불가능하다면 0 출력
'''
import sys
input=sys.stdin.readline

n, m = map(int, input().rstrip().split())
nl = list(map(int, input().rstrip().split()))

sta, end = 0, 0
nsum = nl[0]
le = 1
ans = int(10e9)
while end < n and sta <= end:
    if nsum >= m:
        ans = min(ans, le)
        nsum -= nl[sta]
        sta += 1
        le -= 1
    elif nsum < m:
        end += 1
        if end == n:
            break
        nsum += nl[end]
        le += 1
    if ans == 1:
        break
if ans == int(10e9):
    ans = 0
print(ans)

