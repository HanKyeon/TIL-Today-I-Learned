'''
연속합
'''
import sys
# 입력
n = int(input())
nl = sys.stdin.readline().rstrip()
nl = list(map(int, nl.split()))

dt = [-1001] * n
dt[0] = nl[0]

for i in range(1, n) :
    dt[i] = max(dt[i-1] + nl[i], nl[i])

print(max(dt))

# DP를 내가 생각한대로 해도 되지만
# 잘 생각해보면 앞에까지의 합이 음수가 아니라면 더하는 것이 무조건 이득이다.
# 즉, 앞까지의 합이 음수일 경우, 다음 숫자부터 합을 시행하면 최댓값이 된다.

'''
dt = [[-1001] * n for _ in range(n)]
# 테이블로 작성. 각 인덱스 시작부터 모든 값의 합 기록
for i in range(n) :
    if nl[i] >= 0:
        for j in range(i, n) :
            # j+1이다. 슬라이싱도 이상 미만이므로.
            dt[i][j] = sum(nl[i:j+1])
    else :
        dt[i][0] = nl[i]
# 최댓값 찾아서 반환
maxval = -1001
for a in dt :
    maxval = max(maxval, max(a))
# 출력
print(maxval)
'''