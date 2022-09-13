'''
으른 상어

1번 상어가 최강
n n 격자. m개 상어 자기 위치에 냄새 뿌리기.
1초마다 동시에 상하좌우 인접한 칸 중 하나로 이동, 자기 냄새 뿌리기. 냄새는 상어가 k번 이동하면 사라진다.
각 상어가 이동 방향을 결정 할 때는 인접한 칸 중 아무 냄새가 없는 칸의 방향으로. 그런 칸이 없다면, 자신의 냄새가 있는 칸으로. 이 때 가능한 칸이 여러개일 경우 특정 우선순위를 따른다. 상어마다 다를 수 있고, 같은 상어라도 보고 있는 방향에 따라 다를 수 있다. 상어가 처음 보고 있는 방향은 제시되고, 그 후에는 이동한 방향이 보고 있는 방향.
모든 상어가 이동한 뒤 여러 마리의 상어가 한 칸에 잇다면 가장 작은 번호를 가진 상어를 제외하고 죽는다.
냄새 뿌리고 죽을 시 냄새 시간만큼 남아있음.

입력
N, M, K 제시 2이상 20이하n, 2이상 n**2 이하 m, 1이상 1000이하 k
격자 제시. 0은 빈 칸, 0이아닌 수는 상어.
상어 방향 제시. 1,2,3,4는 상하좌우
상어의 방향 우선순위 상어 당 4줄 제시. 각 줄은 4개의 수. 상 하 좌 우 우선순위 제시.
첨부터 이동 못하는 경우 x

출력
1번 상어만 격자에 남게 되기까지 걸리는 시간 출력. 1000초가 넘어가도 다른 상어가 남아있다면 -1 출력
'''
from collections import deque
import sys
input = sys.stdin.readline
# 사방이동
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

n, m, k = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
sws = [[] for _ in range(m)] # 상어 방향 우선 순위
shadi = list(map(int, input().rstrip().split()))
for i in range(m):
    for j in range(4):
        d1, d2, d3, d4 = map(int, input().rstrip().split())
        sws[i].append([d1-1, d2-1, d3-1, d4-1])

# for i in g:
#     print(*i)
# print(shadi)
# for i in sws:
#     print(*i)

# 큐에는 방구들만 넣고 상어 위치, 방향 관리는 sha로 관리.
# shadi 는 상어의 방향.

sha = [[] for _ in range(m)] # 상어 본체의 위치
alive = set(range(m))
q = deque()
for i in range(n):
    for j in range(n):
        if g[i][j] == 0:
            g[i][j] = [-1, 0]
            continue
        a = g[i][j]-1
        sha[a] = [i, j, shadi[a]-1]
        q.append((i, j, a, k)) # i, j에 a 상어의 체취가 4초간 지속된다.
        g[i][j] = [a, k] # a상어의 체취가 4초이다.
q.append((1,1))

def second(): # 1초 지나게 하기.
    global q, k
    for i in alive: # 산 상어만 훑는다.
        h, w, drt = sha[i] # 상어 현재 위치, 방향, i
        ndi = -1 # 새 방향
        for j in sws[i][drt]: # i번째 상어의 drt방향 우선순위를 돌면서
            nh, nw = h + dh[j], w + dw[j]
            if 0<=nh<n and 0<=nw<n and g[nh][nw][1] == 0: # 그래프에서 체취가 0초 남은 상태라면
                ndi = j # 새 방향
                sha[i] = [nh, nw, ndi] # 상어 이동
                break
        if ndi < 0: # 체취가 없는 방향이 없다면
            for j in sws[i][drt]: # i번째 상어의 drt방향 우선순위
                nh, nw = h + dh[j], w + dw[j] # 돌면서
                if 0<=nh<n and 0<=nw<n and g[nh][nw][0] == i: # 자기 체취인 방향으로 정하고
                    ndi = j # 새 방향
                    sha[i] = [nh, nw, ndi] # 이동하고 끝
                    break
