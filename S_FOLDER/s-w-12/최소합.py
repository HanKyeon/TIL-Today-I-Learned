'''
최소합

각 칸에서 오른쪽이나 아래로만 이동 가능. 0,0에서 n-1,n-1까지 이동 할 때 최솟값

입력
테케T
n 제시
그래프

출력
#테케 답
'''
dh = [1, 0]
dw = [0, 1]

def dfs(h, w, num): # 각 칸은 10 이하 자연수
    global n, ans
    if h == n-1 and w == n-1:
        ans = min(ans, num)
        return
    if num + (n-1-h+n-1-w) >= ans:
        return
    for i in range(2):
        nh, nw = h+dh[i], w+dw[i]
        if 0<=nh<n and 0<=nw<n:
            dfs(nh, nw, num+g[nh][nw])

for tc in range(1, int(input())+1):
    n = int(input())
    ans = int(10e9)
    g = [list(map(int, input().rstrip().split())) for _ in range(n)]
    dfs(0, 0, g[0][0])
    print(f"#{tc} {ans}")






