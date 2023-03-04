'''
최애 정하기

최애 멤버를 정할 것이다. 같은 멤버를 좋아하는 것은 안된다. 이분매칭 해라. 단, 좋아하는 사람은 단 한 명만 가능하다.

입력
사람 수 n, 걸 그룹 수 m 제시.
m개 줄 걸그룹 멤버 이름 제시. 영문 대문자로만 제시, 최대 길이 100글자.
n개 줄 좋아하는 멤버 수 k, 좋아하는 멤버 이름 제시.

출력
우정 지킬 수 있으면 YES, 없다면 최대한 겹치지 않게 친구들 전체가 좋아할 수 있는 최대 멤버 수 출력.
'''
import sys
input = sys.stdin.readline

def matching(idx):
    for i in g[idx]:
        if v[i]:
            continue
        v[i] = 1
        if not connect[i] or matching(connect[i]):
            connect[i] = idx
            return True
    return False

n, m = map(int, input().rstrip().split())
ps = {}
for i in range(1, m+1):
    a = input().rstrip()
    ps[a] = i
g = [[]]
for _ in range(n):
    a = list(input().rstrip().split())
    a.pop(0)
    s = []
    for i in a:
        s.append(ps[i])
    g.append(s)
connect = [0]*(m+1)
cnt = 0
for i in range(1, n+1):
    v = [0]*(m+1)
    if matching(i):
        cnt += 1

if cnt == n:
    print("YES")
    exit()
else:
    print("NO")
    print(cnt)