# 이부분이 문제 같은데
    for i in range(len(sha)): # 상어 자리가 겹치면 죽일거다.
        if i not in alive: # 죽은 애면 패스
            continue
        for j in range(i+1, len(sha)): # 무조건 i가 더 크다.
            if j not in alive: # 죽은 애면 패스
                continue
            ih, iw, idr = sha[i] # 산 친구의 ih, iw
            jh, jw, jdr = sha[j] # 산 친구의 ih, iw
            if ih == jh and iw == jw and j in alive: # 죽임 처리
                sha[j] = [-1, -1, -1]
                alive.remove(j)

    while q: # 체취 처리. 이 부분에서 아마 지나온 
        a = q.popleft()
        if len(a) == 2: # 상어 차레라면
            break
        h, w, sn, cnt = a
        if cnt-1 > 0: # 체취가 남아있을거면
            g[h][w] = [sn, cnt-1] # 그래프에 상어 체취 몇초 남았는지 갱신
            q.append((h, w, sn, cnt-1)) # 큐에 체취 추가
        elif cnt-1 == 0: # 체취가 끝났으면
            g[h][w] = [-1, 0] # 그래프 초기화.
    
    for i in alive: # 산 상어 체취 추가
        shh, shw, _ = sha[i] # 새 위치
        g[shh][shw] = [i, k] # 새 위치에 체취 추가.
        q.append((shh, shw, i, k)) # 새 체취 추가

    q.append((1, 1)) # 체취 훑으면 상어 차례라고 알려줌.

for i in range(1, 1002):
    second()
    # print(sha)
    # for i in g:
    #     print(*i)
    # print('=========')
    # print(alive)
    if len(alive) == 1:
        break
if i == 1001:
    ans = -1
else:
    ans = i
print(ans)

