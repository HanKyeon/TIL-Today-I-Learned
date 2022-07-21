'''
정렬 된 배열에서 특정 수의 갯수 구하기

첫줄에서 N과 x가 정수형태 공백 구분
둘째줄에서 N개의 원소가 정수 형태로 공백구분 입력
N은 1이상 100만이하 x는 -10억 ~ 10억

수열의 원소 중 값이 x인 원소 갯수 출력

'''

from bisect import bisect_left, bisect_right

# 정렬된 a 배열에서 left_value ~ right_value의 갯수
def count_by_range(a, left_value, right_valut) :
    # 우측에서부터 right_value값이 최초로 나오는 인덱스
    right_index = bisect_right(a, right_value)
    # 좌측에서부터 left_value값이 최초로 나오는 인덱스
    left_index = bisect_left(a, left_value)
    # 우측 인덱스 - 좌측 인덱스 = 배열 내 a값의 갯수
    return right_index - left_index

n, x = map(int, input().split())

arr = list(map(int, input().split()))

count = count_by_range(arr, x, x)

if count == 0 :
    print(-1)

else :
    print(count)

