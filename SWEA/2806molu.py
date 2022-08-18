'''
N-Queen

8*8 체스에 8개 퀸을 서로 공격 못하게 하는 방식으로

N*N에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수는?

입력
테케T
자연수N 1이상 10이하

출력
#T 퀸 배치 가능 경우의 수
'''

def check(i, col):
    global answer
    n = len(col)-1
    if promising(i, col) :
        if i == n:
            answer += 1
        else:
            for j in range(1, n+1):
                col[i+j] = j
                check(i+1, col)

def promising(i, col):
    for k in range(1, i):
        if col[i] == col[k] or abs(col[i]-col[k]) == i-k:
            return False
    return True

def solution(n):
    global answer
    answer = 0
    col = [0] * (n+1)
    check(0, col)
    return answer

for t in range(1, int(input())+1):
    solution(int(input()))








'''
def queen(h, w):
    global n
    for i in range(n):
        a, b, c, d = h-i, w-i, h+i, w+i
        for j in range(n):
            if i == h or j == w:
                g[i][j] += 1
        if 0<=a<n and 0<=b<n:
            g[a][b] += 1
        elif 0<=a<n and 0<=d<n:
            g[a][d] += 1
        elif 0<=c<n and 0<=d<n:
            g[c][d] += 1
        elif 0<=c<n and 0<=b<n:
            g[c][b] += 1


for testcase in range(1, int(input())+1):
    n = int(input())
    g = [[0]*n for _ in range(n)]
    for i in range(n):
        if not (0 in g[i]):
            continue
        for j in range(n):
            queen(i, j)
'''
