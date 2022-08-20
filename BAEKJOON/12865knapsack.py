'''
평범한 배낭

배낭에 최대한 가치 있게 넣고 싶다.
무게 W와 가치 V
물건을 가져가면 B만큼 즐긴다.
최대 무게 K

입력
물품의 수 N 1이상 100이하
버틸 수 있는 무게 1이상 10만 이하
N개줄에 걸쳐 W V 제시. 1이상 10만 이하 W, 0이상 1000이하 V 정수

출력
배낭에 넣을 수 있는 물건들의 가치합의 최댓값 출력
'''




'''
# pypy3 통과
n, k = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n)] # dp. 가로가 무게, 세로가 물건들

dp[0][wv[0][0]:] = [wv[0][1]] * (k+1-wv[0][0]) # 첫물건 초기화

for i in range(1, n): # 첫물건 이후 물건들을 훑으면서
    nst = wv[i] # 이번에 꺼낸 물건
    if nst[0] <= k: # 그 물건의 무게가 허용 가능하면 그 위치에 val을 넣어준다.
        dp[i][nst[0]] = max(dp[i-1][nst[0]], nst[1]) # 이전에 넣은 가치와 더 가치 높은지 비교해서.

    for j in range(1, k+1): # 무게들을 훑으면서
        # 두 번째 물건의 무게 j 지점에서는 바로 이전 가치, 이전 물건이 보유한 가치, 업뎃된 가치 등을 비교
        # 간단히 말해서 i,j 기준으로 i-1,j i-1,j-1 i,j-1을 비교해서 큰 값.
        dp[i][j] = max(dp[i][j], dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        
        if j + nst[0] <= k: # 현재 무게 물건을 더한 값이 최대 무게 범위 안쪽이면
            # 원래 그 위치가 가진 val
            # j위치가 가진 val에 현재 물건의 val을 더한 값
            # 그 위치의 이전 가치 / 이전 가치의 -1무게와 비교해서 큰 값을 넣어준다.
            dp[i][j+nst[0]] = max(dp[i-1][j+nst[0]], dp[i-1][j+nst[0]-1], dp[i-1][j]+nst[1], dp[i][j+nst[0]])
print(max(dp[-1])) # 마지막 물건까지 확인 했을 때의 최댓값을 넣어줌.
'''
'''
# 될 줄 알았는데... 최댓값만 기록하다보니
# 아래쪽 지점이 최댓값이 아닐 때 무게가 추가될 수 있다는 점을 잊은듯?
# 이렇게 하면 이전 부분에 대한 기록이 사라져서
# 물건이 중복된다! 알고리즘 만드는 사람들은 진짜 천재다!
n, k = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (k+1)

for i in wv:
    sw, sv = i[0], i[1]
    for j in range(k+1):
        if 0 <= j+sw <= k:
            dp[j+sw] = max(dp[j+sw], dp[j]+sv, dp[j+sw-1]) 
print(dp)
'''



# -----------
# 냅색 문제 풀이
# -----------
'''
import sys

N, K = map(int, input().split())
stuff = [[0,0]] # 물건 데이터 들어갈 것임.
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)] #dp

for _ in range(N):
    stuff.append(list(map(int, input().split())))

#냅색 문제 풀이
for i in range(1, N + 1): # 어차피 첫 물건은 0,0 이니까~
    for j in range(1, K + 1): # 동문
        weight = stuff[i][0] # 무게 추출
        value = stuff[i][1] # 가치 추출

        if j < weight: # 만약 j가 무게보다 작다면
            knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else: # j가 무게보다 크다면 해당 위치의 값은 
            # 이전 물건의 j-weight 상태의 가치에 물건 가치를 더한 것과
            # 그냥 이전 그 무게에 가진 가치 중에서 큰 걸로 설정한다.
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])
# 결국 n, k가 최댓값이 될거다.
print(knapsack[N][K])
'''










'''
비트연산 부분집합 : 시간초과


mv = 0
for i in range(2**n):
    ws, vs = 0, 0
    for j in range(n):
        if i & (1<<j):
            ws += wv[j][0]
            vs += wv[j][1]
    if ws <= k and mv < vs:
        mv = vs
print(mv)
'''

