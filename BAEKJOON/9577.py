'''
토렌트

파일을 여러개로 나눠 조각을 지닌 시드가 접속하는 시간에 시드로부터 일부 조각을 전송 받아 파일을 완성시킨다. 시드는 자신이 가지고 있는 조각을 자신이 접속 했을 때 다른 사용자에게 배포하는 역할을 한다.
희원이는 n개의 조각으로 나눠진 하나의 파일을 공유 받으려 한다. 각 시드 별 접속 시간과 가지고 있는 조각 정보가 제시되었고, 희원이 외의 다른 사람 조각은 고정되어 있다. 받으려는 파일의 모든 조각을 전송 받을 수 있는 최소의 시간.
시드 별 가지고 있는조각이 다르고 접속하는 시간도 다르다. 하나의 조각을 받는데 1초가 걸린다. 즉 여러 시드로부터 같은 시간에 동시에 받을 수 없다.

입력
테케 T
n, m 제시. 파일 조각 수 / 사람 수
m개 줄 사용자 별 접속 시작 시간, 나가는 시간, 가지고 있는 조각 수, a개 조각의 각각 번호 q 제시.

출력
파일을 다운 받을 수 있는 최소 시간 출력. 더 접속하는 사용자가 없는데 파일을 모두 다운받지 못한 경우에는 -1 출력
'''
import sys
input = sys.stdin.readline
def stdli(x:set):
    x = list(x)
    x.sort()
    return x
def bmatch(x):
    for i in g[x]:
        if v[i]:
            continue
        v[i] = 1
        if not connect[i] or bmatch(connect[i]):
            connect[i] = x
            return True
    return False

for _ in range(int(input())):
    n, m = map(int, input().rstrip().split())
    g = [set() for _ in range(n+1)]
    mt = 0
    for i in range(1,m+1):
        s = list(map(int, input().rstrip().split()))
        t1, t2, a = s.pop(0), s.pop(0), s.pop(0)
        if mt < t2:
            mt = t2
        for j in s:
            g[j].update(set(range(t1,t2)))
    g = list(map(stdli, g))
    connect = [0]*mt
    ans = 0
    for i in range(1, n+1):
        v = [0]*mt
        if bmatch(i):
            ans += 1
    if ans == n:
        prt = -1
        for i, v in enumerate(connect):
            if v:
                prt = i
        print(prt+1)
    else:
        print(-1)

'''
3
3 2
1 3 1 1
0 3 3 1 2 3
5 3
1 3 2 5 3
2 10 3 2 3 4
9 11 1 1
3 3
0 100 3 1 2 3
0 100 3 1 2 3
0 100 3 1 2 3
'''











