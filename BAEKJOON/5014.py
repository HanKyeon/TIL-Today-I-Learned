'''
스타트 링크

f층 건물. 목표 G층. 현재s층. 엘베는 2버튼. U는 위로 u만큼 d는 아래로 d만큼 간다.
g로 가려면 버튼을 적어도 몇 번 눌러야 하는지. 엘베로 못가면 use the stairs 출력

입력
f, s, g, u, d 제시

출력
s에서 g로 가기 위해 눌러야 하는 버튼의 수 최솟값 출력. 불가능 시 use the stairs 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

def memo():
    global f,s,g,u,d
    dp = [1111111]*(f+1)
    dp[s] = 0
    q = deque([s])
    while q:
        if dp[g] != 1111111:
            return dp[g]
        n = q.popleft()
        for i in [u, -d]:
            if 0<n+i<=f and dp[n+i] == 1111111:
                dp[n+i] = dp[n]+1
                q.append(n+i)
    return "use the stairs"

f, s, g, u, d = map(int, input().rstrip().split())
print(memo())
