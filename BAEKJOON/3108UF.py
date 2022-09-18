'''
로고

거북이 그리기.
연필을 떼는 명령을 몇 번 하는가?
그려야 하는 직사각형은 x1, y1, x2, y2 형태로 제시.

입력
직사각형 갯수 n 1이상 1000이하

출력
N개 직사각형을 전부 그리는데 필요한 PU 명령의 최솟값.
'''
'''
직사각형 교차 여부에 따라 T F 반환해서 union 해주면 될듯?
1000개면 좀 많은데 find(i) find(j+1)로 받아서 애초부터 루트를 합쳐주는 방식으로 union을 진행하자.
1,000,000 1순회 당 100만번 연산이라 생각보다 빡빡하네 메모리도 작고.

PU 연산 횟수는
(0,0)이 직사각형 그룹 내에 있는가를 판단해야 하고,
(0, 0)이 그룹 내에 있을 경우 그룹갯수 -1
그룹에 없을 경우 그룹 갯수 그대로.
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find로 넣자.
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def check2(num1, num2):
    x1, y1, x2, y2 = bxz[num1]
    a1, b1, a2, b2 = bxz[num2]
    # 사각형이 겹치는 경우
    if x1 <= a2 and x2 >= a1 and y1 <= b2 and y2 >= b1:
        # 아예 포함 되는 경우
        if (x1 < a1 and x2 > a2 and y1 < b1 and y2 > b2) or (x1 > a1 and x2 < a2 and y1 > b1 and y2 < b2):
            return False
        return True
    return False

n = int(input())
parent = list(range(n+1))
bxz = [[] for _ in range(n+1)]
ans, fla = 0, False
for i in range(1, n+1):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    # 좌하단 -> 우상단 좌표로 변환
    x1, y1, x2, y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    bxz[i] = [x1, y1, x2, y2]
    # 0, 0을 지나는 곳이 있나 미리 체크
    if fla:
        continue
    elif not fla and ((x1*x2 == 0 and y1*y2 <= 0) or (y1*y2 == 0 and x1 * x2 <= 0)):
        fla = True
        ans -= 1

for i in range(1, n):
    for j in range(i+1, n+1):
        a = find(i)
        b = find(j)
        if a == b:
            continue
        if check2(bxz[i], bxz[j]):
            union(a, b)

for i in range(1, n+1):
    if parent[i] == i:
        ans += 1

print(ans)


def check(num1, num2): # 얘가 틀렸다고 하네. 확인해보자.
    x1, y1, x2, y2 = bxz[num1]
    a1, b1, a2, b2 = bxz[num2]
    if a1 < x1: # x1이 무조건 왼쪽으로 설정.
        x1, y1, x2, y2, a1, b1, a2, b2 = a1, b1, a2, b2, x1, y1, x2, y2

    if y1 > b2: # ab 사각 형 기준 11시 방향에서 시작점이 잡히면 안됨
        return False
    elif b1 <= y1 <= b2: # ab 사각형 기준 9시에 위치해있다면
        if a1 <= x2: # 우상단 점의 x좌표가 넘어가면 겹친다.
            return True
        return False
    elif y1 < b1: # ab 사각형 기준 7시라면
        if a1 <= x2 <= a2 and y2 >= b1: # ab 사각형 12시 쪽으로 점이 있거나
            return True
        if x2 >= a1 and b1 <= y2 <= b2: # ab 사각형 3시 쪽으로 점이 있어야 한다.
            return True
        return False






'''
쫌 더 빠름

import sys

input = sys.stdin.readline


def sol3108():
    n = int(input())
    squares = [[0, 0, 0, 0]]
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        squares.append([x1, y1, x2, y2])

    u = [-1] * (n + 1)

    # 사각형 i가 이전 사각형과 변이 겹치는지 체크
    # 겹칠 경우 두 사각형은 연필을 내린채로 한번에 그릴 수 있음
    for i in range(1, n+1):
        # 현재 사각형
        sx1, sy1, sx2, sy2 = squares[i]

        for j in range(i):
            # j 사각형과 겹친다면 union
            if check(squares[i], squares[j]):
                union(u, i, j)

    answer = 0
    for i in range(n+1):
        if u[i] < 0:
            answer += 1

    return answer - 1


def check(a, b):
    # 사각형이 겹치는 경우
    if a[0] <= b[2] and a[2] >= b[0] and a[1] <= b[3] and a[3] >= b[1]:
        
        # 아예 포함 되는 경우
        if (a[0] < b[0] and a[2] > b[2] and a[1] < b[1] and a[3] > b[3]) or (a[0] > b[0] and a[2] < b[2] and a[1] > b[1] and a[3] < b[3]):
            
            return False
        
        return True
    
    return False


def union(u, x, y):
    x = find(u, x)
    y = find(u, y)
    if x != y:
        if u[x] < u[y]:
            u[x] += u[y]
            u[y] = x
        else:
            u[y] += u[x]
            u[x] = y


def find(u, x):
    if u[x] < 0:
        return x
    u[x] = find(u, u[x])
    return u[x]


if __name__ == '__main__':
    print(sol3108())
'''













