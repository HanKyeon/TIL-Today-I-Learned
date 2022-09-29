'''
원자 소멸 시뮬레이션

2차원 평면에서 이동, 두개 이상의 원자가 충돌 할 경우 충돌한 원자들은 각자 보유한 에너지를 모두 방출하고 소멸.

원자의 움직임
1. 최초 위치 x,y
2. 원자는 4방이동한다.
3. 모든 원자는 1초에 1만큼 이동.
4. 최초 위치에서 동시 이동.
5. 두 개 이상의 원자 충돌 시 에너지 방출 및 소멸

n개의 원자들의 x,y 이동 방향, 보유 에너지가 주어질 때 원자들이 소멸되면서 방출하는 에너지의 총합을 구해라.

n은 1000이하. 보유 에너지 100이하 자연수
원자들 첫 위치 x,y는 -1000이상 1000이하 정수
2차원 평면 위에서 움직이며 이동 좌표 범위 제한x
원자 이동은 0 상 1 하 2 좌 우 3
우너자들은 동시에 1초에 이동 방향으로 1만큼 이동.
원자 최초 위치 중봇x
충돌시 바로 소멸
이동방향 변경x

입력
테케T
x위치, y위치, 이동 방향, 보유 에너지k 제시.
이동 방향은 상0 하1 좌2 우3

출력
#테케 방출 에너지 총합
'''
def nuclear():
    global atms
    natms = {} # (h, w)로 부르고, [에너지합, [방향]] 을 값으로
    for i in atms:
        h, w = i
        eng, di = atms[i]
        nh, nw = h+dh[di], w+dw[di]
        if natms.get((nh, nw), 0):
            natms[(nh, nw)][0] += eng
            natms[(nh, nw)][1].append(di)
        else:
            natms[(nh, nw)] = [eng, [di]]
    atms = {} # (h, w)로 부르고, [eng, di] 를 값으로.
    ret = 0
    for i in natms:
        eng, di = natms[i]
        if len(di) >= 2:
            ret += eng
            continue
        atms[i] = [eng, di[0]]
    return ret

dh = [1, -1, 0, 0]
dw = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    n = int(input())
    atms = {}
    for _ in range(n):
        w, h, di, eng = map(int, input().rstrip().split())
        atms[(h*2, w*2)] = [eng, di]
    kys = list(atms.keys())
    l = 0
    for i in range(n-1):
        for j in range(i+1, n):
            dy, dx = abs(kys[i][0]-kys[j][0]), abs(kys[i][1]-kys[j][1])
            if dy == dx:
                b = dy+dx
            elif dy == 0 or dx == 0:
                b = max(dy, dx)
            if l < b:
                l = b
    ans = 0
    if l == 0:
        print(f"#{tc} {ans}")
    for _ in range(l+1): # b+1번하니 에러 뜨네? -> l에 최댓값 넣어놓고 뭐하냐?
        ans += nuclear()
    print(f"#{tc} {ans}")
















