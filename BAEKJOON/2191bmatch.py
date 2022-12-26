'''
들쥐의 탈출

N마리 들쥐와 M개 땅굴.
2차우너 평면 상의 한 위치 존재.
매가 들쥐를 습격 했을 때 쥐들은 매를 피하기 위해 땅굴 속으로 숨을 수 있다.
모든 쥐들이 땅굴에 숨을 수 있다면 매에 잡아먹히는 쥐가 한마리도 없지만, 각 굴에는 한 마리의 쥐만 들어갈 수 있으며, 도망가는 속도가 있기에 모든 쥐들이 도망 갈 수 있는 것이 아니다.
매는 현재 기준으로 S초 이후 지상에 도착한다.
들쥐는 매 초당 V만큼의 거리를 움직인다. S초에 정확히 땅굴에 도착해도 도착 가능.
잡아먹히게 되는 들쥐의 최소 수 구해라.

입력
n, m, s, v 제시. 세로 가로 쥐속 매속
n개 줄 들쥐 x, y 좌표
m개 줄 땅굴 x, y 좌표
소숫점 셋째 자리까지 주어질 수 있다.

출력
잡아먹히게 되는 들쥐 최솟값.
'''
import sys
input = sys.stdin.readline

def matching(idx):
    global m, mx
    for i in range(m):
        if v[i] or dst[idx][i] > mx:
            continue
        v[i] = 1
        if connect[i] < 0 or matching(connect[i]):
            connect[i] = idx
            return True
    return False

n, m, s, v = map(int, input().rstrip().split())
mx = s*v
mic = []
for i in range(n):
    a, b = map(float, input().rstrip().split())
    mic.append((a, b))
hal = []
for i in range(m):
    a, b = map(float, input().rstrip().split())
    hal.append((a, b))

dst = [[] for _ in range(n)]
for i in range(n):
    a, b = mic[i]
    for h, w in hal:
        dst[i].append(((a-h)**2 + (b-w)**2) ** 0.5)

connect = [-1]*m
cnt = 0
for i in range(n):
    v = [0]*m
    if matching(i):
        cnt += 1
    if cnt == m:
        break

print(n-cnt)




