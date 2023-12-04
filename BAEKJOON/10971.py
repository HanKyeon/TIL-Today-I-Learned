'''
외판원 순회 2

TSP 문제. 1~n까지 번호, 길 존재. 한 도시에서 출발해 n개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획할 것. 한 번 들르면 못간다. 가장 적은 비용을 들이는 여행 계획.
각 이동 비용은 행영 w[i][j] 형태로 제시. 양방향 가격 다를 수 있음.
갈 수 없다면 0임.
n과 비용행렬 제시, 가장 적은 비용을 들이는 외판원 순회 여행 경로를 구해라.

입력
n 제시
n개 줄 비용 제시

출력
최소 비용 출력
'''
def check(cost: int, nod: int):
    global n, ans
    if cost >= ans: return
    if len(stk) == n:
        if not g[nod][stk[0]]: return
        nco = cost+g[nod][stk[0]]
        if nco < ans: ans = nco
        return

    for i in range(n):
        if v[i] or not g[nod][i]: continue
        v[i]=1; stk.append(i)
        check(cost+g[nod][i], i)
        v[i]=0; stk.pop()

n = int(input())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
v = [0]*n
stk, ans = [], 11111111

for i in range(n): v[i]=1; stk.append(i); check(0, i); v[i]=0; stk.pop()
print(ans)