'''
from collections import deque
import sys
input = sys.stdin.readline
# 사방이동
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

n, m, k = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
sws = [[] for _ in range(m)] # 상어 방향 우선 순위
shadi = list(map(int, input().rstrip().split()))
for i in range(m):
    for j in range(4):
        d1, d2, d3, d4 = map(int, input().rstrip().split())
        sws[i].append([d1-1, d2-1, d3-1, d4-1]) # 방향은 1,2,3,4가 아닌 0,1,2,3으로 관리됨.
# 큐에는 방구들만 넣고 상어 위치, 방향 관리는 sha로 관리.
# shadi 는 초기 상어의 방향. 이것도 sha에 넣어서 관리 할 것.
sha = [[] for _ in range(m)] # 상어 본체의 위치. 상어를 1~n번이 아니라 0~n-1번으로 관리 할 예정
alive = set(range(m)) # 생존한 상어 여부 확인 할 것.
q = deque() # 체취 관리 할 것.
for i in range(n):
    for j in range(n):
        if g[i][j] == 0:
            g[i][j] = [-1, 0] # 그래프를 3차원으로 관리 할 예정. 몇번 상어의 체취가 몇초인지.
            continue
        a = g[i][j]-1 # 상어 번호는 1~n이 아니라 0~n-1로 관리됨.
        sha[a] = [i, j, shadi[a]-1]
        q.append((i, j, a, k)) # i, j에 a 상어의 체취가 k초간 지속된다.
        g[i][j] = [a, k] # a상어의 체취가 k초이다.
q.append((1,1)) # 체취 한 사이클을 알려주기 위한 값. 큐를 정지 시키는 용도.

def second(): # 1초 지나게 하기.
    global q, k
    for i in alive: # 산 상어만 훑는다.
        h, w, drt = sha[i] # 상어 현재 위치, 방향, 상어 i 정보.
        ndi = -1 # 새 방향. 0123이면 에러 날까봐 -1로 조정
        for j in sws[i][drt]: # i번째 상어의 drt방향 우선순위를 돌면서
            nh, nw = h + dh[j], w + dw[j]
            if 0<=nh<n and 0<=nw<n and g[nh][nw][1] == 0: # 그래프에서 체취가 0초 남은 상태라면
                ndi = j # 새 방향
                sha[i] = [nh, nw, ndi] # 상어 이동
                break
        if ndi < 0: # 체취가 없는 방향이 없다면
            for j in sws[i][drt]: # i번째 상어의 drt방향 우선순위
                nh, nw = h + dh[j], w + dw[j] # 돌면서
                if 0<=nh<n and 0<=nw<n and g[nh][nw][0] == i: # 자기 체취인 방향으로 정하고
                    ndi = j # 새 방향
                    sha[i] = [nh, nw, ndi] # 이동하고 끝
                    break
    
    for i in range(len(sha)): # 상어 자리가 겹치면 죽일거다.
        if i not in alive: # 죽은 애면 패스
            continue
        for j in range(i+1, len(sha)): # 무조건 i가 작으므로 i가 더 세다. range니까
            if j not in alive: # 죽은 애면 패스
                continue
            ih, iw, idr = sha[i] # 산 친구의 ih, iw
            jh, jw, jdr = sha[j] # 산 친구의 ih, iw
            if ih == jh and iw == jw and j in alive: # 같은 위치라면 죽임 처리
                sha[j] = [-1, -1, -1]
                alive.remove(j)

    while q: # 체취 처리. 이 부분에서 아마 지나온 
        a = q.popleft()
        if len(a) == 2: # 상어 차레라면
            break
        h, w, sn, cnt = a
        if cnt-1 > 0: # 체취가 남아있을거면
            g[h][w] = [sn, cnt-1] # 그래프에 상어 체취 몇초 남았는지 갱신
            q.append((h, w, sn, cnt-1)) # 큐에 체취 추가
        elif cnt-1 == 0: # 체취가 끝났으면
            g[h][w] = [-1, 0] # 그래프 초기화.
    
    for i in alive: # 산 상어 위치의 체취 추가
        shh, shw, _ = sha[i] # 새 위치
        g[shh][shw] = [i, k] # 그래프에 체취 추가.
        q.append((shh, shw, i, k)) # 새 체취 추가

    q.append((1, 1)) # 체취 훑으면 상어 차례라고 알려줌.

# 1001초 실행
for i in range(1, 1002):
    second()
    if len(alive) == 1:
        break
if i == 1001: # 1001초면 불가능
    ans = -1
else: # 1000초까지 정답 갱신
    ans = i
print(ans)
'''

