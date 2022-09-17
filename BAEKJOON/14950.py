'''
정복자

N개의 도시와 M개의 도로. 양방향 도로. 비용.
시작은 1번. B를 점령하고 싶다면 도로의 비용이 소모. 점령하면 t만큼 비용 증가.
최소비용 정복

입력
n, m, t 제시. 도시갯수n, 도로개수m, 증가비용t 제시.
n은 1만이하 m은 3만이하 t는 10이하 자연수.
a, b, c 제시. a에서 b로가는데 c 코스트. c는 1만이하

출력
최소 비용
'''
'''
# 20220918
백준 : 14950 9489
 14950 : UF 문제가 아니라 최소 스패닝 트리 문제인데, UF로 풀린다. ez
 9489 : 내가 맞다. 예외처리 빠짐없이 했고, 어떤 자료가 와도 레벨로 나눈 트리 구조가 무너지지 않는다. 10새들
'''

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 해서 넣기
    if x < y:
        parent[y] = x
        nodc[x] += nodc[y]
    else:
        parent[x] = y
        nodc[y] += nodc[x]

n, m, t = map(int, input().rstrip().split())
parent = list(range(n+1))
nodc = [1]*(n+1)
ans = int((n-2)*(n-1)//2) * t
heap = []
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    heappush(heap, (c, a, b))

while nodc[1] != n:
    c, a, b = heappop(heap)
    a, b = find(a), find(b)
    if find(a) == find(b):
        continue
    union(a, b)
    ans += c

if n == 1:
    ans = 0

print(ans)


'''
t 증가량 얼마나?
1. 도시 하나 점령 : t 안더해짐
2. 2개 점령 : t하나
3. 3개 점령. t하나 + t2
4. 4개 점령. 1 2 3
5. 5개 점령. 1 2 3 4
n-1까지의 합.
(n-1)(n-2)//2
(1+n-2)*2
'''






