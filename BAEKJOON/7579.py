'''
앱

현재 n개의 앱 a1 a2 an이 활성화 상태이다. 앱은 mi바이트 만큼 메모리 사용. 앱aiㅡㄹ 비활성화 한 후, 다시 실행하고자 할 때 추가적으로 들어가는 비용을 수치화 한 것을 ci라 고 하자.
사용자가 새로운 앱 b를 실행하고자 하여 추가 m바이트가 필요하다. 현재 활성화 되어 있는 앱 a1,...,an 중에서 몇개를 비활성화하여 m바이트 이상의 메모리를 추가 확보 해야한다. 그 중에서 비활성화 했을 경우 비용 ci의 합을 최소화 하여 필요한 메모리 m바이트를 확보하는 방법을 찾아야 한다.

입력
n, m 1이상 100이하n 1이상 천만이하m
a1 a2 앱이 사용중인 메모리 바이트 수 합쳐도 m이하.
앱을 비활성화 했을 때 비용 c1, c2.. 0이상 100이하
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
mz = list(map(int, input().rstrip().split())) # 지금 먹는 메모리
cz = list(map(int, input().rstrip().split())) # 비용
scz = sum(cz) # 자주 쓰길래 할당해줌

# ci 즉 비용을 가로로 두고 냅색을 수행했다. 각 비용 별 최대로 확보 가능한 메모리를 구한 뒤
dp = [0] * (scz+1)
ndp = [0] * (scz+1)

# 냅색 알고리즘. 나는 2차원 배열보다 배열 2개 쓰는게 편하더라.
while mz and cz: # 팝이 좋아
    ai, ci = mz.pop(), cz.pop() # 메모리, 비용
    for i in range(scz+1):
        if i+ci <= scz:
            ndp[i+ci] = max(dp[i]+ai, dp[i+ci]) # 수정되는 ndp는 수정되지 않은 dp를 기준으로 변경된다.
    dp = ndp[:]

# 낮은 비용에서 확보 가능한 메모리를 확인하며 처음 m을 넘으면 정답으로 정하고 출력.
for i in range(scz+1):
    if dp[i] >= m:
        ans = i
        break
print(ans)



'''
# 파이썬 시간초과
# 파이파이 메모리 초과
# 정답은 나옴. 1000만이라는 수를 간과함.
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
mz = list(map(int, input().rstrip().split()))
cz = list(map(int, input().rstrip().split()))

# 메모리를 가로축으로 냅색 알고리즘을 수행했다.
dp = [-1] * (m+1)
ndp = [-1] * (m+1)

while mz and cz:
    ai, ci = mz.pop(), cz.pop()
    for i in range(m+1):
        if i <= ai:
            if dp[i] == -1:
                ndp[i] = ci
            else:
                ndp[i] = min(dp[i], ci)
        if dp[i] == -1:
            continue
        if i+ai<=m:
            if dp[i+ai] == -1:
                ndp[i+ai] = dp[i]+ci
            else:
                ndp[i+ai] = min(dp[i]+ci, ndp[i+ai])
    dp = ndp[:]

print(dp[m])

'''

















