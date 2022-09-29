'''
고인물이 싫어요

마을에 n개의 물탱크 m개의 파이프로 연결.
k번 물탱크에 방문 했을 때, k번 물탱크와 k번 물탱크에서 0개 이상의 파이프를 거쳐 이용한 물탱크 중, 청정수가 담긴 물탱크의 수가 고인물이 담긴 물탱크의 수보다 더 많은 경우 청정수를 얻을 수 있다.
방문 할 예정인 물탱크에 대한 정보가 주어질 때마다 청정수 가능한지 구하자.

입력
물탱크의 수 n, 파이프 수 m, 방문 횟수 q 제시.
1번부터 n번 물탱크까지 순서대로 들어있는 물의 종류 제시. 청정수1 고인물 0
m개 줄에 파이프가 연결하는 두 물탱크의 번호 u, v 제시. 같은 물탱크를 연결하는 파이프 여러개 존재 가능.
q개 줄 방문 할 물탱크 번호 제시.
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 금지
    rx, ry = find(x), find(y)
    if rx == ry:
        return
    if rx < ry:
        parent[ry] = rx
        nodc[rx] += nodc[ry]
        sts[rx] += sts[ry]
    else:
        parent[rx] = ry
        nodc[ry] += nodc[rx]
        sts[ry] += sts[rx]

n, m, qst = map(int, input().rstrip().split())
parent = list(range(n+1))
sts = [0]+list(map(int, input().rstrip().split()))
nodc = [1]*(n+1)
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    union(a, b)

for _ in range(qst):
    a = int(input())
    a = find(a)
    if sts[a] > nodc[a]-sts[a]:
        print(1)
    else:
        print(0)








