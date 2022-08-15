'''
바이러스

bfs로 해야지

컴퓨터 수 100이하 번호는 1부터 매김
연결된 컴퓨터 쌍의 수.
그 수만큼 직접 연결된 컴터ㅡㄷㄹ
'''
def bfs(num):
    # visited의 합 반환해야 한다.
    li = [num]
    while li:
        now = li.pop(0)
        v[now] = 1
        for j in g[now]:
            if v[j] == 0 :
                li.append(j)
    return sum(v)

n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
v = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b) # 테케 그지같이 주면 안되므로 내가 다 받아야 한다.
    g[b].append(a)
print(bfs(1)-1)

