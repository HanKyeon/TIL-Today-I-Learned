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
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

def dfs(num): # dfs해서 dli에 추가하는 것.
    v[num]=1
    for i in g[num]:
        if v[i] == 0:
            dli.append(i)
            dfs((i))

n = int(input())
v = [0]*(n+1) # 방문 여부
numn = [0]*(n+1) # 갈 수 있는 노드 갯수
nodv = [0] + list(map(int, input().rstrip().split())) # 인구 수 
g = [set() for _ in range(n+1)] # 그래프
for i in range(1, n+1):
    nl = list(map(int, input().rstrip().split()))
    for j in range(len(nl)):
        if j == 0:
            numn[i]= nl[j]
        else:
            g[i].add(nl[j])
            g[nl[j]].add(i)

parts = [] # 쪼개진 부분 여부 확인
for i in range(1, n+1):
    if v[i] == 0:
        dli = [i]
        dfs(i)
        parts.append(dli)

# print(g)
# print(parts)

if len(parts) >= 3:
    print(-1)
elif len(parts) == 2:
    sumli1 = sum([nodv[i] for i in parts[0]])
    sumli2 = sum([nodv[i] for i in parts[1]])
    print(abs(sumli1-sumli2))
elif len(parts) == 1:
    nods = parts[0] # 하나로 묶인 노드 번호들
    ans = int(10e9)
    for i in range(1, n//2+1):
        sets = set(nods)
        for j in combinations(nods, i):
            # 첫번째 묶음 유효성 점검
            q = deque([j[0]]) # 큐에 하나만 넣기
            sets1 = set(j) # 비교군 세트
            oks = set([j[0]]) # 방문처리 확인. 넣어서 확인 할 세트
            sum1 = 0 # 첫번째 리스트 합
            while q: # 한 노드에 대해 bfs해서
                num = q.popleft()
                sum1 += nodv[num] # 합에 추가
                for nno in g[num]: # 노드 순환하며
                    if not nno in oks and nno in sets1: # 방문 해야 하는데 방문처리 안했으면
                        q.append(nno) # 방문
                        oks.add(nno) # 방문처리
            if sets1 != oks: # 비교군과 방문처리가 다르다면 다음 조합
                continue

            # 나머지 노드들에 대해 마찬가지로 점검
            sets2 = set(nods) # 다른 묶음 노드
            for k in j:
                sets2.remove(k)
            j2 = list(sets2) # bfs를 위해 리스트화
            # 아래로는 위와 동일
            q = deque([j2[0]])
            oks2 = set([j2[0]])
            sum2 = 0
            while q:
                num = q.popleft()
                sum2 += nodv[num]
                for nno in g[num]:
                    if not nno in oks2 and nno in sets2:
                        q.append(nno)
                        oks2.add(nno)
            if sets2 != oks2:
                continue
            # print(sets1, sets2, abs(sum1-sum2))
            ans = min(ans, abs(sum1-sum2)) # 다 뚫고 오면 갱신
        
    print(ans) # 출력




            
            





'''
def dfs(num):
    v[num]=1
    for i in g[num]:
        if v[i] == 0:
            dfs((i))

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
print(part, parts)
if len(parts) >= 3:
    print(-1)
else:
    pass
'''


'''
def bfs(lil): # 리스트 길이 받아서 반환 할 것
    pass

n = int(input())
v = [0]*(n+1) # 방문 여부
numn = [0]*(n+1) # 갈 수 있는 노드 갯수
nodv = [0] + list(map(int, input().rstrip().split())) # 인구 수 
g = [set() for _ in range(n+1)] # 그래프
for i in range(1, n+1):
    nl = list(map(int, input().rstrip().split()))
    for j in range(len(nl)):
        if j == 0:
            numn[i]= nl[j]
        else:
            g[i].add(nl[j])
            g[nl[j]].add(i)

print(v)
print(numn)
print(nodv)
print(g)


'''






