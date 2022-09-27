'''
주사위 굴리기

크기 n*m 지도. 지도 위에 주사위 전개도. 좌표는 r,c
주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여져 있는 곳의 좌표는 x,y이다. 처음 주사위에는 모든 면이 0이다.
지도 각 칸에는 정수 하나씩. 주사위를 굴렸을 때, 이동한 칸에 쓰여있는 수가 0이면 주사위의 바닥면에 쓰여있는 칸에 복사된다. 0이 아닌 경우에는 칸에 쓰여있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여있는 수는 0이 된다.

주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동 했을 때마다 상단에 쓰여있는 값을 구하는 프로그램을 작성하시오.
주사위는 지도 밖으로 이동시킬 수 없다. 바깥으로 이동시키려 하면 명령 무시, 출력 무시.

입력
n, m 제시. 주사위 좌표 x,y 제시. 명령 갯수 k 제시
n개 줄에 북->남 서->동 순서로 제시.
주사위를 놓은 칸에 쓰여있는 수는 항상 0이다. 지도의 각 칸에 쓰여있는 수는 10미만의 자연수 또는 0.
마지막 줄에 이동하는 명령이 순서대로 제시. 동1 서2 북3 남4

출력
이동 할 때마다 주사위의 윗면에 쓰여있는 수를 출력. 바깥으로 이동시키려 하는 경우 해당 명령 무시. 출력 x
'''
import sys
input = sys.stdin.readline

# 주사위. 상향이 1 하향이 6 동쪽이3 아래가6 남쪽이5 북쪽이2 서쪽이4
zsw = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
# 동서북남 1-1 2-1 3-1 4-1
dh = [0, 0, -1, 1]
dw = [1, -1, 0, 0]
def zg(num):
    if num == 1:
        zsw[1], zsw[2], zsw[3], zsw[4], zsw[5], zsw[6] = zsw[4], zsw[2], zsw[1], zsw[6], zsw[5], zsw[3]
    if num == 2:
        zsw[1], zsw[2], zsw[3], zsw[4], zsw[5], zsw[6] = zsw[3], zsw[2], zsw[6], zsw[1], zsw[5], zsw[4]
    if num == 3:
        zsw[1], zsw[2], zsw[3], zsw[4], zsw[5], zsw[6] = zsw[2], zsw[6], zsw[3], zsw[4], zsw[1], zsw[5]
    if num == 4:
        zsw[1], zsw[2], zsw[3], zsw[4], zsw[5], zsw[6] = zsw[5], zsw[1], zsw[3], zsw[4], zsw[6], zsw[2]

n, m, h, w, k = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
ys = list(map(int, input().rstrip().split()))
for i in ys:
    nh, nw = h+dh[i-1], w+dw[i-1]
    if not (0<=nh<n and 0<=nw<m):
        continue
    h, w = nh, nw
    zg(i)
    if g[h][w] == 0:
        g[h][w] = zsw[6]
    else:
        zsw[6] = g[h][w]
        g[h][w] = 0
    print(zsw[1])



'''
# 기본
  2
4 1 3
  5
  6
# 1동
  2
6 4 1
  5
  3
# 2서
  2
1 3 6
  5
  4
# 3남
  6
4 2 3
  1
  5
# 4북
  1
4 5 3
  6
  2
'''


















