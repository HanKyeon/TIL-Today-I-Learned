'''
창고 다각형

d를 [0]*n 설정
리스트의 최댓값 maxh
저장할 최댓값 stoh

왼쪽 오른쪽, 오른쪽에서 왼쪽 둘 다 실행.
최대 높이가 동일한 막대가 2이상 존재 할 경우 : 최대 높이가 처음 시작하는 인덱스~마지막 인덱스까지 maxh로 설정
stoh와 비교하여 입력된 인덱스의 높이가 높다면 stoh를 초기화하고 해당 인덱스에 stoh 등록.
최댓값 인덱스 여러개 뽑으려면 enumerate 이용. [i for i,v = enumerate(리스트) if v==maxh]

입력
1이상 1000이하의 N
인덱스, 높이 L K. 1이상 1000이하. 왼쪽면 L 최대가 1000이므로 1001까지 있어야 한다.

출력
창고 다각형 넓이
'''
# 입력 및 데이터 정리
n = int(input())
g = [0] * (1001)
for _ in range(n) :
    l, k = map(int, input().split())
    g[l] = k
maxh = max(g)
# 최대 높이가 2개 이상일 경우
maxidxlist = [i for i, val in enumerate(g) if val == maxh]
lmax = min(maxidxlist)
rmax = max(maxidxlist)
# 그 사잇값을 최댓값으로 통일
for i in range(lmax, rmax) :
    g[i] = maxh
# 왼쪽 오른쪽 시행
lh = 0
rh = 0
# 왼쪽
for i in range(lmax) :
    if g[i] > lh :
        lh = g[i]
    g[i] = lh
# 오른쪽
for j in range(1000, rmax, -1) :
    if g[j] > rh :
        rh = g[j]
    g[j] = rh
# 출력
print(sum(g))


