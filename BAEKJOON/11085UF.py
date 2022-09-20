'''
군사 이동

백준월드 큐브월드.
p개 지점과 w개의 길. 양방향, 너비.
경로상의 너비가 가장 좁은 길을 최대화.

입력
p, w 제시. 2이상 1000이하, 1이상 5만이하.
백준월드 수도, 큐브월드 수도 제시. c, v
w줄에 길이 연결하는 두 지점과 너비가 공백 제시.

출력
너비가 가장 좁은 길의 너비 출력
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 한 값
    if x < y:
        parent[y] = x
        widcnt[x] = min(widcnt[x], widcnt[y])
        return x
    else:
        parent[x] = y
        widcnt[y] = min(widcnt[x], widcnt[y])
        return y

p, w = map(int, input().rstrip().split())
sta, end = map(int, input().rstrip().split())
parent = list(range(p+1))
widcnt = [int(10e9)] * (p+1)
heap = []
for _ in range(w):
    nod1, nod2, wid = map(int, input().rstrip().split())
    heappush(heap, (-wid, nod1, nod2))

while heap:
    if find(sta) == find(end):
        break
    wid, nod1, nod2 = heappop(heap)
    nod1, nod2 = find(nod1), find(nod2)
    if nod1 == nod2:
        continue
    root = union(nod1, nod2)
    widcnt[root] = min(widcnt[root], -wid)

sta = find(sta)
if widcnt[sta] == int(10e9):
    widcnt[sta] = 0
print(widcnt[find(sta)])
















