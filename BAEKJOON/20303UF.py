'''
할로윈의 양아치

스브러스는 늦게 일어나서 사탕을 뺏을 것이다.
한 명 까면 친구 사탕도 모조리 빼앗는다.
k명 이상의 아이들이 울기 시작하면 온 집의 어른들이 거리로 나온다.
스브러스가 들키지 않고 최대로 뺏을 수 있는 사탕의 양을 구해라.

입력
n,m,k 제시. 애들 수, 친구 관계수, 울음소리 최소 애들 수
받은 사탕 리스트 제시.
m개에 걸쳐 a, b 제시. a와 b가 친구임을 의미.

출력
들키지 않고 최대한 뺏을 수 있는 사탕의 수
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
        cdl[x] += cdl[y]
        cnt[x] += cnt[y]
    else:
        parent[x] = y
        cdl[y] += cdl[x]
        cnt[y] += cnt[x]

def knapsack(li):
    global k
    dp, ndp = [0]*(k+1), [0]*(k+1)
    while li:
        cdy, num = li.pop()
        for i in range(k+1-num):
            ndp[i+num] = max(dp[i]+cdy, dp[i+num])
        dp = ndp[:]
    return dp[k-1]

n, m, k = map(int, input().rstrip().split())
cdl = [0]+list(map(int, input().rstrip().split()))
cnt = [1]*(n+1)
parent = [i for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    a, b = find(a), find(b)
    if a==b:
        continue
    union(a, b)
fl = []
for i in range(1, n+1):
    if parent[i] == i:
        fl.append((cdl[i], cnt[i]))

print(knapsack(fl))




'''
1 3 : 4 9 / 13 2
2 5 6 10 : 15 1 5 5 / 26 4
4 9 : 4 20 / 24 2
7 8 ": 19 14 / 33 2
'''











