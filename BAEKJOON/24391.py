'''
귀찮은 해강이

1번부터 n번까지 n개의 강의
강의코드와 동일한 번호의 건물에서 진행. 강의코드가 1이면 1번 건물, n-1이면 n-1 건물에서 진행.
한 건물에서 밖으로 나와서 다른 건물로 이동ㅎ는 횟수 최소화.
강의 시간표 제시, 최소 몇 번 만 밖에 나오면 되는가? 처음 안센다.

입력
강의 갯수 n, 연결된 건물 쌍의 갯수 m
m개줄 i, j 제시. i와 j 연결.
n개 강의 코드로 이루어진 강의 시간표 공백으로 출력.

출력
밖에 나와야 하는 최소 횟수 출력.
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

n, m = map(int, input().rstrip().split())
parent = list(range(n+1))
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    a, b = find(a), find(b)
    if a == b:
        continue
    union(a, b)
nl = list(map(int, input().rstrip().split()))
root = find(nl[0])
cnt = 0
for i in nl:
    nroot = find(i)
    if root == nroot:
        continue
    cnt += 1
    root = nroot
print(cnt)

















