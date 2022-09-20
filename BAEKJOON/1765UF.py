'''
닭싸움 팀 정하기

누가 우리 편이고 누가 남의 편인지 알아야 한다. 평소 학생 인간관계에 따라 정리 가능.
1. 친구 친구는 친구
2. 원수 원수는 친구
이 때 두 학생이 친구이면 같은 팀, 같은 팀 끼리는 전부 친구.
인간관계 제시, 얼마나 많은 팀이 생기는가?

입력
학생수 n 제시. 2이상 1000이하 1부터 n번호
인간관계 중 알려진 것 m 1이상 5000이하
인간관계 F p q 혹은 E p q 제시.
F는 p랑 q 친구
E는 p랑 q 원수.
친구이면서 원수 없음.

출력
첫째 줄에, 가능한 최대 팀 갯수 출력.
'''
'''
원수가 문젠데..
원수의 원수를 연결하는데 둘이 원수인지 확인해야 하지 않나?
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 해서 넣기
    if x < y:
        parent[y] = parent[x]
    else:
        parent[x] = parent[y]

n, m = int(input()), int(input())
parent = list(range(n+1))
frnz, wonsu = [], [[] for _ in range(n+1)]
for _ in range(m):
    p, a, b = input().rstrip().split()
    a, b = int(a), int(b)
    if p == 'E':
        wonsu[a].append(b)
        wonsu[b].append(a)
    else:
        union(a, b)
for i in wonsu:
    if not i:
        continue
    leni = len(i)
    if leni < 2:
        continue
    for j in range(leni-1):
        for k in range(j+1, leni):
            pj, pk = find(i[j]), find(i[k])
            if pj == pk:
                continue
            union(pj, pk)
ans = 0
for i in range(1, n+1):
    if parent[i] == i:
        ans += 1
# print(f"parent : {parent}")
# print(f"wonsu : {wonsu}")
print(ans)



'''
# 빠른 코드

import sys
from sys import stdin

sys.setrecursionlimit(5000000)

class DisjointSet:
    def __init__(self, N):
        self.group = [i for i in range(N)]
        
    def find(self, n):
        if self.group[n] == n:
            return n
        self.group[n] = self.find(self.group[n])
        return self.group[n]

    def merge(self, p, q):
        p = self.find(p)
        q = self.find(q)

        if p is not q:
            self.group[p] = q

def main():
    n = int(stdin.readline())
    m = int(stdin.readline())

    f_dsj = DisjointSet(n+1)
    enemy = [0 for _ in range(n+1)]

    for _ in range(m):
        rel = stdin.readline().split()
        r, p, q = rel[0], int(rel[1]), int(rel[2])
        if r == 'F':
            f_dsj.merge(p, q)
        else:
            if enemy[p]:
                f_dsj.merge(enemy[p], q)
            if enemy[q]:
                f_dsj.merge(p, enemy[q])
            
            enemy[p] = q
            enemy[q] = p
    
    num_group = 0

    for i in range(1, n+1):
        if f_dsj.group[i] == i:
            num_group += 1
    
    print(num_group)

if __name__ == '__main__':
    main()
'''









