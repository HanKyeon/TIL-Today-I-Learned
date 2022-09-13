'''
텀 프로젝트

텀 프로젝트 수행. 팀원 수 제한x 한 팀만 있을 수 있음. 팀에 한 명만 있을 수도 있음.
학생들이(s1, s2, ..., sr)이라 할 때, r=1이고 s1이 s1을 선택하는 경우나, s1이 s2를 선택하고, s2가 s3를 선택하고,..., sr-1이 sr을 선택하고, sr이 s1을 선택하는 경우에만 한 팀이 될 수 있다. dfs로 팀을 고른다.

어느 팀에도 속하지 않는 학생들의 수를 계산하는 프로그램을 작성하라.

입력
테케T
학생 수가 정수 n으로 제시. 2이상 10만이하.
각 테케 둘째 줄에는 선택된 학생들의 번호 제시. 1부터 n까지 번호 부여.
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# 정답은 정답이나 최적 정답이 아닌듯? 메모리 초과.
def dfs(nidx, sta, num):
    global n, li
    if nidx == sta:
        n -= num
        while li:
            x = li.pop()
            v[x] = 0
        return
    if nidx in li:
        return
    if v[nl[nidx]]:
        li.append(nidx)
        dfs(nl[nidx], sta, num+1)


for _ in range(int(input())):
    n = int(input())
    nl = [0] + list(map(int, input().rstrip().split()))
    v = [1] * (n+1)
    for i in range(1, n+1):
        li = [i]
        if v[i]:
            dfs(nl[i], i, 1)
    print(n)





'''
def dfs(idx):
    sta.append(idx)
    if v[nl[idx]] == 0:
        v[nl[idx]] = 1
        dfs(nl[idx])
    elif v[nl[idx]] == 1:
        fla = False
        while sta:
            a = sta.pop()
            if a != nl[idx] and not fla:
                v[a] = 2
            elif a == nl[idx]: # nl[idx]는 시작점이자 도착점 이므로 flag를 True로 돌려줌. 나머지는 다 못만드는 친구들.
                v[a] = 2
                fla = True
            else:
                v[a] = -1
    else:
        while sta:
            a = sta.pop()
            v[a] = -1

for _ in range(int(input())):
    n = int(sys.stdin.readline())
    nl = [0] + list(map(int, input().rstrip().split()))
    v = [0 for _ in range(n+1)]
    sta = []
    for i in range(1, n+1):
        if v[i] == 0:
            v[i] = 1
            dfs(i)
    ans = 0
    for i in v:
        if i == -1:
            ans += 1
    print(ans)
'''



