'''
# 주석이 이쁜 코드
# BOJ 19237
from collections import defaultdict

N, M, k = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 초기방향
init_dir = defaultdict(int)
data = list(map(int, input().split()))
for i in range(M):
    init_dir[i + 1] = data[i]

# 우선순위 정보: {상어 번호: [[위쪽일때 4방향]],[아래쪽..],[왼쪽..],[오른쪽..]]}
priority = defaultdict(list)
for i in range(M):
    priority[i + 1].append([0])
    for _ in range(4):
        priority[i + 1].append(list(map(int, input().split())))

# 그래프: 칸 마다 [상어 번호, 상어 방향, 냄새 번호, 냄새 남은 시간]
for x in range(N):
    for y in range(N):
        if graph[x][y] == 0:
            graph[x][y] = [0, 0, 0, 0]
        else:
            shark_id = graph[x][y]
            shark_dir = init_dir[shark_id]
            smell_id = shark_id
            smell_time = k
            graph[x][y] = [shark_id, shark_dir, smell_id, smell_time]

# idx 1,2,3,4 순으로 상하좌우
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

# 전역 변수
shark_cnt = M
time = 0

# k를 상수로 사용
def get_k():
    return k


# 메인 로직
while True:
    new_graph = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]
    moved = set()

    # 모든 상어 이동
    for x in range(N):
        for y in range(N):
            info = graph[x][y]
            # 상어가 없으면, 냄새만 줄이기 (냄새도 없으면 패스)
            if info[0] == 0:
                # 주의: 이번 반복에 들어온 상어나 냄새가 없을때만 실행
                if new_graph[x][y][2] == 0:
                    # 냄새가 있는 경우
                    if info[2] != 0:
                        # 남은 시간이 1인 경우
                        if info[3] == 1:
                            new_graph[x][y] = [0, 0, 0, 0]
                        else:
                            new_graph[x][y] = [0, 0, info[2], info[3] - 1]
            # 상어가 있으면
            else:
                # 이미 움직인 상어라면, 패스
                if info[0] in moved:
                    continue
                # 빈칸을 찾아서, 우선순위 4방향대로 다음 칸 결정
                has_space = False
                next_dir = 0
                for i in range(4):
                    next_dir = priority[info[0]][info[1]][i]
                    nx = x + dx[next_dir]
                    ny = y + dy[next_dir]
                    if 0 <= nx < N and 0 <= ny < N and graph[nx][ny][2] == 0:
                        has_space = True
                        break
                # 빈칸이 없다면, 내 냄새를 찾아서 우선순위 4방향대로 다음 칸 결정
                if not has_space:
                    for i in range(4):
                        next_dir = priority[info[0]][info[1]][i]
                        nx = x + dx[next_dir]
                        ny = y + dy[next_dir]
                        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny][2] == info[0]:
                            break

                # 상어 움직이기
                # 1. 현재 위치에 내 냄새 남기기
                new_graph[x][y] = [0, 0, info[2], get_k() - 1]
                # 2. 다음 위치로 이동하기
                new_info = new_graph[nx][ny]
                # 다음 칸이 비었거나, 내가 더 낮을 경우: 현재 상어 이동
                # (즉, 이미 상어가 있다면 더 낮은 것이 살아남음)
                if new_info[0] == 0 or new_info[0] > info[0]:
                    new_graph[nx][ny] = [info[0], next_dir, info[0], get_k()]
                # 경쟁이 있었을 경우: 상어 마리수 -1
                if new_info[0] != 0:
                    shark_cnt -= 1
                # 3. 움직인 상어는 기록에 추가
                moved.add(info[0])

    # 소요 시간 +1
    time += 1

    # 조건에 따라 종료
    if shark_cnt == 1 or time >= 1000:
        break

    # 그래프 복사
    graph = new_graph


# 결과 출력
if time >= 1000 and shark_cnt >= 2:
    print(-1)
else:
    print(time)

'''


