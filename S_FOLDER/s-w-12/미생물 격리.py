'''
미생물 격리

정사각형 안에 k개의 미생물 군집.
가로 n, 세로 n에 있다. 바깥쪽 가장자리 약품처리.

1.최초 각 미생물 군집의 위치와 군집 내 미생물의 수, 이동 방향이 주어진다. 약품이 칠해진 부분에는 미생물이 배치되어 있지 않다. 이동방향은 상, 하, 좌, 우 네 방향 중 하나이다.

2. 각 군집들은 1시간마다 이동방향에 있는 다음 셀로 이동한다.

3. 미생물 군집이 이동 후 약품이 칠해진 셀에 도착하면 군집 내 미생물의 절반이 죽고, 이동방향이 반대로 바뀐다. 
미생물 수가 홀수인 경우 반으로 나누어 떨어지지 않으므로, 다음과 같이 정의한다.
살아남은 미생물 수 = 원래 미생물 수를 2로 나눈 후 소수점 이하를 버림 한 값
따라서 군집에 미생물이 한 마리 있는 경우 살아남은 미생물 수가 0이 되기 때문에, 군집이 사라지게 된다,

4. 이동 후 두 개 이상의 군집이 한 셀에 모이는 경우 군집들이 합쳐지게 된다. 
합쳐 진 군집의 미생물 수는 군집들의 미생물 수의 합이며, 이동 방향은 군집들 중 미생물 수가 가장 많은 군집의 이동방향이 된다. 
합쳐지는 군집의 미생물 수가 같은 경우는 주어지지 않으므로 고려하지 않아도 된다.

M시간 동안 격리 했을 때, 남아있는 미생물 수는?

입력
테케T
셀 갯수 n, 격리시간m, 군집 갯수 k 제시
k개의 미생물 정보 제공. 세로, 가로, 수, 방향
상1 하2 좌3 우4

출력
#테케t 살아남은 미생물 수 총합.
'''
from heapq import heappop, heappush

# 사방향. 방향 전환은 (+2)%2
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

def bfs1t(): # bfs 1번 하는 함수
    dtn = {}
    ret = 0
    while heap:
        num, h, w, di = heappop(heap)
        nh, nw = h+dh[di], w+dw[di]
        if 0<=nh<n and 0<=nw<n:
            if nh==0 or nw==0 or nh==n-1 or nw==n-1:
                num //= 2
                if di%2:
                    di -=1
                else:
                    di += 1
            if dtn.get((nh, nw), 0):
                dtn[(nh, nw)][0] += num
                dtn[(nh, nw)][3] = di
            else:
                dtn[(nh,nw)] = [num, nh, nw, di]
    for i in dtn.keys():
        ret += dtn[i][0]
        heappush(heap, dtn[i])
    return ret

for tc in range(1, int(input())+1):
    n, m, k = map(int, input().rstrip().split())
    heap = []
    for _ in range(k):
        h, w, num, di = map(int, input().rstrip().split())
        heappush(heap, (num, h, w, di-1)) # 미생물 수 적은 순서대로
    ans = 0
    for i in range(m):
        ans = bfs1t()
    print(f"#{tc} {ans}")















