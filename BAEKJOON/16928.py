'''
뱀과 사다리 게임

정육면체 주사위. 1~6.
크기 10*10 보드판 진행. 1~100 적힘.
주사위를 굴려서 나온 수만큼 이동.
주사위를 굴린 칸의 결과가 100번 칸을 넘어가면 이동 금지.
도착한 칸이 사다리면 사다리를 타고 위로 이동.
뱀이 있는 칸에 도착하면 뱀을 따라서 내려감.
사다리를 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 크고, 뱀을 이용해 이동한 칸의 번호는 원래 칸보다 작다.
게임의 목표는 1번 칸에서 시작해서 100번 칸에 도착하는 것.
게임판의 상태가 주어졌을 때, 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값.

입력
게임판에 있는 사다리 수 n, 뱀의 수 m. 각 1이상 15이하
N개 줄에는 사다리 정보 x, y. x번 칸에 도착 시 y번칸으로 이동.
m개 줄에는 뱀 정보 u, v. u번 칸에 도착하면 v번 칸으로 이동.
1번칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아니다. 모든 칸은 최대 하나의 사다리 또는 뱀 보유. 두가지 동시보유x
항상 100번 칸에 도착 할 수 있는 입력 제시.

출력
100번 칸에 도착하기 위해 주사위를 최소 몇 번 굴려야 하는지 출력
'''
# BFS
from collections import deque
import sys
input = sys.stdin.readline

def bfs(idx):
    q = deque() # 큐
    q.append((idx, 0)) # 큐, 카운트
    while q:
        sta, c = q.popleft()
        if sta == 100: # 도착점이면
            return c # c 리턴
        for i in range(1, 7): # 1부터 6까지 더해주는데
            ns = sta+i
            if 1 <= ns <= 100: # 범위 안일 때만
                if sdr[ns] != 0: # 근데 사다리면 이동
                    ns = sdr[ns]
                if snk[ns] != 0: # 뱀이면 이동
                    ns = snk[ns]
                if v[ns] > c+1: # 방문처리. 새로 들어가는게 기존 값보다 작을 경우 갱신한다.
                    v[ns] = c+1
                    q.append((ns, c+1)) # 그 좌표 추가

n, m = map(int, input().rstrip().split())
sdr, snk = [0]*101, [0]*101
for i in range(n): # 사다리 정보 추가
    sta, end = map(int, input().rstrip().split())
    sdr[sta] = end
for i in range(m): # 뱀 칸 정보 추가
    sta, end = map(int, input().rstrip().split())
    snk[sta] = end
v = [int(10e9)]*101
print(bfs(1)) # bfs 실행

'''
# DP
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
sdr, snk = [0]*101, [0]*101
for i in range(n): # 사다리 정보 추가
    sta, end = map(int, input().rstrip().split())
    sdr[sta] = end
for i in range(m): # 뱀 칸 정보 추가
    sta, end = map(int, input().rstrip().split())
    snk[sta] = end
dp = [0, 0]+[10e9]*99 # dp. 1번 칸에서 시작하므로 1번칸까지 0으로 초기화
i = 1 # 시작 지점
while i < 101:
    for j in range(1, 7):
        if 0<=i-j<101 and snk[i-j] == 0: # 시작 점이 뱀으로 내려가는 칸이라면 갱신이 불가능하므로 뒤의 조건이 달림.
            dp[i] = min(dp[i-j]+1, dp[i]) # 현재 값과 이동 전 값+1 비교해서 작은 값
    if snk[i] != 0: # 뱀 길이라면
        b = dp[snk[i]] # 저장 할 값
        dp[snk[i]] = min(dp[snk[i]], dp[i]) # 뱀 도착지 카운트 변경
        if dp[snk[i]] != b: # 기존 값과 달라지면
            i = snk[i] # i를 이동시키고 반복 재진행
            continue
    if sdr[i] != 0: # 사다리가 있다면
        dp[sdr[i]] = min(dp[sdr[i]], dp[i]) # 도착지 정보 바꾸고
        dp[i] = int(10e9) # 사다리 지점 못가게 막음
    i+=1 # 정상 진행
print(dp[-1]) # 최종값
'''
'''
DP로 풀 때 예외
1 1
2 88
94 3
-> 88로 와서 6칸 이동해서 94로 갈 수가 없다! 이 점을 캐치해야 한다.
'''


'''
import sys 
from collections import deque
input = sys.stdin.readline 

N, M = map(int, input().split())

ladder = []
snake  = []

for _ in range(N):
    ladder.append(list(map(int, input().split())))

for _ in range(M):
    snake.append(list(map(int, input().split())))
    
visited = [False for _ in range(101)]
visited[1] = True
q = deque([[0, 1]])

while q:
    t, cur = q.popleft()
    
    for lad in ladder:
        if cur == lad[0]:
            cur = lad[1]
            
    for sna in snake:
        if cur == sna[0]:
            cur = sna[1]
            
    if cur == 100:
        print(t)
        break
    
    for i in range(1, 7):
        if cur + i <= 100 and not visited[cur + i]:
            q.append([t+1, cur + i])
            visited[cur + i] = True 
'''




