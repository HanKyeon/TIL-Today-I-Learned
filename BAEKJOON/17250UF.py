'''
은하철도

은하가 행성으로 가드캐. 은하 철도가 개설될 때마다 몇개의 행성들이 서로 여행 할 수 있게 되는가?

입력
은하 수 n, 철도 수 m 2이상 10만이하 1이상 10만이하
n줄에 각 은하 내에 존재하는 행성들의 수가 1번 은하부터 차례로 제시. 행성 수 단위는 조
m줄에 은하철도 제시. 같은 은하 사이에 여러 철도 없음.

출력
연결 될 때마다 '해당 철도'를 이용 할 수 있는 행성들의 수 출력
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x < y:
        parent[y] = x
        cnt[x] += cnt[y]
    else:
        parent[x] = y
        cnt[y] += cnt[x]

n, m = map(int, input().rstrip().split())
parent = [i for i in range(n+1)]
cnt = [0]+[int(input().rstrip()) for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    a, b = find(a), find(b)
    if a == b:
        print(cnt[a])
        continue
    union(a, b)
    if a < b:
        print(cnt[a])
    else:
        print(cnt[b])




