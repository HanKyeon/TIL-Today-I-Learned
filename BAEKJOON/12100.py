'''
2048 easy

4*4 보드에서 즐기는 게임.
보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동 시키는게 1번의 이동.
같은 값을 갖는 두 블록이 충돌 시 하나로 합쳐짐.
실제 게임은 이동마다 블록이 추가되지만, 문제에서는 추가되지 않는다.
한 번의 이동에서 이미 합쳐진 블록은 또 합쳐질 수 없다.

입력
보드 크기 n 1이상 20이하
보드판 초기 상태 제시

출력
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록 출력
'''
import sys
input = sys.stdin.readline

# 상 하 좌 우 0123
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

def wasd(di, ct, vl, gg): # 방향, 몇회 했는지, 현재 저장된 값, 그래프
    global ans
    if ct == 5 and vl > ans: # 끝까지 갔으면 최댓값 기록
        ans = max(ans, vl)
        return # 종료
    if vl * (2**(5-ct)) <= ans : # 저장된 값에 2**남은 횟수 곱한 값 vs ans 비교해서 백트래킹
        return
    ng = []
    for i in range(n): # 복사해서 쓸 것이다!
        ng.append(gg[i][:])
    
    nv = [[0]*n for _ in range(n)] # 방문처리.
    
    if di == 0: # 상
        for i in range(1, n):
            for j in range(n):
                if ng[i][j] == 0:
                    continue
                nh, nw = i + dh[di], j + dw[di] # 한 칸 이동
                while 0<=nh<n and 0<=nw<n: # 범위 내일 때
                    if 0<=nh<n and 0<=nw<n and ng[nh][nw] == ng[nh-dh[di]][nw-dw[di]] and nv[nh][nw] == 0: # 합칠 수 있으면 합치기
                        nv[nh][nw] = 1
                        ng[nh][nw] *= 2
                        ng[nh-dh[di]][nw-dw[di]] = 0
                        break # 합치면 땡
                    elif 0<=nh<n and 0<=nw<n and ng[nh][nw] == 0: # 0이면 위치 바꿔주기
                        ng[nh-dh[di]][nw-dw[di]], ng[nh][nw] = ng[nh][nw], ng[nh-dh[di]][nw-dw[di]]
                    elif 0<=nh<n and 0<=nw<n and ng[nh][nw] != 0: # 0 아닌거 만나면 그대로 끝. 같은 값일 때 처리는 위에서 했음.
                        break
                    nh, nw = nh + dh[di], nw + dw[di] # 하나 더 이동
        vl = max(map(max, *ng))
        for i in range(4): # dfs
            wasd(i, ct+1, vl, ng)
    elif di == 1: # 하. 설명은 상과 동일
        for i in range(n-1, -1, -1): # 다른 점 : 아래쪽부터 아래로 보내줘야 함
            for j in range(n):
                if ng[i][j] == 0:
                    continue
                nh, nw = i + dh[di], j + dw[di]
                while 0<=nh<n and 0<=nw<n:
                    if 0<=nh<n and 0<=nw<n and ng[nh][nw] == ng[nh-dh[di]][nw-dw[di]] and nv[nh][nw] == 0:
                        nv[nh][nw] = 1
                        ng[nh][nw] *= 2
                        ng[nh-dh[di]][nw-dw[di]] = 0
                        break
                    elif 0<=nh<n and 0<=nw<n and ng[nh][nw] == 0:
                        ng[nh-dh[di]][nw-dw[di]], ng[nh][nw] = ng[nh][nw], ng[nh-dh[di]][nw-dw[di]]
                    elif 0<=nh<n and 0<=nw<n and ng[nh][nw] != 0:
                        break
                    nh, nw = nh + dh[di], nw + dw[di]
        vl = max(map(max, *ng))
        for i in range(4):
            wasd(i, ct+1, vl, ng)
    elif di == 2: # 좌 : 상과 설명 동일
        for i in range(n):
            for j in range(n):
                if ng[i][j] == 0:
                    continue
                nh, nw = i + dh[di], j + dw[di]
                while 0<=nh<n and 0<=nw<n:
                    if 0<=nh<n and 0<=nw<n and ng[nh][nw] == ng[nh-dh[di]][nw-dw[di]] and nv[nh][nw] == 0:
                        nv[nh][nw] = 1
                        ng[nh][nw] *= 2
                        ng[nh-dh[di]][nw-dw[di]] = 0
                        break
                    elif 0<=nh<n and 0<=nw<n and ng[nh][nw] == 0:
                        ng[nh-dh[di]][nw-dw[di]], ng[nh][nw] = ng[nh][nw], ng[nh-dh[di]][nw-dw[di]]
                    elif 0<=nh<n and 0<=nw<n and ng[nh][nw] != 0:
                        break
                    nh, nw = nh + dh[di], nw + dw[di]
        vl = max(map(max, *ng))
        for i in range(4):
            wasd(i, ct+1, vl, ng)
    elif di == 3: # 우
        for i in range(n):
            for j in range(n-1, -1, -1): # 다른 점 : 우측부터 우측이동 시켜줘야함.
                if ng[i][j] == 0:
                    continue
                nh, nw = i + dh[di], j + dw[di]
                while 0<=nh<n and 0<=nw<n:
                    if 0<=nh<n and 0<=nw<n and ng[nh][nw] == ng[nh-dh[di]][nw-dw[di]] and nv[nh][nw] == 0:
                        nv[nh][nw] = 1
                        ng[nh][nw] *= 2
                        ng[nh-dh[di]][nw-dw[di]] = 0
                        break
                    elif 0<=nh<n and 0<=nw<n and ng[nh][nw] == 0:
                        ng[nh-dh[di]][nw-dw[di]], ng[nh][nw] = ng[nh][nw], ng[nh-dh[di]][nw-dw[di]]
                    elif 0<=nh<n and 0<=nw<n and ng[nh][nw] != 0:
                        break
                    nh, nw = nh + dh[di], nw + dw[di]
        vl = max(map(max, *ng))
        for i in range(4):
            wasd(i, ct+1, vl, ng)


n = int(input())
if n == 1:
    ans = int(input())
    print(ans)
else:
    g = [list(map(int, input().rstrip().split())) for _ in range(n)]
    v = [[0]*n for _ in range(n)] # 합쳐진 칸인지 아닌지 확인 할 것!
    ans = max(map(max, *g)) # 적어도 현재 최댓값은 깔고 간다.
    for i in range(4): # dfs 시작해라~
        wasd(i, 0, ans, g)
    print(ans)



'''
10
0 0 64 32 32 0 0 0 0 0
0 32 32 64 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0
64 64 128 0 0 0 0 0 0 0
0 0 64 32 32 0 0 0 0 0
0 32 32 64 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0
64 64 128 0 0 0 0 0 0 0
128 32 0 0 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0

우 상 우 하 상

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
'''

