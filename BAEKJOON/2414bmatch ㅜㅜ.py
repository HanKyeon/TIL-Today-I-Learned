'''
게시판 구멍 막기

n*m 게시판에 빵꾸 있다.
테이프 길이는 무한, 끊어내는 횟수 최소화.
빵꾸 꿇려있지 않은 부분을 막아서는 안된다.
. 구멍이 없는 부분
* 구멍이 있는 부분

입력
n, m 제시
n개 줄 게시판 제시.

출력
테이프 끊는 횟수 최솟값
'''
import sys
input = sys.stdin.readline

def matching(idx):
    global vc
    if v[idx]:
        return False
    v[idx] = 1
    for i in g[idx]:
        if connect[i] < 0 or matching(connect[i]):
            connect[i] = vc
            return True
    return False

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n)]
gg = [[] for _ in range(m)]
for i in range(n):
    s = list(input().rstrip())
    for j in range(m):
        if s[j] == '*':
            g[i].append(j)
            gg[j].append(i)

ans = 0
connect = [-1] * n
vc = 0
for i in range(n):
    v = [0] * n
    if matching(i):
        vc+=1


print(connect)
print(vc)


'''
# 4
3 3
.*.
*.*
.*.
# 13
5 5
*.*.*
.*.*.
*.*.*
.*.*.
*.*.*

'''
'''
# 실패
import sys
input = sys.stdin.readline

def matching(idx):
    global vc
    for i in g[idx]:
        if v[i]:
            continue
        v[i] = 1
        if connect[idx][i] < 0 or matching(connect[idx][i]):
            vc+=1
            connect[idx][i] = vc
            return True
    return False

def matching2(idx):
    global vc
    for i in gg[idx]:
        if v[i]:
            continue
        v[i] = 1
        if connect[i][idx] < 0 or matching2(connect[i][idx]):
            vc+=1
            connect[i][idx] = vc
            return True
    return False

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n)]
gg = [[] for _ in range(m)]
for i in range(n):
    s = list(input().rstrip())
    for j in range(m):
        if s[j] == '*':
            g[i].append(j)
            gg[j].append(i)

ans = 0
connect = [[-1]*m for _ in range(n)]
vc = 0
for i in range(n):
    v = [0] * m
    matching(i)

for i in range(m):
    v = [0]*n
    matching2(i)
print(vc)
for i in connect:
    print(i)
'''
