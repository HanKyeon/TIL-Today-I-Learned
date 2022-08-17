
def dfs(num):
    print(num, end=' ')
    v[num] = 1
    for i in g[num]:
        if v[i] == 0:
            dfs(i)

def dfs2(num):
    st = [num]
    while st:
        n = st.pop()
        if v[n] == 0:
            print(n, end=' ')
            v[n] = 1
            for i in reversed(g[n]):
                if v[i] == 0:
                    st.append(i)
        else : continue

for testcase in  range(1, int(input())+1):
    n, l = map(int, input().split())
    v = [0] * (n+1)
    g = [[] for _ in range(n+1)]
    for _ in range(l):
        st, en = map(int, input().split())
        g[st].append(en)
        g[en].append(st)
    g = list(map(sorted, g))
    print(f"#{testcase}", end=' ')
    dfs2(1)
    print()



