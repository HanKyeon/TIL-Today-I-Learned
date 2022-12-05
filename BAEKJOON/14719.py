'''
빗물

비가 오면 블록 사이에 빗물이 고인다.
고이는 빗물의 총량은?

입력
h, w 제시.
블록 높이 0이상 h이하 정수 w개 제시.
블록 내부 빈 공간 x 바닥은 항상 막혀있다.

출력
한 칸의 용량은 1, 고이는 빗물의 총량을 출력해라.
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split()) # 높이 n 길이 m
nl = list(map(int, input().rstrip().split())) # 길이 m

maxh = max(nl)
nnl = [maxh] * m

idx = 0
val = nl[idx]
nnl[0] = nl[0]
while nl[idx] != maxh:
    nval = nl[idx]
    if nval > val:
        val = nval
    nnl[idx] = val
    idx += 1

idx = m-1
val = nl[idx]
nnl[0] = nl[0]
while nl[idx] != maxh:
    nval = nl[idx]
    if nval > val:
        val = nval
    nnl[idx] = val
    idx -= 1

print(sum(nnl) - sum(nl))
