'''
로봇 시뮬레이션

가로A 세로B 크기 땅. 로봇 n개. 최대100개
로봇위치 x, y. 로봇은 nwes 중 하나를 바라보고 서있다. 위치 역시 다른 상태로 시작.
m개의 명령. 명령은 스크립트로 작동.
L : 좌로 90도 회전
R : 우로 90도 회전
F : 전방 한 칸 전진
명령이 잘못될 수 있다. 두가지 존재.
1. Robot X crashes into the wall : 벽에 박거나 벗어나거나.
2. Robot X crashes into robot Y : Y랑 충돌하거나.

입력
a, b 제시.
n, m 제시.
n개 줄 로봇 초기 위치 제시.
m개 줄 명령 제시. 로봇넘버, LRF, 반복횟수. 1이상 100이하 반복

출력
결과 출력.
문제 없을 시 OK 문제 있다면 위처럼, 가장 먼저 발생하는 충돌 출력.
'''
import sys
input = sys.stdin.readline

mov = [(0, 1), (1,0), (0,-1), (-1,0)] # 북이 우측

def turning(robotNumber:int, order:int, repeatTimes:int):
    if repeatTimes % 4:
        rb[robotNumber][2] = (rb[robotNumber][2] + repeatTimes%4*order) % 4

def querySolve(robotNumber:int, repeatTimes:int) -> str:
    h, w, di = rb[robotNumber]
    nh, nw = h, w
    dh, dw = mov[di]
    for _ in range(repeatTimes):
        h, w = h+dh, w+dw
        if 0<=h<a and 0<=w<b:
            if (h, w) in v:
                for i in range(1, n+1):
                    x, y, _ = rb[i]
                    if x == h and w == y:
                        return f"Robot {robotNumber} crashes into robot {i}"
        else:
            return f"Robot {robotNumber} crashes into the wall"
    else:
        rb[robotNumber][0], rb[robotNumber][1] = h, w
        v.add((h, w))
        v.remove((nh, nw))
    return False

a, b = map(int, input().rstrip().split())
n, m = map(int, input().rstrip().split())
v = set()
rb = [[-1,-1,-1]]
parseDirection = {"N":0, "E":1, "S":2, "W":3}
for i in range(1, n+1):
    x, y, d = input().rstrip().split()
    x, y = int(x), int(y)
    rb.append([x-1, y-1, parseDirection[d]])
    v.add((x-1, y-1))
queryz = [input().rstrip().split() for _ in range(m)]
for i in queryz:
    rbn, lrf, rep = i
    rbn, rep = int(rbn), int(rep)
    if lrf == "L":
        turning(rbn, -1, rep)
        continue
    elif lrf == "R":
        turning(rbn, 1, rep)
        continue
    a = querySolve(rbn, rep)
    print(rb)
    if a:
        print(a)
        break
else:
    print("OK")



'''
1 3
2 1
1 1 N
1 2 N
1 F 2


2에 먼저 부대낀다.

3 3
1 9
2 2 W
1 F 1
1 L 1
1 F 1
1 L 1
1 F 2
1 L 5
1 F 2
1 R 3
1 F 2

5 4
2 2
1 1 E
5 4 W
1 L 96
1 F 2
'''

'''

5 4
2 2
1 1 E
5 4 W
1 F 7
2 F 7

5 4
2 4
1 1 E
5 4 W
1 F 3
2 F 1
1 L 1
1 F 3

5 4
2 2
1 1 E
5 4 W
1 L 96
1 F 2

5 4
2 3
1 1 E
5 4 W
1 F 4
1 L 1
1 F 20


Robot 1 crashes into the wall
Robot 1 crashes into robot 2
OK
Robot 1 crashes into robot 2
'''


