'''
돌 그룹

3개 그룹.
돌을 움직이며, 크기가 다른 두 그룹을 골라서 큰 쪽에서 작은쪽에 작은 쪽의 수만큼 더해준다.
돌을 같은 갯수로 만들 수 있으면 1을, 아니면 0을 출력해라.
'''
import sys
from collections import deque
input = sys.stdin.readline

def gogo(n1, n2):
    if n1 < n2:
        return n1*2, n2-n1
    if n1 > n2:
        return n1-n2, n2*2

def lego(n1, n2, n3):
    if n1==n2==n3:
        return 1
    q = deque([(n1,n2,n3)])
    while q:
        n1, n2, n3 = q.popleft()
        if n1==n2==n3:
            return 1
        if n1 != n2:
            a, b = gogo(n1, n2)
            if not (a, b, n3) in v:
                v.add((a, b, n3))
                q.append((a, b, n3))
        if n1 != n3:
            a, c = gogo(n1, n3)
            if not (a, n2, c) in v:
                v.add((a, n2, c))
                q.append((a, n2, c))
        if n2 != n3:
            b, c = gogo(n2, n3)
            if not (n1, b, c) in v:
                v.add((n1, b, c))
                q.append((n1, b, c))
    return 0

a, b, c = map(int, input().rstrip().split())
v = {(a, b, c)}
print(lego(a,b,c))







