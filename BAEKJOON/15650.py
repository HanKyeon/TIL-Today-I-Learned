'''
N과 M2

n, m이 주어졌을 때 조건을 만족하는 길이가 m인 수열 구해라.
1부터 n까지 자연수 중 중복 없이 m개를 고른 수열.
고른 수열은 오름차순이어야 한다.
'''
def dfs(idx, cnt):
    global n, m
    if cnt == m:
        print(*l)
        return
    for i in range(idx+1, n+1):
        l.append(i)
        dfs(i, cnt+1)
        l.pop()

n, m = map(int, input().rstrip().split())
for i in range(1, n+1):
    l = [i]
    dfs(i, 1)










