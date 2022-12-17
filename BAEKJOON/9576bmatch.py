'''
책 나눠주기

n권의 책. 1~n번
학부생 m명
m개 줄 a, b 제시
a이상 b 이하인 책 중 남아있는 책 한 권을 골라 그 학생에게 제시.
a~b까지 모든 책을 이미 다른 학생에게 주고 없다면 책 안준다.
책 줄 수 있는 최대 학생 수는?
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1111)

def matching(idx):
    mi, ma = g[idx]
    for i in range(mi, ma+1):
        if v[i]:
            continue
        v[i] = 1
        if not connect[i] or matching(connect[i]):
            connect[i] = idx
            return True
    return False

for _ in range(int(input())):
    n, m = map(int, input().rstrip().split())
    g = [[]]
    for i in range(1, m+1):
        a, b = map(int, input().rstrip().split())
        g.append((a, b))
    connect = [0] * (n+1)
    for i in range(1, m+1):
        v = [0] * (n+1)
        a, b = g[i]
        matching(i)
    print(len(connect)-connect.count(0))






