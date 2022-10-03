'''
소셜 네트워킹 어플리케이션

친구 관계 그래프를 그릴 수 있다.
유저 수와 각 유저의 친구 관계 제시.
두 사람이 친구 관계 그래프 상에서 경로가 존재하는지 안하는지 구하시오.

입력
테케
유저수 친구관계수 n, m 제시.
m개 줄에 a, b 제시. a와 b가 친구.
구할 쌍의 수 m 제시.
구해야 하는 쌍의 수 u, v 제시

출력
Scenario i: i는 테케
1 경로 존재
0 경로 없음

'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): #find해서
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def check(x, y): # find 안해서
    return 1 if find(x) == find(y) else 0

for tc in range(1, int(input())+1):
    n, m = int(input()), int(input())
    parent = list(range(n+1))
    for _ in range(m):
        a, b = map(int, input().rstrip().split())
        a, b = find(a), find(b)
        if a == b:
            continue
        union(a, b)
    k = int(input())
    print(f"Scenario {tc}:")
    for _ in range(k):
        a, b = map(int, input().rstrip().split())
        print(check(a, b))
    print()





