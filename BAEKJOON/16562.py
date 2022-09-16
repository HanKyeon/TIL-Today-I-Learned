'''
친구비

19학번 이준석은 학생이 n명인 학교에 입학. 모든 학생과 친구가 되길 원함.
학생 i에게 ai만큼 돈을 주면 1달간 친구.
준석이는 k원이 있다.
친구의 친구는 친구다.
가장 적은 비용으로 모든 사람과 친구가 되는 법은?

입력
학생수 n 1이상 1만이하, 관계수 m 1이상 1만이하, 돈k 1이상 천만이하
학생번호i 원하는 친구비 ai 제시. n개 줄
v, w. 학생 v와 학생 w가 친구라는 뜻. m개 줄 지가 지 일 수 있고 같은 친구가 여러번 있을 수 있음.
'''
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a, b = find(x), find(y)
    if a==b:
        return
    if a < b:
        parent[b] = a
        count[a] += count[b]
    else:
        parent[a] = b
        count[b] += count[a]

n, m, k = map(int, input().rstrip().split())
mny = [0] + list(map(int, input().rstrip().split()))

parent = list(range(n+1))
count = [1]*(n+1)
val = [[] for _ in range(n+1)]
for _ in range(m):
    v, w = map(int, input().rstrip().split())
    union(v, w)
for i in range(1, n+1):
    a = find(parent[i])
    heappush(val[a], mny[i])
ans = 0
for i in val:
    if i:
        ans += heappop(i)

if ans > k:
    ans = 'Oh no'
print(ans)









