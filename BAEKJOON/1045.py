'''
도로

0 to n-1 도시, 도로. 도로엔 우선순위.
a b가 x로 연결, c d 가 y로 연결일 때 a,b < c,d 이면 x의 우선순위가 더 높다.
ai != bi인 가장 작은 양정수 i에 대해 ai < bi면 ai<bi 면 (a1,...,ak) < (b1,...,bk)로 정의한다.
도로의 집합은 하나 이상의 도로가 우선순위에 대한 내림차순으로 정렬되어 있는 것이다.
집합 사이에도 우선순위가 있는데, 두 집합을 튜플로 나타냈을 때의 우선순위를 따른다. 한 집합에 있는 도로만으로 임의의 도시에서 임의의 도시로 이동 가능 할 때 연결되어있다고 한다.
m개의 도로를 가진 도로 집합 중 연결되어 있으면서 우선순위가 가장 높은 것을 찾는 것.

입력
n, m 제시. n은 50이하 자연수 m은 n-1이상 1000이하.
n개 줄 행렬 제시. i,j존재 시 Y 없으면 X. i와 j가 연결되어있으면 j와 i는 연결.

출력
정답 없을 시 -1 출력. 존재한다면 0을 끝 점으로 갖는 도로 갯수, 1을 끝점으로 갖는 도로 갯수, n-1을 끝점으로 갖는 도로 갯수를 차례로 출력
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().rstrip().split())
parent = list(range(n))
egs = []
for i in range(n):
    s = input().rstrip()
    for j in range(i+1, n):
        if s[j] == "Y":
            egs.append((i, j))
if m < n-1 or len(egs) < m:
    print(-1)
    exit()
ans = [0]*n
cnt = 0
trashCount = m-n+1
for i, j in egs:
    if not trashCount and cnt == n-1:
        break
    ri, rj = find(i), find(j)
    if ri == rj:
        if trashCount:
            ans[i] += 1
            ans[j] += 1
            trashCount -= 1
        continue
    union(ri, rj)
    cnt += 1
    ans[i] += 1
    ans[j] += 1
if not trashCount and cnt == n-1:
    print(*ans)
else:
    print(-1)


