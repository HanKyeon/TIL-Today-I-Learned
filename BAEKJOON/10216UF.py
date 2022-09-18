'''
Count Circle Groups

2차원 평면 위의 N곳에 적군 진영이 설치되어 있다.
하나의 통신탑을 설치해 i번째 적군의 통신탑은 설치 위치로부터 Ri 이내 거리에 포함되는 모든 지역을 사진의 통신 영역 Ai로 가지게 된다. 임의의 통신 영역 Ai와 Aj가 닿거나 겹치는 부분이 있다면 진영 i와 j는 직접적으로 통신이 가능하다. 물론 직접 통신 아니라 돌려가도 가능하다.
상호 통신 가능한 경우 한 그룹이다. 그룹 수를 알아내야 한다.

입력
테케T
적군 진영 수 n 1이상 3000이하
적군 진영 좌표0이상 5000이하 x y, 해당 진영의 R 제시. 모두 정수

출력
적군 진영 그룹 갯수 출력
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a, b = find(x), find(y)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def check(info1, info2):
    x1, y1, r1 = info1
    x2, y2, r2 = info2
    dst =((x1-x2)**2 + (y1-y2)**2)
    if dst <= (r1+r2)**2:
        return True
    return False

for _ in range(int(input())):
    n = int(input())
    parent = list(range(n+1))
    nod = [() for _ in range(n+1)]
    for i in range(1, n+1):
        x, y, r = map(int, input().rstrip().split())
        nod[i] = (x, y, r)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if find(i) == find(j):
                continue
            if check(nod[i], nod[j]):
                union(i, j)
    ans = 0
    for i in range(1, n+1):
        if i == parent[i]:
            ans +=1
    print(ans)


'''
# 빠른 코드

import sys
input = sys.stdin.readline
g_cnt = 0


def find(x):
    if parent[x] == -1:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False

    if height[a] < height[b]:
        a, b = b, a
    parent[b] = a

    if height[a] == height[b]:
        height[a] += 1
    return True


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        V = int(input())
        parent = [-1 for _ in range(V)]
        height = [0 for _ in range(V)]

        pos_x = list()
        pos_y = list()
        rads = list()
        for i in range(V):
            y, x, r = map(int, input().rstrip().split())
            pos_x.append(x)
            pos_y.append(y)
            rads.append(r)

        g_cnt = V
        for i in range(V):
            for j in range(i):
                if (pos_x[i] - pos_x[j]) ** 2 + (pos_y[i] - pos_y[j]) ** 2 <= (rads[i] + rads[j]) ** 2:
                    if union(i, j):
                        g_cnt -= 1
        print(g_cnt)
'''


















