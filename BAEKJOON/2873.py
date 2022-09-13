'''
롤러코스터

r c. 1,1에서 n, n까지 최댓값으로 도달하는 방법.
경로를 출력해야 한다. 사방이동만 가능.

입력
R, C 제시. 2이상 1000이하. R개 줄에 각 칸을 지날 때 얻을 수 있는 기쁨 제시. 1000이하 양정수

출력
가장 큰 기쁨을 주는 롤러코스터의 1,1에서 n,n까지 어떻게 움직이면 되는지 출력. 위U 오R 왼L 아래D
'''
'''
1. r, c 중 하나라도 홀수면 모든 칸 방문 가능. 홀수의 역방향으로 먼저 이동 할 경우.
2. r, c 둘 다 짝수일 경우. 이 때가 문젠데..

한붓 그리기 생각하면 될듯? 팔이 몇개여야 할까 -> 폐기

우수법 좌수법 비슷한 방법으로 칸을 하나하나 제외해서 다 덮을 수 있는지 확인.

합이 홀수이면 (idx기준) 그 칸 하나 빼고 다 덮을 수 있고, 나머지는 2칸 이상 벌어짐. 2칸 이상 못지나 갈 때, 합이 홀수인 칸은 하나는 꼭 포함되어 있었다. 예외 있으면 틀려야지...

사방탐색 -> 어느 한쪽으로 치우치게 가면은 에러가 날 수 있다. 우,하 우선에 따라서. 좌측 맨 아래가 가장 적을 때 에러가 낫음. 구석탱이에 최솟값이 있으면 에러가 뜨는듯?
=> 좌표를 기준으로 방향의 우선순위를 잡아줌. -> 폐ㄱㅣ y좌표까지 고려해야 할듯 or 극단일 때 조정.
-> 사분면 나눠서 해도 불가. -> 먼저 둘러두고 시작하면 되려나 가능은 해보이는데 -> 내가 어려워서 포기

'''
from collections import deque
import sys
input = sys.stdin.readline
# 하 상 우 좌
dhbx = [1, -1, 0, 0]
dwbx = [0, 0, 1, -1]
bxa = ['D', 'U', 'R', 'L']
# 좌 상 하 우
dhox = [0, -1, 1, 0]
dwox = [-1, 0, 0, 1]
oxa = ['L', 'U', 'D', 'R']

r, c = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(r)]
ans = ''
if r % 2: # 하나라도
    for i in range(r):
        if i == r-1:
            ans += 'R' * (c-1)
            break
        if i % 2:
            ans += 'L' * (c-1) + 'D'
        else:
            ans += 'R' * (c-1) + 'D'
elif c % 2: # 홀수면 전부 다 돌 수 있음.
    for i in range(c):
        if i == c-1:
            ans += 'D' * (r-1)
            break
        if i % 2:
            ans += 'U' * (r-1) + 'R'
        else:
            ans += 'D' * (r-1) + 'R'
else: # 둘 다 짝수길이 일 때.
    val, jp = int(10e9), [0, 0]
    for i in range(r):
        for j in range(c):
            if (i + j) % 2 == 0:
                continue
            if g[i][j] < val:
                val, jp = g[i][j], [i, j]
    del val # val은 더이상 안쓴다.

    '''
    검색해서 찾아봄..
    아래, 위 이동을 묶었으므로 뺄 좌표 // 2만큼 진행해준다. 이후 우측 이동을 한 번 했으므로
    뺀 곳이 있는 좌표와 y좌표가 같거나, 그 다음x에 뺀 곳의 좌표가 있거나. 그럴 경우 좌우 와리가리 쳐주는 것이다. 
    '''
    ans = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (jp[1] // 2) # 직전까지 진행해준다. 그럼 x좌표가 같거나, x+1에 뺀 좌표가 있을 것.
    x = 2 * (jp[1] // 2) # x 좌표
    y = 0 # 당연히 맨 위에서 끝난다. 아래이동 우측한칸 위이동 우측한칸을 세트로 묶었으니.
    xbound = 2 * (jp[1] // 2) + 1 # 뺄 곳의 x좌표로 만들어주는데, 같은 좌표로 끝났다면 +1까지 해줄 것이고, 다음 좌표라도 +1까지 해줘야 정상적으로 지그재그 이동이 가능해진다. xbound는 지그재그 이동을 할 범위라 보면 된다.

    while x != xbound or y != r - 1: # x가 끝범위와 다르다면, 즉 x가 xbound-1인 동안. 즉, [r-1, xbound]에 도달하면 반복이 끝난다. 이 때, xbound+r-1이 무조건 홀수가 되므로, 해당 부분에 도달하지 못할 리는 없음. 진짜 똑똑한듯. r이 짝수이므로 r-1은 홀수, 2칸씩 이동 후 우측으로 한 칸 이동했으므로 xbound는 무조건 짝수이다. 고로 i+j가 홀수가 되어서 r-1, xbound에 무조건 도달하게 된다.
        if x < xbound and [y, xbound] != jp: # 뺀 좌표와 같아지지 않도록 예외처리.
            x += 1 # x를 이동시켜주고
            ans += 'R' # 우측이동
        elif x == xbound and [y, xbound - 1] != jp: # 같은 좌표이고, 왼쪽이 뺀 좌표가 아니라면
            x -= 1 # 좌측이동
            ans += 'L'
        if y != r - 1: # r의 끝이 아니라면
            y += 1 # 아래 이동
            ans += 'D'
    # [r-1, xbound에 도달하면 ]
    ans += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - jp[1] - 1) // 2)
print(ans)

'''
    v = [[0] * c for _ in range(r)] # 방문 처리 노드.
    y, x = jp # 좌표
    v[y][x] = 1 # 이 칸 안밟고 갈 것.
    v[0][0] = 1 # 시작지점 방문
    q = deque()
    q.append((0, 0))
    while q:
        h, w = q.popleft()
        if w <= x:
            for i in range(4):
                nh, nw = h + dhbx[i], w + dwbx[i]
                if 0<=nh<r and 0<=nw<c and v[nh][nw] == 0:
                    v[nh][nw] = 1
                    q.append((nh, nw))
                    ans += bxa[i]
                    break
        else:
            for i in range(4):
                nh, nw = h + dhox[i], w + dwox[i]
                if 0<=nh<r and 0<=nw<c and v[nh][nw] == 0:
                    v[nh][nw] = 1
                    q.append((nh, nw))
                    ans += oxa[i]
                    break
print(ans)
'''













