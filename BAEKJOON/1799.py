'''
비숍

비숍을 놓을 수 없는 곳이 존재하며, 비숍이 서로가 서로를 잡을 수 없도록 두면 최대 몇개의 비숍을 놓을 수 있는가

입력
체스판 크기 10이하 자연수
그래프

출력
체스판 
'''

# set를 쓰지 않은 코드

import sys
input = sys.stdin.readline

def findml(idx):
    global n, ans, v

    # 백트래킹 종료조건. 여태 쌓여있는 v의 갯수가 일정 수를 넘어야 최댓값을 갱신 할 수 있으므로, 그 이하 종료한다.
    if sum(v) + 2*n-1 - idx <= ans:
        return

    # 일반 종료 조건. 마지막 인덱스까지 했으면 정답 갱신
    if idx == 2*n-1:
        ans = max(ans, sum(v))
        # print([i for i, v in enumerate(v) if v == 1])
        return
    if not bzr[idx]: # 대각선에 암것도 없으면 그냥 실행
        findml(idx+1)
    else: # 뭔가 있다면
        fla = False # 넣어서 돌렸는지 확인하는 용도
        for i in bzr[idx]:
            if v[i] == 1: # 이미 선택한 대각선이라면 다음 숫자 진행
                continue
            else: # 선택되지 않은 대각선 라인일 경우
                v[i] = 1 # 방문
                fla = True # 넣어서 돌아간 적 있다고 표시해주고
                findml(idx+1) # 함수 재귀
                v[i] = 0 # 방문 취소
        if not fla: # 넣어서 돌린 적이 없으면 빈 리스트나 마찬가지이므로 그냥 실행
            findml(idx+1)

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
bzr = [[] for _ in range(2*n-1)] # 빈자리
v = [0]*(2*n-1) # 방문 여부 확인
ans = 0
for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            bzr[i-j + n-1].append(i+j) # \방향에 그래프에 /대각선 정보 입력. 여기서 \방향 빼줘야 이따 편할듯
# print(bzr)
findml(0)
print(ans)


'''
# pass한 코드

import sys
input = sys.stdin.readline

def findml(idx, v):
    global n, ans

    # 백트래킹 종료조건. 여태 쌓여있는 v의 갯수가 일정 수를 넘어야 최댓값을 갱신 할 수 있으므로, 그 이하 종료한다.
    if len(v) + 2*n-1 - idx <= ans:
        return

    # 일반 종료 조건. 마지막 인덱스까지 했으면 정답 갱신
    if idx == 2*n-1:
        ans = max(ans, len(v))
        # print(v)
        return
    
    # 몸체
    if not bzr[idx]: # 대각선에 암것도 없으면 그냥 실행
        findml(idx+1, v)
    else: # 뭔가 있다면
        fla = False # 넣어서 돌렸는지 확인하는 용도
        for i in bzr[idx]:
            if i in v: # 이미 선택한 대각선이라면 다음 숫자 진행
                continue
            elif not i in v: # 선택되지 않은 대각선 라인일 경우
                v.add(i) # 세트에 넣고
                fla = True # 넣어서 돌아간 적 있다고 표시해주고
                # print(f"{idx}번째에서 {i}를 넣었다.")
                findml(idx+1, v) # 함수 재귀
                v.remove(i) # 담 반복을 위해 지워주기.
        if not fla: # 넣어서 돌린 적이 없으면 빈 리스트나 마찬가지이므로 그냥 실행
            findml(idx+1, v)

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
bzr = [[] for _ in range(2*n-1)] # 빈자리
v = [0]*(2*n-1) # 방문 여부 확인용도로 만들엇는데 왜 안썼지?
ans = 0
for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            bzr[i-j + n-1].append(i+j) # \방향에 그래프에 /대각선 정보 입력. 여기서 \방향 빼줘야 이따 편할듯
# print(bzr)
a = set()
findml(0, a)
print(ans)
'''

