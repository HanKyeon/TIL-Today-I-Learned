'''
수들의 합 2

n개의 수로 된 수열. i부터 j까지 합이 m이 되는 경우의 수

입력
n, m 제시
배열 제시

출력
경우의 수 출력
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
nl = list(map(int, input().rstrip().split()))
ans = 0
hap, sta, end = nl[0], 0, 0
if hap == m:
    ans+=1
while end < n:
    if hap > m:
        hap -= nl[sta]
        sta+=1
    else:
        try:
            end+=1
            hap += nl[end]
        except:
            break
    if hap == m:
        ans += 1
print(ans)
