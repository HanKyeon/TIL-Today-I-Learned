'''
거짓말

아는 사람 있으면 진실 모르는 사람만 있으면 구라
다른 파티에서 만나서 들어도 구라쟁이인게 걸린다!

입력
사람 수 n 파티 수 m
진실을 아는 사람 수 번호 1~n 연속 제시
각 파티마다 오는 사람의 수와 번호가 같은 방식으로 제시.
n , m은 50이하 자연수 진실 아는 사람 수는 0이상 50이하 각 파티마다 오는 사람의 수는 1이상 50이하 정수

출력
정답 출력
'''
from collections import deque
import sys
input=sys.stdin.readline

n, m = map(int, input().split())
cant = list(map(int, input().rstrip().split()))
sets = []
if len(cant) == 1: # 0명 예외처리
    for _ in range(m):
        x = input()
    print(m)
else: # 1이상
    v = [0]*(n+1) # 방문처리
    cant = set(cant[1:]) # 거짓말 못치는 사람들
    for i in cant:
        v[i] = 1 # 선 방문처리
    g = [set() for _ in range(n+1)] # 그래프. 간선
    moims = [] # 모임들
    for _ in range(m):
        s = list(map(int, input().rstrip().split()))
        l = s.pop(0)
        moims.append(set(s)) # 모임들에 파티 참여 멤버들 넣어줌
        for i in range(l):
            for j in range(i, l):
                # 간선 추가. 서로 이어져 있으면 얘기 할 수 없음.
                g[s[i]].add(s[j])
                g[s[j]].add(s[i])
    q = deque() # bfs 할 거임
    for i in cant: # 0인거 합체
        q.append(i)
    while q:
        c = q.popleft()
        for i in g[c]:
            if v[i] == 0:
                v[i] = 1
                q.append(i)
    vs = [i for i, v in enumerate(v) if v == 0] # 거짓말 칠 수 있는 사람들
    vs.pop(0) # 0 빼기
    del v
    del g
    vs = set(vs)
    # moims
    ans = 0
    for i in moims: # 모임들이 순수한 사람들의 부분집합 이라면. 이건 아예 콤비네이션 써도 됐을듯?
        if i.issubset(vs):
            ans += 1 # 정답 추가.
    print(ans)




'''
# 잘못된 접근
    ans = 0
    g = set(g[1:])
    ppl = set()
    for i in range(1, n+1):
        if i in g:
            continue
        ppl.add(i)
    for i in range(m):
        s = list(map(int, input().rstrip().split()))
        s.pop(0)
        s = set(s)
        fla = False
        for j in g:
            if j in s:
                fla = True
                break
        if fla:
            while s:
                a = s.pop()
                if a in ppl:
                    ppl.remove(a)
                g.add(a)
        else:
            sets.append(s)
    print(sets)
    for i in sets:
        print(i, 'i입니다.')
        if i.issubset(ppl):
            ans += 1
    print(ppl)
    print(ans)
'''
'''
# 빠른 코드
input = sys.stdin.readline

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b, knowTrue):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a in knowTrue and b in knowTrue:
        return 
    
    if a in knowTrue: #만약 a가 아는 사람일 경우 해당 파티의 부모 노드는 a로 지정함
        parent[b] = a
    elif b in knowTrue:
        parent[a] = b 
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
 
N, M = map(int, input().split())

knowTrue = list(map(int, input().split()))
parent = [0] * (N+1)
for i in range(N+1):
    parent[i] = i

for i in range(1, knowTrue[0]):
    union_parent(parent, knowTrue[i], knowTrue[i+1], knowTrue)
knowTrue = knowTrue[1:]

parties = []
result = 0
for _ in range(M):
    party = list(map(int, input().split()))
    for i in range(1, party[0]):
        union_parent(parent, party[i], party[i+1], knowTrue) #각 멤버를 묶음
    parties.append(party)

#모든 파티를 체크 후에 과장함.
for party in parties: #파티를 확인함.  
    for i in range(1, party[0]+1):
        if find_parent(parent, party[i]) in knowTrue:
            break
    else:   
        result += 1

print(result)
'''


