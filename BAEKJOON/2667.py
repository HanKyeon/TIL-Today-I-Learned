'''
단지 번호 붙이기
'''
import sys
# 입력
n = int(input())
g = [[] for _ in range(n)]
for i in range(n) :
    g[i] = list(map(int, list((sys.stdin.readline().rstrip()))))
# x, y 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(gr, xy) :
    for i in range(n) :
        for j in range(n) :

