'''
ABCDE

총 n명 참가중.
0부터 n-1번으로 번호.
조건 만족하는 ABCDE 존재하는지 구하려 한다. 5명 사이클이 존재하면 1 없으면0

입력
n, m 제시.
m개 줄 a,b 제시 a, b 친구.

출력
a,b,c,d,e 존재하면 1 없으면 0
'''
import sys
input = sys.stdin.readline

def dfs(idx):
    global ans
    if ans:
        return 1
    if len(li) == 5:
        ans = 1
        return 1
    for i in g[idx]:
        if v[i]:
            continue
        v[i] = 1
        li.append(i)
        dfs(i)
        li.pop()
        v[i] = 0
        if ans:
            break
    return ans

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    g[a].append(b)
    g[b].append(a)
v = [0]*n
ans, li = 0, []
for i in range(n):
    li.append(i)
    v[i] = 1
    ans = dfs(i)
    li.pop()
    v[i] = 0
    if ans:
        break
print(ans)
