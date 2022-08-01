'''
가장 긴 증가하는 부분 수열
'''

n = int(input())
nl = list(map(int,input().split()))
d = [0]
d.extend(nl)
dp = [0] * (n + 1)
# dp[1] = 1

for i in range(len(d)) :
    for j in range(i) :
        if d[i] > d[j] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

'''
[0, 5, 6, 1, 2, 3]
[0, 1, 2, 1, 2, 3]
이전에 가장 많이 만들 수 있는 수열의 길이가 가진 값보다 현재 값이 크다면 +1
'''