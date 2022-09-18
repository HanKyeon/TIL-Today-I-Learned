'''
회의 준비

참석자와 참석자 간 관계를 따져 하나 이상의 위원회를 구성 하려 한다.

1. 서로 알고 있는 사람은 반드시 같은 위원회.
2. 위원회의 수는 최대가 되어야 함.

이 방식으로 위원회 구성 후 각 위원회의 대표를 한 명씩 뽑아야 한다.
대표만이 회의 시간 중 발언권을 가진다. 그래서 여러 사람을 거쳐 의견을 전달해야 하는데, 의견을 전달하는 경로가 여러개 있을 경우 가장 적은 사람을 거치는 경로로 의견을 전달하며, 이 때 거치는 사람의 수를 참석자의 의사 전달 시간이라고 한다.

의사 전달 시간 중 최댓값이 최소가 되도록 하는 대표를 정하는 프로그램 작성.

1, 2, 3이 1-2, 2-3으로 연결되어 있다면 1이 대표라면 2가 1 3이 2이므로 합이3. 따라서 대표가 2가 되면 1이 1 3이 1이므로 대표는 3이 되어야 한다.

입력
회의 참석자 수 n. 1이상 100이하.
관계 수 m.
아는 사이 2개 제시.

출력
두성되는 위원회의 갯수 k.
대표 번호를 작은 수부터 한 줄에 하나씩 출력. 한 그룹 내 대표가 될 수 있는 사람이 둘 이상일 경우 그 중 한 명만 출력.
'''
'''
거리 상 중앙 값을 구해야 하는데
거리 값으로 유니온을 구현 해줘야 하능감?

부모1 자식2 자식3 자식4 자식5 자식6 자식7
이렇게 있을 때   
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find된 값을 받자.
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = int(input()), int(input())
parent = list(range(n+1))
fw = [[int(10e9)]*(n+1) for _ in range(n+1)]
# 플루이드 워셜 자기 자신 0으로 초기화
for i in range(1, n+1):
    fw[i][i] = 0
# 입력 받으면서 유니온도 해준다.
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    fw[a][b], fw[b][a] = 1, 1
    union(find(a), find(b))
# 플루이드 와샬
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            fw[i][j] = min(fw[i][j], fw[i][k] + fw[k][j])
# 10e9 값 0으로 변경. 그냥 n+1하고 덧셈해서 크기 비교 해도 될듯? 없어도 되는 과정.
for i in range(n+1):
    for j in range(n+1):
        if fw[i][j] == int(10e9):
            fw[i][j] = 0

# 그룹
grp = [[] for _ in range(n+1)]
# 부모 그룹에 최대 거리랑 idx 추가
for i in range(1, n+1):
    heappush(grp[find(i)], (max(fw[i]), i))

cnt = 0
ans = []
for i in grp:
    if i: # 그룹이 존재하면
        cnt+=1 # 그룹 수 하나 늘리고
        heappush(ans, (i[0][1])) # 그룹 대표 ans에 넣기

# 출력
print(cnt)
while ans:
    print(heappop(ans))







'''
in : 
6 3
1 6
6 5
3 4

answer : 
3
2
3 (or 4)
6
'''





