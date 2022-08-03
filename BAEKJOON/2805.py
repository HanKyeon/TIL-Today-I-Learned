'''
나무자르기. 떡자르기랑 같다. 이분탐색.
'''

import sys
# n, m 입력
n, m  = map(int, input().split())
# 나무 높이 입력. 최대 100만개의 나무를 받아야 하므로 readline()으로 실행
trh = list(map(int, (sys.stdin.readline().rstrip()).split()))
# 이분탐색 데이터
sta = 0
end = max(trh)
rh = 0 # 최종 높이

while sta <= end :
    mid = (sta + end) // 2
    ta = 0
    # 나무들 순회하면서 자르는 값보다 높으면 높이에 더해준다
    for i in trh :
        if i > mid :
            ta += i - mid
    # 반틈에서 나무의 양이 원하는 만큼이라면 최종 높이에 mid 넣고 탈출
    if ta == m :
        rh = mid
        break
    # 나무의 양이 많으면, 양을 줄이기 위해 sta를 줄여줘야 한다.
    if ta > m :
        sta = mid + 1
        rh = max(rh, mid)
    # 양이 적으면 더 많이 얻기 위해 아래쪽으로 자르게 end를 줄여준다.
    if ta < m :
        end = mid - 1

print(rh)

'''
나무를 0m 1m 2m 3m ... 으로 잘라갈 수록 얻어지는 나무의 양이 줄어든다.
정렬된 상태라고 볼 수 있으므로 이분탐색을 하기 적당하다.
목표값보다 양이 많을 때, 적을 때 sta와 end를 어느 방향으로 움직일지 설정을 잘 하다.
'''