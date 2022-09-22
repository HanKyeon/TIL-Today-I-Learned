'''
전자카트

사무실에서 출발해 각 구역을 한 번 씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량.
각 구역을 이동 할 때의 배터리 사용량은 표로 제공
1번은 사무실, 2번부터 n번 관리 구역 번호.
'''
def dfs(sta, val):
    global n, ans
    # print(v)
    if len(v) == n-1:
        ans = min(ans, val+g[sta][0])
        return
    
    if val + n-1-len(v) >= ans:
        return
    
    for i in range(1, n):
        if i in v:
            continue
        v.add(i)
        dfs(i, val + g[sta][i])
        v.remove(i)

for tc in range(1, int(input())+1):
    n = int(input())
    g = [list(map(int, input().rstrip().split())) for _ in range(n)]
    ans = int(10e9)
    v = set()
    for i in range(1, n):
        v.add(i)
        dfs(i, g[0][i])
        v.remove(i)
    print(f"#{tc} {ans}")