'''
# 빠른 코드

n, m, k = map(int, input().split())
array = [[(0, 0)] * n for _ in range(n)]
now_pos = [[0] * n for _ in range(n)]
pos = [None] * (m + 1)
for i in range(n):
  data = list(map(int, input().split()))
  for j in range(n):
    if data[j] != 0:
      array[i][j] = (data[j], k)
      now_pos[i][j] = data[j]
      pos[data[j]] = (i, j)

directions = [None] * (m + 1)
directions[1:] = list(map(int, input().split()))
dx = [None, -1, 1, 0, 0]
dy = [None, 0, 0, -1, 1]

priorities = [None]
for i in range(m):
  temp = [None]
  for _ in range(4):
    temp.append(list(map(int, input().split())))
  priorities.append(temp)

def update_smell(array, now_pos):

  for i in range(n):
    for j in range(n):
      if array[i][j][0] != 0:
        time = array[i][j][1] - 1
        if time == 0:
          array[i][j] = (0, 0)
        else:
          array[i][j] = (array[i][j][0], time)
      if now_pos[i][j] != 0:
        array[i][j] = (now_pos[i][j], k)

time = 0
while True:

  update_smell(array, now_pos)
  time += 1
  now_pos = [[0] * n for _ in range(n)]
  
  for num in range(m, 0, -1):
    if pos[num] == None:
      continue
    x, y = pos[num]
    d = directions[num]
    check_list = priorities[num][d]
    found = False
    for i in [0, num]:
      if found:
        continue
      for d in check_list:
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
          if array[nx][ny][0] == i:
            now_pos[nx][ny] = num
            directions[num] = d
            found = True
            break


  pos = [None] * (m + 1)
  remain = 0
  for i in range(n):
    for j in range(n):
      if now_pos[i][j] != 0:
        pos[now_pos[i][j]] = (i, j)
        remain += 1
  if remain == 1:
    print(time)
    break
  else:
    if time >= 1000:
      print(-1)
      break
'''
'''
# 빠른 코드2

n, m, k = map(int, input().split())

# 모든 상어의 위치와 방향 정보를 포함하는 2차원 리스트
array = []
for i in range(n) :
  array.append(list(map(int, input().split())))

# 모든 상어의 현재 방향 정보
directions = list(map(int, input().split()))

# 각 위치마다 [특정 냄새의 상어 번호, 특정 냄새의 남은 시간]을 저장하는 2차원 리스트
smell = [[[0, 0]] * n for _ in range(n)]

# 각 상어의 회전 방향 우선순위 정보
priorities = [[] for _ in range(m)]
for i in range(m) :
  for j in range(4) :
    priorities[i].append(list(map(int, input().split())))

# 특정 위치에서 이동 가능한 4가지 방향 (위, 아래, 왼쪽, 오른쪽)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 모든 냄새 정보를 업데이트
def update_smell() :
  # 각 위치를 하나씩 확인하며
  for i in range(n) :
    for j in range(n) :
      # 냄새가 존재하는 경우, 시간을 1만큼 감소시키기
      if smell[i][j][1] > 0 :
        smell[i][j][1] -= 1
      # 상어가 존재하는 해당 위치의 냄새를 k로 설정
      if array[i][j] != 0 :
        smell[i][j] = [array[i][j], k]


# 모든 상어를 이동시키는 함수
def move() :
  # 이동 결과를 담기 위한 임시 결과 테이블 초기화
  new_array = [[0] * n for _ in range(n)]
  # 각 위치를 하나씩 확인하며
  for x in range(n) :
    for y in range(n) :
      # 상어가 존재하는 경우
      if array[x][y] != 0 :
        direction = directions[array[x][y] - 1] # 현재 상어의 방향
        found = False
        # 일단 냄새가 존재하지 않는 곳이 있는지 확인
        for index in range(4) :
          nx = x + dx[priorities[array[x][y] - 1][direction-1][index] - 1]
          ny = y + dy[priorities[array[x][y] - 1][direction-1][index] - 1]
          if 0 <= nx and nx < n and 0 <= ny and ny < n :
            if smell[nx][ny][1] == 0 : # 냄새가 존재하지 않는 곳이면
              # 해당 상어의 방향 이동시키기
              directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction-1][index]
              # (만약 이미 다른 상어가 있다면 번호가 낮은 상어가 들어가도록)
              # 상어 이동시키기
              if new_array[nx][ny] == 0 :
                new_array[nx][ny] = array[x][y]
              else :
                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
              found = True
              break
        if found :
          continue
        # 주변에 모두 냄새가 남아 있다면, 자신의 냄새가 있는 곳으로 이동
        for index in range(4) :
          nx = x + dx[priorities[array[x][y] - 1][direction-1][index] - 1]
          ny = y + dy[priorities[array[x][y] - 1][direction-1][index] - 1]
          if 0 <= nx and nx < n and 0 <= ny and ny < n :
            if smell[nx][ny][0] == array[x][y] : # 자신의 냄새가 있는 곳이면
              # 해당 상어의 방향 이동시키기
              directions[array[x][y] - 1] = priorities[array[x][y]-1][direction-1][index]
              # 상어 이동 시키기
              new_array[nx][ny] = array[x][y]
              break
  return new_array


time = 0
while True :
  update_smell() # 모든 위치의 냄새를 업데이트
  new_array = move() # 모든 상어를 이동시키기
  array = new_array
  time += 1
  
  # 1번 상어만 남았는지 체크
  check = True
  for i in range(n) :
    for j in range(n) :
      if array[i][j] > 1 :
        check = False
  
  if check :
    print(time)
    break
  
  # 1,000초가 지날 때까지 끝나지 않았다면
  if time >= 1000 :
    print(-1)
    break
'''