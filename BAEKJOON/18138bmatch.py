'''
리유나는 세일러복을 좋아해

하얀 티샤쓰와 세일러 카라를 더해서 만든다
흰 티의 너비를 w라 할 때, 너비가 w/2 이상 w*3/4 이하인 세일러 카라를 붙일 수 있다. 혹은 w이상 w*5/4 이하인 카라를 붙일 수 있다.
최대 몇 개나 만들 수 있는가?

입력
n, m 제시. 티/카라
n개 줄 흰 티 너비 w
m개 줄 카라 너비 w 제시
w는 모두 정수.

출력
만들 수 있는 세일러 복 갯수의 최댓값
'''
import sys
input = sys.stdin.readline

def matching(x):
    for i in g[x]:
        if v[i]:
            continue
        v[i] = 1
        if not connect[i] or matching(connect[i]):
            connect[i] = x
            return True
    return False

n, m = map(int, input().rstrip().split())
g, tr = [[] for _ in range(n+1)], [[]]
for _ in range(n):
    w = int(input())
    tr.append((w/2, w*3/4, w, w*5/4))

for i in range(1,m+1):
    w = int(input())
    for j in range(1, n+1):
        a,b,c,d = tr[j]
        if a<=w<=b or c<=w<=d:
            g[j].append(i)

ans = 0
connect = [0]*(m+1)
for i in range(1,n+1):
    v = [0]*(m+1)
    if matching(i):
        ans += 1

print(ans)












