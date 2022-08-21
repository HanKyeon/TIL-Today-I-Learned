'''
치킨 배달

N*N 도시.

x1-x2 y1-y2의 절댓값의 합이 치킨거리다.
치킨집을 M개로 줄이려 한다.
치킨 거리가 가장 짧게 M개로 줄이는 방법은?

입력
2이상 50이하 N, 1이상 13이하 M 제시
도시정보. 0은 빈 칸 1은 집 2는 치킨집

출력
폐업 시키지 않을 치킨집을 최대 M개 골랐을 때, 도시 치킨 거리의 최솟값
'''
import sys
input = sys.stdin.readline

def 치킨거리(hom, chi):
    hcli = [] #각 집의 치킨거리 최솟값 담을 값
    for i in hom:
        chl = 100 # 1,1 50,50이 최대 차이이므로 편하게 100 담음
        for j in chi:
            chl = min(abs(i[0]-j[0]) + abs(i[1]-j[1]), chl) # 치킨집마다 거리를 확인해 최솟값 저장
        hcli.append(chl) # 최솟값 담기
    return sum(hcli) # 그 합이 도시 치킨 거리다.

n, m = map(int, input().split())
hl, cl = [], [] # 홈리스트 치킨리스트
for i in range(1, n+1):
    s = input().split() # 입력
    for j in range(n):
        if s[j] == '1':
            hl.append((i, j+1)) # 집 좌표 추가
        elif s[j] == '2':
            cl.append((i, j+1)) # 치킨집 좌표 추가

minc = [] # 부분집합으로 갯수가 만족 할 때 거리를 담을 리스트
for i in range(2**len(cl)):
    scl = [] # 셀렉된 치킨 리스트
    for j in range(len(cl)):
        if i & (1<<j):
            scl.append(cl[j])
    if len(scl) == m: # 갯수가 m개면
        minc.append(치킨거리(hl, scl)) # 도시 치킨 거리를 구해서 담아준다.
    else:
        continue # 아니면 또 진행하고

print(min(minc)) # 그 중 가장 작은 값이 치킨 거리이다.




