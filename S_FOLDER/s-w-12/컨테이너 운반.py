'''
컨테이너 운반

n개 트럭  m대 트럭 a에서 b로.
트럭당 한 개. 적재용량 초과 x
실린 화물 무게, 트럭마다 적재 용량 제시.
A에서 B로 m대의 트럭이 편도 1회만 운행.
이 때 이동한 화물의 총 중량이 최대가 되도록 옮겼다면, 옮긴 화물 전체 무게는?
화물이 싣지 못할 수도 있고 남는게 없을 수도 있다.

입력
테케 T
컨테이너수 n 트럭 수 m. n개 화물이 무게 wj, 그 다음줄에  m개 트럭 적재 용량 제시.

출력
테케T 답

'''
from heapq import heappop, heappush

def 함수(trk):
    while nl and trk < nl[-1]:
        nl.pop()

for tc in range(1, int(input())+1):
    n, m = map(int, input().rstrip().split())
    nl = list(map(int, input().rstrip().split())) # 옮길 화물
    ml = list(map(int, input().rstrip().split())) # 트럭 용량들
    nl.sort()
    ml.sort()
    ans = 0
    while ml and nl:
        trk = ml.pop()
        if nl and trk < nl[-1]:
            함수(trk)
        if nl:
            ans += nl.pop()
    print(f"#{tc} {ans}")










