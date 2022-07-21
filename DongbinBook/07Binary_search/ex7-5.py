'''
부품 n개. 부품 별 고유번호.
어떤 손님이 M개 종류 부품 대량 구매.

M개 종류 모두 확인해서 견적서를 작성해야 한다.

예를 들어
가게 부품N = 5개
[8, 3, 7, 9, 2]

손님이 요천
M = 3개
[5, 7, 9]

이 때, 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes, 없으면 no를 출력.

첫 줄에는 1이상 100만 이하 정수 N
공백 구분 N개의 정수. 정수 역시 1이상 100만이하.

1이상 100만 이하 정수 M
공백 구분 M개의 정수. 정수 역시 1이상 100만 이하.
'''
# 이진 탐색 함수.
# 탐색을 원하는 배열, 찾고자 하는 값, 시작값, 끝값
def binary_search(array, target, start, end) :
    # 반씩 줄여나가기에 start가 end보다 작은 동안 반족.
    # start가 end보다 커지면 탐색을 다 한 것이므로 탈출, None 반환
    while start <= end :
        # 이진 탐색 닉값
        mid = (start + end) // 2
        # 딱 찍었는데 가운데 있으면 그 값을 뱉으면 됨.
        if array[mid] == target :
            return mid
        # 만약 중간값이 타겟보다 크다면, 중간값을 기준으로 왼쪽 탐색.
        elif array[mid] > target :
            end = mid - 1
        # 만약 중간값이 타겟보다 작다면, 중간값을 기준으로 오른쪽 탐색.
        else :
            start = mid + 1
    
    return None
# n 입력
n = int(input())

arr = list(map(int, input().split()))
arr.sort() # 이진 탐색은 정렬된 배열에서 가능하므로 소트.

m = int(input())

x = list(map(int, input().split())) # m 목록의 값을 딱 찍어서 찾으므로 sort가 필요 없음.

# x 순회
for i in x :
    # 이진탐색해서 반환하는 값을 판단.
    result = binary_search(arr, i, 0, n-1)
    # None은 없을 때 반환되므로 아래와 같이 출력.
    if result != None :
        print('yes', end = ' ')
    else :
        print('no', end = ' ')



#-----------------

'''
계수 정렬을 이용 할 수도 있다.
계수 정렬은 모든 원소를 포함한 리스트를 만든 뒤, 인덱스에 접근하여
특정한 번호의 부품이 매장에 존재하는지 확인하면 됨.
즉, 100만개의 리스트를 만들어서 배열에 등록 한 뒤
손님의 x를 순회하며 01010의 리스트를 순회하면 된다.
'''

n = int(input())
arr = [0] * 1000001

for i in input().split() :
    arr[int(i)] = 1

m = int(input())

x = list(map(int, input().split())) # m 목록의 값을 딱 찍어서 찾으므로 sort가 필요 없음.

for i in x :
    if arr[i] == 1 :
        print('yes', end = ' ')
    else :
        print('no', end = ' ')


#-----------

'''
또한, 이 문제는 set 자료형을 통해 확인이 가능하다.
존재 유무만 판단하면 되기 때문이다. (종류가 M)
'''

n = int(input())
arr = set(map(int, input().split()))

m = int(input())

x = list(map(int, input().split())) # m 목록의 값을 딱 찍어서 찾으므로 sort가 필요 없음.

for i in x :
    if i in arr :
        print('yes', end = ' ')
    else :
        print('no', end = ' ')










