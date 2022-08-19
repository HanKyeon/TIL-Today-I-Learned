'''
징검다리 건너기

N개의 돌이 일렬로 나열, 마지막 돌 틈 사이 산삼
다음 위치인 킹점프 
1돌 건너는 왕점프
2돌 건너는 짱점프
킹점프와 왕점프 시 에너지가 돌마다 다르다.
짱점프는 단 1회, 점프하는 돌 상관없이 k만큼 소모
산삼을 위한 에너지소비 최소화
첫돌부터 시작

입력
돌의 갯수N
n-1에 걸쳐 1번돌부터 N-1번돌까지 작은 점프에너지 / 큰점프에너지
마지막줄 k
'''

N = int(input())
kw = [list(map(int, input().split())) for _ in range(N - 1)]
Z = int(input())

if N == 1 :
    dp = [10e9] * N
    dp[0] = 0
    print(dp[-1])
elif N == 2 :
    dp = [10e9] * N
    dp[0] = 0
    dp[1] = dp[0] + kw[0][0]
    print(dp[-1])
elif N == 3 :
    dp = [10e9] * N
    dp[0] = 0
    dp[1] = dp[0] + kw[0][0]
    dp[2] = min(dp[2], dp[0] + kw[0][1], dp[1] + kw[1][0])
    print(dp[-1])
else :

    dp = [10e9] * N
    dp[0] = 0
    dp[1] = dp[0] + kw[0][0]
    dp[2] = min(dp[2], dp[0] + kw[0][1], dp[1] + kw[1][0])

    dpEnd = []

    for i in range(0, N-2) :
        dp[i+2] = min(kw[i][1] + dp[i], kw[i+1][0] + dp[i+1], dp[i+2])
    dpEnd.append(dp[-1])

    for u in range(0, N-3) :
        cp = dp[:]
        cp[u+3] = cp[u] + Z
        for i in range(0, N-2) :
            cp[i+2] = min(kw[i][1] + cp[i], kw[i+1][0] + cp[i+1], cp[i+2])
        dpEnd.append(cp[-1])

    print(min(dpEnd))


'''
def jump() :
    pass

N = int(input())
kw = [list(map(int, input().split())) for _ in range(N - 1)]
Z = int(input())
dp = [0] * N
dp[1] = dp[0] + kw[0][0]
# dp[2] = max(dp[0] + kw[0][1], dp[1] + kw[1][0])
dpEnd = []

for i in range(0, N-2) :
    dp[i+2] = min(kw[i][1] + dp[i], kw[i+1][0] + dp[i+1])
dpEnd.append(dp[-1])

sta = 0
end = 3
savmax = dp[3]-dp[0]
useZ = []

while end < N-1 :
    sta += 1
    end += 1
    if dp[end]-dp[sta] > Z :
        useZ.append(sta)

for u in useZ :
    cp = dp[:]
    cp[u+3] = cp[u] + Z
    if u < N-1-3 :
        cp[u+4] = min(cp[u+4], cp[u+3]+kw[u+3][0])
    # cp[u+4] = cp[u+3] + kw[u+3][0]
    for i in range(u+3, N-3) :
        cp[i+2] = min(kw[i][1] + cp[i], kw[i+1][0] + cp[i+1])
    dpEnd.append(cp[-1])

print(min(dpEnd))
'''
