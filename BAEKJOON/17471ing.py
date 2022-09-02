'''
게리맨더링

연결 된 도시 인구차 최소로 만들어서 출력.

입력
구역의 갯수 n 1번부터 n번까지 제시 2이상 10이하
구역의 인구가 n개까지 한줄로 공백 구분
각 구역에 인접한 구역의 정보 제공.
구역과 인접한 구역의 수, 인접한 구역의 번호들 정수 공백 구분
A와 B가 인접이라면 B도 A에 인접.

출력
두 선거구 인구 차이의 최솟값. 선거구가 두 개로 나눠지지 않으면 -1 출력
'''
import sys
input = sys.stdin.readline

def dfs(num):
    v[num]=1
    for i in g[num]:
        if v[i] == 0:
            dfs(i)

n = int(input())
v = [0]*(n+1)
nod = [0]*(n+1)
pp = [0] + list(map(int, input().rstrip().split()))
g = [set() for _ in range(n+1)]
for i in range(1, n+1):
    nl = list(map(int, input().rstrip().split()))
    for j in range(len(nl)):
        if j == 0:
            nod[i]= nl[j]
        else:
            g[i].add(nl[j])
            g[nl[j]].add(i)
part = 0
parts = []
for i in range(1, n+1):
    if v[i] == 0:
        dfs(i)
        part += 1
        if not parts:
            parts.append(sum(v))
        else:
            parts.append(sum(v) - parts[-1])
if len(parts) >= 3:
    print(-1)
else:



















