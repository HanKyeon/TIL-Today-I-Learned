'''
사이클 게임

선이 홀수 후가 짝수
0~n-1 고유 번호 부여된 점 n개 제시. 어떤 세 점도 일직선에 있지 않다.
매 차례 플레이어는 두 점 선택해서 도로 놓기. 원래 있던거 추가 불가.
사이클 생기면 게임 끝.

사이클이란
C에 속한 임의의 선분의 한 끝점에서 출발하여 모든 선분을 한 번씩만 지나서 출발점으로 되돌아올 수 있다.

사이클 여부 판단 및 게임 진행중인지 아닌지 확인. 몇 번째에 사이클이 완성 되었는지

입력
점의 갯수 3이상 50만이하 n, 진행된 차례 3이상 100만이하 m
i번째 차례에 해당 플레이어가 선택한 두 점의 번호 제시.

출력
표준 출력. m번째 차례까지 진행 한 상황에서 게임이 종료되었다면 사이클이 처음 만들어진 차례의 번호를 양정수로 출력 m번 차례를 모두 처리했는데 안끝났으면 0 출력
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def check(x, y):
    return find(x) == find(y)

def union(x, y):
    a, b = find(x), find(y)
    if a == b: return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().rstrip().split())
parent = list(range(n))
ans = 0
for i in range(1, m+1):
    a, b = map(int, input().rstrip().split())
    if ans: continue
    if check(a, b):
        ans = i
    else:
        union(a, b)
print(ans)


















