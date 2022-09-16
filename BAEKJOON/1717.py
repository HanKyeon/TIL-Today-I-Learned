'''
집합의 표현

집합 이루고 있다.
합집합 연산과 두 원소가 같은 집합에 포함되어 있는지 확인할 것.

입력
n, m 제시. 100만이하 10만이하 양수 m은 입력 갯수
합집합은 0, a, b
1, a, b는 a과 b의 루트가 같은지 확인.
a, b는 음이 아닌 정수

출력
1로 시작하는 입력에 대해 한 줄에 하나씩 YES NO 출력 yes no 가능
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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

def check(x, y):
    return find(x) == find(y)

n, m = map(int, input().rstrip().split())
parent = list(range(n+1))

for _ in range(m):
    ysz, nod1, nod2 = map(int, input().rstrip().split())
    if ysz:
        if check(nod1, nod2):
            print("YES")
        else:
            print("NO")
    else:
        union(nod1, nod2)










