'''
피자 오븐

n분간 오븐 동작 예정. 버튼 동작은 아래와같이 5가지.
ADDH: $t' = t + 60$
ADDT: $t' = t + 10$
MINT: $t' = t - 10$
ADDO: $t' = t + 1$
MINO: $t' = t - 1$
버튼 최소 횟수로 누를 것이다. 설정해야 할 시간이 주어졌을 때, 그 시간을 만들기 위해 눌러야 하는 버튼의 최소 횟수와 그 방법을 구해라.

입력
T개 테케.
N분 제시

출력
각 테케마다 5개의 정수를 한 줄에 공백 구분 출력. ADDH, ADDT, MINT, ADDO, MINO 버튼 누르는 횟수 출력.
최소 횟수를 누르는 방법이 여러가지인 경우 사전순으로 가장 앞서는 방법 출력.
ADDH, ADDT, MINT, ADDO, MINO 순이다.
'''
import sys
from collections import deque
input = sys.stdin.readline

def lego(target):
    btns = [0]*5
    s, t, o = target//60, (target % 60)//10, target%10
    if o > 5:
        t+=1
        o-=10
    if t > 3:
        s+=1
        t-=6
    if t < 0 and o == 5:
        t+=1
        o-=10
    btns[0] = s
    btns[2-(t >= 0)] = abs(t)
    btns[4-(o >= 0)] = abs(o)
    return btns

for _ in range(int(input())):
    print(*lego(int(input())))

'''
# 실패한 코드 : 시간 제한 보고 풀이 생각해보자.
mov = [60, 10, -10, 1, -1]
def lego(target):
    v = [0] + [11111111]*(target+60)
    q = deque([(0, [0, 0, 0, 0, 0], 0)])
    while q:
        cnt, btns, cost = q.popleft()
        if v[cost] < cnt:
            continue
        for i in range(4, -1, -1):
            co = mov[i]
            costco = cost+co
            if 0<=costco<=target+60 and v[costco] > cnt+1:
                v[costco] = cnt+1
                btns[i] += 1
                if costco == target:
                    return btns
                q.append((cnt+1, btns[:], costco))
                btns[i] -= 1

for _ in range(int(input())):
    print(*lego(int(input())))
'''
