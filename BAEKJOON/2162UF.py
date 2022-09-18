'''
선분 그룹

N개의 선분들이 2차원 평면 상에 주어져 있다. 선분은 양 끝점의 x,y 좌표로 표현.
두 선분이 만나는 경우에, 두 선분은 같은 그룹에 속한다고 정의. 그룹의 크기는 그 그룹에 속한 선분의 갯수로 정의. 두 선분이 만난다 -> 끝점이 만나는 것 포함.
N개의 선분 제시. 몇개의 그룹으로 되어있을까? 또 가장 크기가 큰 그룹에 속한 선분의 갯수는 몇 개일까?

입력
첫째 줄에 1이상 3000이하 n 제시.
x1 y2 x2 y2 제시. 절댓값은 5000 안넘은

출력
그룹의 수, 가장 크기가 큰 그룹에 속한 선분의 갯수. 그냥 최대선분 수?
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
        nodc[a] += nodc[b]
    else:
        parent[a] = b
        nodc[b] += nodc[a]

# 17387에 나오는 선분 교차 알고리즘이라고 한다.........
def ccw(x1, y1, x2, y2, x3, y3):
    tmp = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0

def check(sb1, sb2):
    x1, y1, x2, y2 = sb1
    x3, y3, x4, y4 = sb2
    if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) == 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) == 0:
        if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            return 1

    elif ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0:
        return 1
    return 0

n = int(input())
parent = list(range(n+1))
jp = [[] for _ in range(n+1)]
nodc = [1] * (n+1)

for i in range(1, n+1):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    elif x1 == x2:
        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
    jp[i] = (x1, y1, x2, y2)

for i in range(1, n+1):
    for j in range(i+1, n+1):
        if check(jp[i], jp[j]):
            union(i, j)

gn = 0
for i in range(1, n+1):
    if parent[i] == i:
        gn += 1
ans = max(nodc)
print(gn)
print(ans)

'''
# 파이썬3로 돌아가는 짱빠른 코드

# 2162
import sys


def collide(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    # Step 1
    # check that range of two lines have intersection
    if (x1 if x1 > x2 else x2) < (x3 if x3 < x4 else x4) or (x3 if x3 > x4 else x4) < (x1 if x1 < x2 else x2):
        return False
    if (y1 if y1 > y2 else y2) < (y3 if y3 < y4 else y4) or (y3 if y3 > y4 else y4) < (y1 if y1 < y2 else y2):
        return False
    # Step 2
    # line1 = [x1, y1, x2, y2], line2 = [x3, y3, x4, y4]
    # Linear Equation of line 1 : (y1-y2)X - (x1-x2)Y + (x1*y2 - x2*y1) = 0
    # Matrix Expression of Equations, Ax = b
    # [y2-y1 | -(x2-x1)] [x] = [x1*y2 - x2*y1]
    # [y4-y3 | -(x4-x3)] [y] = [x3*y4 - x4*y3]
    # det A = (x2-x1)*(y4-y3) - (x4-x3)*(y2-y1)
    det = (x2-x1)*(y4-y3) - (x4-x3)*(y2-y1)
    if det != 0:  # two lines are not parallel
        # calculating coordinates of intersection point
        x = ((x2-x1)*(x3*y4-x4*y3) - (x4-x3)*(x1*y2-x2*y1)) / det
        y = ((y2-y1)*(x3*y4-x4*y3) - (y4-y3)*(x1*y2-x2*y1)) / det
        # check that intersection point is in range
        lies_in_xrange = (x-x1)*(x-x2) <= 0 and (x-x3)*(x-x4) <= 0
        lies_in_yrange = (y-y1)*(y-y2) <= 0 and (y-y3)*(y-y4) <= 0
        return True if lies_in_xrange and lies_in_yrange else False
    else:  # two lines are parallel
        return True if (y2-y1)*x3 - (x2-x1)*y3 + (x2*y1-x1*y2) == 0 else False
        # (x3, y3) is on line1. Shortly, line1 and line2 are same.
        # Cause of Step1, we do not have to check the range.

n = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
nbd_ = [[j for j in range(n) if collide(lines[i], lines[j]) and i!= j] for i in range(n)]

group = []
vertices = set([i for i in range(n)])  # using for operation with neighborhood
visited = [False for i in range(n)]
while vertices:
    tmp_group = set([])
    now = vertices.pop()
    tmp_group.add(now)
    visited[now] = True
    to_go = nbd_[now]
    while to_go:
        now = to_go.pop(0)
        vertices.remove(now)
        tmp_group.add(now)
        visited[now] = True
        for nbd in nbd_[now]:
            if not visited[nbd] and nbd not in to_go:
                to_go.append(nbd)
    group.append(tmp_group)

print(len(group))
print(max([len(i) for i in group]))

'''


















