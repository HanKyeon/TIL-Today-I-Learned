'''
극장 좌석

1~n번 번호 좌석. 자기 좌석에 앉아야 하는데 양옆으로는 이동 가능. VIP는 반드시 지 좌석에 앉음.
VIP 회원 좌석번호 제시, 사람들이 좌석에 앉는 서로 다른 방법의 갯수르 구하시오

입력
n 제시
m 제시
m개 줄 고정석 번호 제시

출력
사람드리 좌석에 앉을 수 있는 방법의 가짓수 출력
'''
n, m = int(input()), int(input())
nl = [int(input()) for _ in range(m)]
al = []
for i in range(m): al.append(nl[i] if not i else nl[i]-nl[i-1])
al.append(n+1-(nl[-1] if m else 0))

dp = [1,1,2,3,5,8]+[0]*35
for i in range(6, 41): dp[i] = dp[i-1]+dp[i-2]
ans = 1
for i in al: ans*=dp[i-1] # ; print(f"{i-1}명 자유라서 {dp[i]} 곱해서 ans는 {ans}")
print(ans)

'''
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
vip = [False] * (N+1)

for _ in range(M):
    vip[int(sys.stdin.readline())] = True

dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1

for i in range(2, N+1):
    # 만약 자리를 바꿀 수 없는 좌석이면
    if vip[i]: dp[i] = dp[i-1]
    elif vip[i-1]: dp[i] = dp[i-1]
    else:
        if vip[i-2]: dp[i] = dp[i-1]*2
        else: dp[i] = dp[i-1]+dp[i-2]
    
print(dp[-1])
'''