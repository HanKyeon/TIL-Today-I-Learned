'''
열혈 강호

n명의 직원 m개의 일.
한 개의 일
할 수 있는 일의 목록과 지급해야 하는 월급 제시. m개 일 중 최대 몇개 가능하고 얼마 내야 하는지.

입력
n, m 제시.
n개 줄 일의 갯수와 일의 번호, 그 일을 할 때 지급해야 하는 월급 제시.
'''
import sys
input= sys.stdin.readline

def matching(idx):
    for i, co in g[idx]:
        if v[i]:
            continue
        v[i] = 1
        if cost[i] > co:
            if cost[i] == 10001:
                cost[i] = co
                connect[i] = idx
                return True
            nidx = connect[i]
            cost[i] = co
            connect[i] = idx
            matching(nidx)
            return True
        if not connect[i] or matching(connect[i]):
            cost[i] = co
            connect[i] = idx
            return True
    return False

n, m = map(int, input().rstrip().split())
g = [[]]
for i in range(n):
    s = list(map(int, input().rstrip().split()))
    ap = []
    a = s.pop(0)
    for i in range(a):
        b, c = s[i*2], s[i*2+1]
        ap.append((b, c))
    g.append(ap)

connect = [0]*(m+1)
cost = [10001]*(m+1)
ans = 0
for i in range(1, n+1):
    v = [0]*(m+1)
    if matching(i):
        ans += 1
def jr(val):
    if val == 10001:
        return 0
    return val
print(m-connect.count(0)+1)
print(sum(map(jr, cost)))








