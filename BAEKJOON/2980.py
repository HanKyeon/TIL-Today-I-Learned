'''
도로와 신호등

문제
상근이는 트럭을 가지고 긴 일직선 도로를 운전하고 있다. 도로에는 신호등이 설치되어 있다. 상근이는 각 신호등에 대해서 빨간 불이 지속되는 시간과 초록 불이 지속되는 시간을 미리 구해왔다. (빨강색과 초록색 불빛은 무한히 반복된다)

상근이의 트럭이 도로에 진입했을 때, 모든 신호등의 색상은 빨간색이고, 사이클이 막 시작한 상태이다. 상근이는 1초에 1미터를 움직인다. 신호등의 색상이 빨간색인 경우에는 그 자리에서 멈추고 초록색으로 바뀔때 까지 기다린다.

상근이가 도로의 끝까지 이동하는데 걸리는 시간을 구하는 프로그램을 작성하시오. 도로의 시작은 0미터이고, 끝은 L미터인 지점이다.

입력
신호등 갯수 N 도로길이 L
신호등 위치 D 빨간불 지속 R 초록불 지속 G
D가 증가하는 순서로 제시.

출력
첫째 줄에 상근이가 도로의 끝까지 이동하는데 걸리는 시간을 출력한다.
'''

n, l = map(int, input().split()) # 입ㄺ
shd =[[0,0,0]] + [list(map(int, input().split())) for _ in range(n)] + [[l,0,0]] # 신호등. 위치 빨 파
t = 0 # 시간
for i in range(1, n+2): # 신호등들 순회
    t += shd[i][0]-shd[i-1][0] # 이전 신호등부터의 거리만큼 시간 추가
    if shd[i][1]+shd[i][2] == 0: # 빨간불 파란불 합이 0이면
        t += shd[i][1] # 빨간불 시간 추가
    else:
        fla = t % (shd[i][1]+shd[i][2]) # 신호등 앞까지 진행된 시간을 신호사이클로 나눠준 시간만큼 진행
        if fla < shd[i][1]: # 빨간불 유지시간 내라면
            t += shd[i][1]-fla # 시간에 추가
        else: # 파란불이면 건너라
            continue
print(t)

'''
N, L = map(int, input().split())    # N: 신호등 개수 / L: 도로 길이(0부터 시작)
ans = 0
prev_D = 0
for _ in range(N):
    D, R, G = map(int, input().split())     # D: 신호등 위치 / R, G: 빨간불, 초록불 지속 시간

    ans += D-prev_D

    time = [0, 1]
    while True:
        time[0] += R
        time[1] = 1
        if time[0] >= ans:
            break

        time[0] += G
        time[1] = 0
        if time[0] >= ans:
            break

    if time[1] == 1:                        # 현재 신호가 빨간불이면
        ans += time[0]-ans                  # 기다려야하는 시간만큼 추가

    prev_D = D                              # 현재 신호등 위치 저장

ans += L - prev_D                           # 현재 위치에서 도착지에 도착할때까지의 거리 추가
print(ans)
'''








'''
시작점0
위치

0 0
3 5 5 cycle = 10
5 2 2 cycle = 4

1 1
3 4 5
5 1 2

2 2
3 3 5
5 0 2

3 3
3 2 5
5 2 1

4 3
3 1 5
5 2 0

5 3
3 0 5
5 1 2

6 4
3 5 4
5 0 2

7 5
5 2 1

8 6
5 2 0

9 7
10 8
11 9
12 10

'''









