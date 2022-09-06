'''
파티

N개 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.

N명의 학생이 1이상 N이하 x번 마을에 모여서 파티를 벌이기로 했다.
마을 사이에는 총 M개의 단방향 도로들. i번째 길을 지나오는데 Ti의 시간 소비.
각각의 학생들은 파이테 참석하기 위해 걸어가서 그들의 마을로 돌아와야 한다.
최단시간에 오고가기를 원한다.
도로는 단방향. 오고 가는 길이 다를 수 있다.
가장 많은 시간을 소비하는 학생은?

입력
1이상 1000이하 n, m 제시 1이상 n이하 x 제시.
시작 끝 시간 제시.
정당한 데이터만 제시.

출력
n명의 학생 중 오고 가는데 가장 오래 걸리는 학생의 소요시간 출력
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

# 빠르게 하려면 x에서 각 집에 가는 거리는 한 번 구해두고 가져다 쓰면 될 것 같다.

def dij(sta, end):
    global n
    dst = [int(10e9)] * (n+1)
    heap = [(0, sta)]
    dst[sta] = 0
    while heap:
        sumc, now = heappop(heap)
        if dst[now] < sumc:
            continue
        for i in g[now]:
            co, nod = i
            cost = sumc + co
            if cost < dst[nod]:
                dst[nod] = cost
                heappush(heap, (cost, nod))
    return dst[end]

n, m, x = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c= map(int, input().rstrip().split())
    g[a].append((c, b))
sumd = [0] * (n+1)
for i in range(1, n+1):
    sumd[i] += dij(i, x) + dij(x, i)

print(max(sumd))




'''
# 빠른 코드

import sys

I= sys.stdin.readline

n,m,x = map(int,I().split())


house_a = [[] for i in range(n)]
house_d = [[] for i in range(n)]
cost1 = [0]*n
cost2 = [0]*n



for i in range(m):
    tmp = list(map(int,I().split()))
    house_a[tmp[0]-1].append([tmp[1]-1,tmp[2]])
    house_d[tmp[1]-1].append([tmp[0]-1,tmp[2]])
    
#print(house_a)
#print(house_d)
    

def opt(house,cost):
    stacks = [x-1]
    while stacks:
        #print("----------------")
        #print(stacks)
        #print(house)
        #print(cost)
        
        p = stacks.pop()
        for i in house[p]:
            if i[1] + cost[p] < cost[i[0]] or cost[i[0]] == 0:
                cost[i[0]] = i[1]+cost[p]
                stacks.insert(0,i[0])
    cost[x-1] = 0
    return cost


min_a = opt(house_a,cost1)
min_d = opt(house_d,cost2)
result = 0
for i in range(len(min_a)):
    if (min_a[i] + min_d[i]) > result:
        result = min_a[i] + min_d[i]


print(result)
'''