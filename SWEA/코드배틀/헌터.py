'''
헌터

몬스터를 먼저 잡고 그에 맞는 집을 찾아가야한다.


1. 몬스터의 위치와 고객의 위치는 한 변의 길이 N이 3 이상 10 이하인 정사각형의 맵으로 주어진다. (3≤N≤10)
2. 고객 및 몬스터 개수 M은 1 이상 4 이하이다. (1≤M≤4)
3. 고객 및 몬스터는 1부터 M까지 번호가 부여되어 있다.
4. 고객의 번호는 처리해 달라는 몬스터의 번호이다.
5. 맵에서 몬스터는 양수로 주어지고 고객은 음수로 주어진다.
   그 수의 절대값은 몬스터의 번호 및 고객의 번호를 의미한다. 0인 경우는 아무것도 없는 경우이다.
6. 몬스터와 고객이 같은 위치를 가지는 경우는 없다.
7. 헌터는 상하좌우로 1시간에 한 칸씩 움직일 수 있다.
8. 헌터는 맵의 맨 왼쪽 위인 (1, 1)부터 시작한다.

입력

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다 (1≤T≤50)
그 다음 줄부터 테스트 케이스 T개 온다. 각 테스트 케이스는 모두 N + 1 줄로 구성되어 있다.
첫 줄은 맵의 한 변의 길이 N이 주어진다.
그 다음 N 줄에는 N*N 맵의 정보가 주어진다. 맵에서 양수는 몬스터, 음수는 고객을 뜻한다.

출력

테스트 케이스 T에 대한 결과는 “#T”을 찍고, 한 칸 띄고, 정답을 출력한다.
(T는 테스트케이스의 번호를 의미하며 1부터 시작한다.)
정답은 모든 작업을 완료할 수 있는 가장 빠른 시간이다.
'''
# 부분집합으로 전부 다 훑기


from itertools import combinations, permutations

for testcase in range(1, int(input())+1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    dic = {} # 번호를 받아 좌표를 받을 것
    mh = []
    for i in range(n):
        for j in range(n):
            if g[i][j] > 0: # 몹들
                dic[g[i][j]-1] = (i, j) # 딕트에 추가
                mh.append(g[i][j]-1) # mh에 추가
            elif g[i][j] < 0: # 집들
                dic[abs(g[i][j])+3] = (i, j) # 딕트에 추가
                mh.append(-g[i][j]+3) # mh에 추가
    ms = [x for x in mh if x<4] # 몹들 번호
    a = list(permutations(mh, len(mh))) # 돌 수 있는 모든 순열
    na = [] # 조건 만족한 경우 담을 것.

    for i in a:
        fla = True # 일단 맞다고 보자.
        for j in ms:
            if i.index(j) > i.index(j+4): # 몹이 집보다 뒤에 있으면
                fla = False # 틀린 길
                break
        if fla == True: # 맞는 길이면
            na.append(i) # na에 담기
    ans = int(10e9) # 최솟값을 구해야해서 일단 10억으로 잡아둠.
    for i in na:
        now, cnt = (0, 0), 0 # 시작점, 거리 담을 값
        for j in i: # 순열 돌면서
            h, w = now # 현좌표 확인
            nh, nw = dic[j] # 이동할 좌표 확인
            now = (nh, nw) # 현좌표 이동
            cnt += abs(nh-h) + abs(nw-w) # 총 이동거리 증가
            if cnt >= ans: # 현재까지 이동거리가 ans보다 크면
                break # 끝
        ans = min(cnt, ans) # 현재 ans와 cnt의 최솟값 저장
    print(f"#{testcase} {ans}")
    








