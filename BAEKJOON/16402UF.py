'''
제국

왕국과 속국.
전쟁 승리 시 왕국과 그 속국은 전부 승리 왕국의 속국으로 복속. 속국 쳐도 왕국 전쟁.
속국이 자신의 종주국 공격 가능. 속국이 승리 시 종주국이랑 속국 먹는다. 근데 지면 아무일도 없는.
왕국의 이름과 두 왕국의 전쟁 결과들이 주어질 때, 모든 전쟁이 끝난 후 속국이 아닌 왕국들의 수와 속국이 아닌 각 왕국의 이름을 출력하라.

입력
왕국의 수 n, 전쟁의 수 m / 2이상 500이하, 1이상 2000이하
왕국이름 제시. 왕국의 이름은 항상 Kingdom of로 시작, 뒤는 공백 없는 하나의 단어. 이름 총 길이 20이하. 중복x
m개줄에 전쟁 결과 제시.
왕국 1이름, 왕국2이름, w가 공백 없이 ,로 구분되어 제시. w가 1이면 왕국1 승리, w가 2면 왕국2 승리.

출력
속국이 아닌 왕국의 수
속국이 아닌 왕국의 이름을 아스키 사전 순으로 정렬하여 한 줄에 하나씩 출력.
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b, w):
    if w == '1':
        parent[b] = a
        parent[a] = a
    else:
        parent[a] = b
        parent[b] = b

n, m = map(int, input().rstrip().split())
parent = {}
for _ in range(n):
    s = input().rstrip()
    parent[s] = s

for _ in range(m):
    a, b, w = input().rstrip().split(',')
    ra, rb = find(a), find(b)
    if w == '1':
        if parent[a] == b:
            parent[a] = a
        if parent[a] != a and parent[a] != b:
            a = parent[a]
        if parent[b] != b and parent[b] != a:
            b = parent[b]
        parent[b] = a
        for i in parent.keys():
            if parent[i] == b:
                parent[i] = a
    else:
        if parent[b] == a:
            parent[b] = b
        if parent[a] != a and parent[a] !=b:
            a = parent[a]
        if parent[b] != b and parent[b] != a:
            b = parent[b]
        parent[a] = b
        for i in parent.keys():
            if parent[i] == a:
                parent[i] = b


ans = []
for i in parent.keys():
    if find(i) == i:
        ans.append(i)

print(str(len(ans)))
# print('\n')
for i in sorted(ans):
    print(i)
    # print('\n')



'''
# 빠름

import sys
getline = sys.stdin.readline

def find(link: list, u: int) -> int:
    if link[u] < 0: return u
    link[u] = find(link, link[u])
    return link[u]

def union(link: list, u: int, v: int): # u win
    r1, r2 = find(link, u), find(link, v)
    if r1 != r2:
        link[r1] += link[r2]
        link[r2] = r1
    elif r1 != u:
        link[u] = link[v]
        link[v] = u


N, M = map(int, getline().split())
link = [-1]*N
idx = {getline().rstrip():i for i in range(N)}
names = list(idx.keys())

for _ in range(M):
    king1, king2, winner = getline().rstrip().split(',')
    if winner == '1': union(link, idx[king1], idx[king2])
    else: union(link, idx[king2], idx[king1])

winners = [i for i in range(N) if link[i] < 0]
print(len(winners))
print('\n'.join(sorted(names[i] for i in winners)))
'''
'''
# 얘도 빠름
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

n, m = map(int, sys.stdin.readline().split())
kingdom = dict()
parent = list(range(n))

for i in range(n):
    string = sys.stdin.readline().rstrip('\n')
    kingdom[string] = i

for i in range(m):
    a, b, w = sys.stdin.readline().rstrip('\n').split(',')
    if w == '1':
        if find_parent(parent, kingdom[a]) == find_parent(parent, kingdom[b]):
            if parent[kingdom[b]] == kingdom[b]:
                kingdom[a], kingdom[b] = kingdom[b], kingdom[a]
        else:
            parent[find_parent(parent, kingdom[b])] = find_parent(parent, kingdom[a])
    else:
        if find_parent(parent, kingdom[a]) == find_parent(parent, kingdom[b]):
            if parent[kingdom[a]] == kingdom[a]:
                kingdom[a], kingdom[b] = kingdom[b], kingdom[a]
        else:
            parent[find_parent(parent, kingdom[a])] = find_parent(parent, kingdom[b])

li = []
for i in kingdom:
    if parent[kingdom[i]] == kingdom[i]:
        li.append(i)
li.sort()

print(len(li))
for i in li:
    print(i)
'''










