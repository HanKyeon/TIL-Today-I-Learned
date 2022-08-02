'''
가장 긴 증가하는 부분 수열
'''
# 입력
n = int(input())
nl = list(map(int,input().split()))
# 필요한 테이블 만들기. 데이터 & 최대 판단 테이블
d = [0]
d.extend(nl)
dp = [0] * (n + 1)
# d[i] 이전까지만 순회 하면서 확인 현재 값보다 크다면 dp테이블에 1을 더해준 값 중 최댓값.
for i in range(len(d)) :
    for j in range(i) :
        if d[i] > d[j] :
            dp[i] = max(dp[i], dp[j]+1)
# 최대 수열 수 출력
print(max(dp))

'''
[0, 5, 6, 1, 2, 3]
[0, 1, 2, 1, 2, 3]
이전에 가장 많이 만들 수 있는 수열의 길이가 가진 값보다 현재 값이 크다면 +1
'''