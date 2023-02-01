'''
불우이웃돕기

집 랜선이 많아서 기부 할 것이다.
집에 n개의 방. 방에는 컴이 있다. 랜으로 연결. n개 컴 전부 연결.
기부 할 수 있는 랜선 길이 최댓값.

입력
컴 갯수 n
랜선 길이
i, j의 문자가 0인 경우 컴퓨터 i와 j를 연결하는 랜선이 없음을 의미. 그외의 경우 랜선 길이.
a to z 1부터 26, A to Z 27부터 52

출력
기부 할 수 있는 랜선 길이의 최댓값 출력. 모든 컴이 연결 안되어 있담녀 -1 출력
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n = int(input())
parent = list(range(n))
egs = []
for i in range(n):
    s = list(input().rstrip())
    for j in range(n):
        a = ord(s[j])
        if a == 48:
            continue
        elif 96 < a < 123:
            a -= 96
        else:
            a -= 38
        heappush(egs, (a, i, j))

ans, cnt = 0, 0
while egs:
    cost, i, j = heappop(egs)
    ri, rj = find(i), find(j)
    if ri == rj:
        ans += cost
        continue
    cnt += 1
    union(ri, rj)
if cnt!= n-1:
    ans = -1
print(ans)













