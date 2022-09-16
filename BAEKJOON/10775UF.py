'''
공항

공항에 G개의 게이트 1에서 G의 번호.
P개의 비행기가 서순으로 도착.
i번째 비행기를 gi 번째 게이트 중 하나에 영구 도킹해야함.
뱅기가 어느 게이트에도 도킹 불가능하다면 공항 폐쇄.
가장 많은 비행기 도킹 가능?

입력
게이트 수 제시. 1이상 10만
뱅기 수 제시. 1~10만
P개 줄에 gi 제시. 뱅기 번호대로인듯?

출력
도킹 가능한 최대 뱅기 수
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a, b = find(x), find(y)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

gnum, pnum = int(input()), int(input())
parent = list(range(gnum+1))
ans = 0
fla = False
for i in range(1, pnum+1):
    gi = int(input())
    if fla: continue
    fgi = find(gi)
    if fgi == 0:
        fla = True
        continue
    union(fgi, fgi-1)
    ans += 1
print(ans)

'''
1. 브루트 포스로 풀었다.
2. union-find로도 풀 수 있다. find로만 풀 수 있다는게 정확한 말인듯?
'''












'''
# 36퍼 시간 초과

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

gnum, pnum = int(input()), int(input())
v = [0] * (gnum+1)
ans = 0
for i in range(1, pnum+1):
    gi = int(input())
    fla = True
    while 0 < gi:
        if v[gi]:
            gi -= 1
            continue
        v[gi] = 1
        ans += 1
        fla = False
        break
    if fla:
        break
print(ans)
'''



