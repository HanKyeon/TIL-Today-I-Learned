'''
열혈강호

직원이 n명, 해야 할 일 m개.
직원이 1~n 일도 1~m
각 직원은 한개의 일만 가능.
각각 일을 담당하는 사람은 1명이어야 한다.
m개 일 중 최대 몇개 가능?

입력
n, m 제시.
n개 줄 i번 직원이 할 수 있는 일의 갯수, 할 수 있는 일의 번호 제시.
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1111)

def matching(idx):
    for i in g[idx]:
        if v[i]:
            continue
        v[i] = 1
        if not connect[i] or matching(connect[i]):
            connect[i] = idx
            return 1
    return 0

n, m = map(int, input().rstrip().split())
g = [[]]
for _ in range(n):
    s = list(map(int, input().rstrip().split()))
    s.pop(0)
    g.append(s)
connect = [0]*(m+1)
for i in range(1, n+1):
    v = [0]*(m+1)
    matching(i)
print(m+1-connect.count(0))

'''
# 빠른 코두

import sys

def main():
    def dfs(visit, node):
        if visit[node] == 1:
            return 0
    
        visit[node] = 1
    
        for key in employee[node]:
            if ans[key] == 0:
                ans[key] = node
                return 1
    
        for key in employee[node]:
            if dfs(visit, ans[key]):
                ans[key] = node
                return 1
    
        return 0
    
    n, m = map(int, sys.stdin.readline().split())
    employee, ans = [[] for _ in range(n + 1)], [0] * (m + 1)
    
    for i in range(1, n + 1):
        temp = list(map(int, sys.stdin.readline().split()))
        for item in temp[1:]:
            employee[i].append(item)
    
    cnt = 0
    for i in range(1, n + 1):
        visit = [0] * (n + 1)
        if dfs(visit, i):
            cnt += 1
    
        if cnt == m:
            break
    
    print(cnt)

if __name__=="__main__":
    main()
'''