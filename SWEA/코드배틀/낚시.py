'''
낚시터 자리잡기.

1. 낚시터의 개수 N은 5 이상 60 이하의 정수 (5 ≤ N ≤ 60)
2. 출입구는 항상 3개이다.
3. 각 출입구에 대기하고 있는 낚시꾼들의 수는 1 이상 20 이하의 정수
4. 낚시터의 자리가 부족하여 낚시꾼들이 자리를 잡지 못하는 경우는 입력으로 주어지지 않는다.
5. 두 개의 출입구에서 동시에 낚시꾼들이 입장하는 것은 불가능 하며, 반드시 하나의 출입구에 있는 모든 낚시꾼들의 배치가 끝나야 다른 출입구의 입장이 가능하다. 

[입력]
입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고, 그 다음 줄부터 T개의 테스트 케이스가 주어진다.
테스트 케이스의 첫 번째 줄에는 낚시터 자리의 개수 N이 주어진다.
그 다음 줄부터 3줄에 걸쳐 각각 두 개의 숫자가 주어진다. 첫 번째 숫자는 출입구의 위치이며, 두 번째 숫자는 해당 출입구에 대기하고 있는 낚시꾼들의 수 이다.

[출력]
출력은 "#t"를 찍고 한 칸 띄운 다음 정답을 출력한다. (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
정답은 각 낚시꾼들의 이동거리의 합이 최소가 될 때의 그 값이다.
'''
from collections import deque
from itertools import permutations

dl = [1, -1] # 우측 우선인데 오타
dr = [-1, 1] # 좌 우선인데 오타

def gl(ginfo): # 게이트 정보. 시작 위치, 사람 수.
    global g, n
    sta, hum = ginfo[0], ginfo[1] # 시작점, 사람 수
    q = deque() # 큐
    q.append((sta, 1)) # 시작지점, 그까지 거리 추가
    ds = {}
    while hum > 0: # 사람 수가 다 떨어지기 전까지
        i, di = q.popleft() # bfs
        if ds.get(di, 0) == 2:
            continue
        if 0 <= i < n and g[i] == 0: # 범위내이고 그래프 갱신 안되어있으면
            print(hum)
            print(g)
            ds.get(di, 0)
            ds[di] = ds.get(di, 0) + 1
            g[i] = di # 갱신하고
            hum -= 1 # 사람 하나 빼준다.
        for x in range(2): # 좌우 훑는데
            ni = i + dl[x] # dl로 우측 우선 확인
            if 0 <= ni < n: # 범위 내이면
                q.append((ni, di+1)) # 큐에 추가

def gr(ginfo): # 게이트 정보. 시작 위치, 사람 수.
    global g, n
    sta, hum = ginfo[0], ginfo[1] # 시작점, 사람 수
    q = deque() # 큐
    q.append((sta, 1)) # 시작지점, 그까지 거리 추가
    ds = {}
    while hum > 0: # 사람 수가 다 떨어지기 전까지
        i, di = q.popleft() # bfs
        if ds.get(di, 0) == 2:
            continue
        if 0 <= i < n and g[i] == 0: # 범위내이고 그래프 갱신 안되어있으면
            print(hum)
            print(g)
            ds.get(di, 0)
            ds[di] = ds.get(di, 0) + 1
            g[i] = di # 갱신하고
            hum -= 1 # 사람 하나 빼준다.
        for x in range(2): # 좌우 훑는데
            ni = i + dr[x] # dl로 우측 우선 확인
            if 0 <= ni < n: # 범위 내이면
                q.append((ni, di+1)) # 큐에 추가

for testcase in range(1, int(input())+1):
    n = int(input())
    gate = []
    ans = int(10e9)
    for _ in range(3): # 게이트 정보
        wi, fi = map(int, input().split())
        gate.append([wi-1, fi])

    for i in permutations(gate, 3): # 게이트 순서 순열
        g = [0] * n
        for j in i: # 게이트 순서대로 돌면서
            gl(j)
            if sum(g) >= ans:
                break
        ans = min(ans, sum(g))
        g = [0] * n
        for j in i:
            gr(j)
            if sum(g) >= ans:
                break
        ans = min(ans, sum(g))
    print(f"#{testcase} {ans}")





'''
5
10
4 5
6 2
10 2

18


19 16 12
39
47
'''








