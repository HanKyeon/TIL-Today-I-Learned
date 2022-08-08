'''
수열

연속적인 k일간 온도합이 가장 큰 값
지렁이합 쓰면 될듯? 아니, 나 이거 풀었었는데

입력
N과 K가 공백을 사이에 두고 제시. 2이상 10만이하, 1과 N사이 정수
측정한 온도 N개가 공백으로 -100~100사이 제시

출력
연속적인 K일의 온도합이 최대가 되는 값
'''

import sys
# 입력
n, k = map(int, input().split())
nl = list(map(int, sys.stdin.readline().split()))
sta = 0
end = k
maxtemp = sum(nl[sta:end])
newtemp = maxtemp
# 새 실행
while end < n :
    newtemp = newtemp - nl[sta] + nl[end]
    sta += 1
    end += 1
    maxtemp = max(maxtemp, newtemp)
print(maxtemp)

'''
import sys
# 입력
n, k = map(int, input().split())
nl = list(map(int, sys.stdin.readline().split()))
mintemp = -100 * k
mtl = [mintemp] * n
mtl[0] = sum(nl[:k])
# 실행
for i in range(1, n - k + 1) :
    mtl[i] = mtl[i-1] + nl[i+k-1] - nl[i-1]
# 출력
print(max(mtl))
'''