'''
# 시간초과

from itertools import combinations
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
bzr = [] # 빈자리
for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            bzr.append((i, j))
ans = 0
for i in range(2*n-2, 0, -1):
    for j in combinations(bzr, i):
        pdi, mdi = {}, {}
        fla = True
        for k in j:
            x, y = k
            a, b = pdi.get(x+y, 0), mdi.get(x-y, 0)
            if a == 0 and b == 0:
                pdi[x+y] = pdi.get(x+y, 0) + 1
                mdi[x-y] = mdi.get(x-y, 0) + 1
            else:
                fla = False
                break
        if fla:
            ans = i
            break
    if fla:
        ans = i
        break
print(ans)
'''

'''
# 미친듯이 빠른데 뭐지???


from sys import stdin


n = int(stdin.readline().rstrip())
board = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

def count_bishop_path(y, x):
    count = 0
    yy = [y - 1, y - 1, y + 1, y + 1]
    xx = [x - 1, x + 1, x + 1, x - 1]
    dy = (-1, -1, 1, 1)
    dx = (-1, 1, 1, -1)

    for i in range(4):
        while 0 <= yy[i] < n and 0 <= xx[i] < n:
            if board[yy[i]][xx[i]]:
                count += 1
            
            yy[i] += dy[i]
            xx[i] += dx[i]
    
    return count

def remove_bishop_path(y, x):
    yy = [y - 1, y - 1, y + 1, y + 1]
    xx = [x - 1, x + 1, x + 1, x - 1]
    dy = (-1, -1, 1, 1)
    dx = (-1, 1, 1, -1)

    for i in range(4):
        while 0 <= yy[i] < n and 0 <= xx[i] < n:
            board[yy[i]][xx[i]] = 0
            
            yy[i] += dy[i]
            xx[i] += dx[i]
    
    board[y][x] = 0


num_bishop = 0
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

for i in range(n//2 + n%2):
    while 1:
        min_bishop = [2*n, -1, -1]

        y, x = i, i
        for j in range(4):
            for k in range(n - 2*i - 1):
                if board[y][x] == 1:
                    count = count_bishop_path(y, x)
                    if count < min_bishop[0]:
                        min_bishop = [count, y, x]

                y += dy[j]
                x += dx[j]
        
        if min_bishop[0] >= 2*n:
            break

        remove_bishop_path(min_bishop[1], min_bishop[2])
        num_bishop += 1

print(num_bishop)
'''

'''
# 뭔가 짱 빠른 방식
import sys
input = sys.stdin.readline
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
size_  = 0
dp = [-1 for _ in range(2*N-1)]
chess = [(0,i) if i < N else (i -N + 1,N-1) for i in range(2*N - 1)] #각 노드별 시작점
def func(start:int,n:int, size :int) -> None:
    if 2*N - 2 < n:
        global size_
        size_ = max(size_,size)
        return
    x,y = chess[n][0], chess[n][1]
    cnt = 0
    while 0<=x < N and 0<=y <N:
        if matrix[x][y]: # 말 놓은 수 있음
            for i in range(start,n,2):
                if -1 < dp[i]: 
                    if abs(x - (chess[i][0] + dp[i])) == abs(y - (chess[i][1] - dp[i])):  
                        break
            else:
                dp[n] = cnt
                func(start,n+2,size+1)
                
        x += 1
        y -= 1
        cnt += 1
    dp[n] = -1
    func(start,n+2,size)
func(0,0,0)
size_1 = size_
size_ = 0
func(1,1,0)
print(size_1 + size_)
'''



'''
하드 테케

10
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1

9
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1

9
1 0 1 0 1 0 1 0 1
0 1 0 1 0 1 0 1 0
1 0 1 0 1 0 1 0 1
0 1 0 1 0 1 0 1 0
1 0 1 0 1 0 1 0 1
0 1 0 1 0 1 0 1 0
1 0 1 0 1 0 1 0 1
0 1 0 1 0 1 0 1 0
1 0 1 0 1 0 1 0 1
'''