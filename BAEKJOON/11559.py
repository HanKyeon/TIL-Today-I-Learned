'''
뿌요뿌요

필드에 여러가지 뿌요 놓기. 아래 바닥이나 다른 뿌요가 나올 때까지 아래로 하강.
뿌요를 놓은 뒤 같은 색 뿌요가 상하좌우로 연결되어 있다면 연결된 같은 색 뿌요들이 아작난다. 1연쇄 시작.
다른 뿌요들이 떨어지고, 또 4개 이상 모이면 터지며 연쇄.
여러 그룹이 동시에 터질 수 있으며, 여러 그룹이 동시에 터지는 것은 1연쇄다.
연쇄가 최대 몇 번 연속ㅇ로 일어날지 예측.

입력
12개 줄에 필드 정보. 6개 보유. 즉 12/6 필드
.은 빈 공간 R빨 G초 B파 P보 Y노
필드는 뿌요들이 전부 아래로 떨어진 뒤의 상태.

출력
현재 주어진 상황에서 몇연쇄가 되는지 출력한다. 하나도 안터지면 0
'''
from collections import deque
import sys
input = sys.stdin.readline

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

def 뿌요(h, w, val):
    li = [(h, w)]
    q = deque([(h, w)])
    while q:
        h, w = q.popleft()
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<6 and 0<=nw<12 and s[nh][nw] == val and not v[nh][nw]:
                v[nh][nw] = 1
                q.append((nh, nw))
                li.append((nh, nw))
    if len(li) >= 4:
        while li:
            h, w = li.pop()
            s[h][w] = '.'
        return True
    return False

def 뭐요():
    for i in range(6):
        for j in range(11, -1, -1):
            if s[i][j] != '.':
                이동(i, j)

def 이동(h, w):
    nw = w+1
    if nw<12 and s[h][nw] == '.':
        s[h][w], s[h][nw] = s[h][nw], s[h][w]
        이동(h, nw)

g = [list(input().rstrip()) for _ in range(12)]
s = list(map(list, zip(*g))) # 전치 행렬로 하는게 편할듯?
ans = 0

for i in s:
    print(i)
print('===')
while True:
    fla = False
    v = [[0]*12 for _ in range(6)]
    for i in range(6):
        for j in range(12):
            if s[i][j] == '.' or v[i][j]:
                continue
            v[i][j] = 1
            a = 뿌요(i, j, s[i][j])
            if fla:
                continue
            if a:
                fla = a
    뭐요()

    for i in s:
        print(i)
    print('===')

    if fla:
        ans+=1
    else:
        break
print(ans)












