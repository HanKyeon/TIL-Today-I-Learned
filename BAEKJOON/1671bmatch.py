'''
상어의 저녁식사

어떤 상어는 저녁식사로 서로를 먹는다. 모든 상어는 자신과 다른 상어의 크기, 속도, 지능을 수치로 나타낸 것을 알고 있다. A의 크기 속도 지능이 상어 B의 크기 속도 지능보다 크거나 같다면 잡아먹을 수 있다.
한 상어가 최대 두개의 상어만 먹을 수 있다.
죽은 상어는 다른 상어들을 잡아먹을 수 없다.
N마리 상어의 크기 속도 지능이 주어졌을 때, 살아남을 수 있는 상어 수의 최솟값.

입력
상어 마릿수 n 50이하 자연수
n개 상어 크기 속도 지으 정보 제시.

출력
살아남을 수 있는 상어 수의 최솟값 출력
'''
import sys
input = sys.stdin.readline

def matching(idx):
    if v[idx]:
        return False
    v[idx] = 1
    for i in g[idx]:
        if not connect[i] or matching(connect[i]):
            connect[i] = idx
            return True
    return False

n = int(input())
sha = [[]]
for i in range(1, n+1):
    sha.append(list(map(int, input().rstrip().split())))
g = [[] for _ in range(n+1)]
connect = [0]*(n+1)
for i in range(1, n+1):
    i1,i2,i3 = sha[i]
    for j in range(i+1, n+1):
        if i == j:
            continue
        j1,j2,j3 = sha[j]
        if i1 < j1 and i2 <= j2 and i3 <= j3:
            g[j].append(i)
        elif i1 <= j1 and i2 < j2 and i3 <= j3:
            g[j].append(i)
        elif i1 <= j1 and i2 <= j2 and i3 < j3:
            g[j].append(i)
        elif i1 >= j1 and i2 >= j2 and i3 >= j3:
            g[i].append(j)

ans = 0
for i in range(1, n+1):
    v = [0]*(n+1)
    if matching(i):
        ans += 1
for i in range(1, n+1):
    v = [0]*(n+1)
    if matching(i):
        ans += 1

print(n-ans)

