'''
로봇 조립

로봇 조립 할 것이다. 여러 부품 섞여있다.
호재는 어떤 로봇 부품인지 안다. 호재 지시 따라 정리한다.
부품들은 1부터 10만까지의 정수. 서로 다른 로봇은 공통 부품을 가지지 않는다.

1. 서로 다른 부품 2개를 말하면 두 부품은 같은 로봇의 부품이라는 정보 제시.
2. 부품 i에 대해 지금까지 알아낸 로봇i의 부품이 몇개냐고 물어본다.

초기에는 부품에 대한 정보가 존재하지 않는다.

입력
호재 지시 횟수 n
부품 둘이 같은건지 알려줄 때는 I a b 같은 로봇의 부품이라는 얘기.
어떤 로봇의 부품이 몇 개인지 물어볼 때는 Q c 형태. 지금까지 알아낸 로봇c의 부품이 몇개냐는 의미.

출력
Q로 시작하는 입력에 대해 한 줄에 하나씩 지금까지 알아낸 해당 로봇의 부품 갯수 출력
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 된 상태
    if x < y:
        parent[y] = x
        nodc[x] += nodc[y]
    else:
        parent[x] = y
        nodc[y] += nodc[x]

n = int(input())
parent = list(range(1000001))
nodc = [1]*(1000001)
for _ in range(n):
    s = input().rstrip().split()
    if len(s) == 3:
        j, a, b = s
        a, b = find(int(a)), find(int(b))
        if a == b:
            continue
        union(a, b)
        continue
    j, c = s
    print(nodc[find(int(c))])




















