
## 이진 탐색

 - 정렬되어 있는 리스트에서 특정한 데이터를 빠르게 탐색 할 수 있도록 해주는 탐색 알고리즘.

 - 순차탐색과의 비교 : 순차 탐색은 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법. 가장 기본적인 탐색 방법. 리스트에서 특정 데이터의 존재를 확인 할 때 별다른 말이 없다면 기본적으로 순차 탐색.

 - 이진 탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법. 기본적으로 리스트가 정렬되어 있어야 함. 로그 시간의 시간 복잡도를 갖는다. 이진탐색은 탐색 범위를 명시해야한다. 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다.

 1. 정렬 된 상태
 2. 시작점과 끝점의 절반인 중간점의 값 확인
 3. 만약 중간점이 탐색 값보다 크다면, 왼쪽에서, 작다면 오른쪽에서 다시 이진 탐색 실시.
 4. (시작점 인덱스 + 끝점 인덱스) // 2 가 중간점

 - 단계마다 탐색범위를 2로 나누는 것과 동일하므로 연산 횟수는 log2 N에 비례.
 - 예를 들어 초기 데이터 개수가 32개일 때, 이상적으로 1단계를 거치면 16개 가량의 데이터만 남는다. 2단계 후에는 8개, 3단계 후에는 4개.
 - 즉, 이진 탐색은 탐색 범위를 절반씩 줄이며 시간복잡도 O(logN)을 보장한다.

 - 재귀로 이진 탐색 구현

```
# 탐색을 수행하고자 하는 배열, 데이터, 시작값 끝값을 받는다.
def binary_search(array, target, start, end) :
    # start가 end보다 크다면 탐색하는 곳에 존재하지 않는 것과 다름 없다.
    # start가 end보다 커진다면 탐색 범위가 다 줄어들었음에도
    # 원소를 찾지 못한 것이기에 None을 반환
    if start > end : 
        return None
    mid = (start + end) // 2 # 중간점
    # 중간 점 인덱스와 타겟이 같다면 중간값 리턴
    if array[mid] == target :
        return mid
    # 중간값이 타겟보다 작다면 중간점 위치를 포함한 오른쪽에는 항상 타겟보다 큰 값이 존재하기에
    # 왼쪽 부분에 대해 탐색을 return
    elif array[mid] > target :
        return binary_search(array, target, start, mid - 1)
    # 중간값이 타겟보다 크다면 중간점 위치를 함한 왼쪽에는 항상 타겟보다 작은 값이 존재하기에
    # 오른쪽 부분에 대한 탐색을 return
    else :
        return binary_search(array, target, mid + 1, end)
 # 원소의 갯수와 타겟값 입력 받기
n, target = list(map(int, input().splt()))
 # 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None :
    print('원소가 존재하지 않습니다.')
else :
    print(result + 1)
```

 - 반복문 구현

```
def binary_search(array, target, start, end) :
    while start <= end :
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target :
            return mid
        # 중간점의 값보다 타겟 값이 작은 경우, 왼쪽 확인을 위해 end를 mid-1로 변경
        elif array[mid] > target :
            end = mid - 1
        # 중간점의 값보다 타겟 값이 큰 경우, 오른쪽 확인을 위해 start를 mid+1로 변경.
        else :
            start = mid + 1
    return None

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result - binary_search(array, target, 0, n - 1)
if result == None :
    print('원소가 존재하지 않습니다.')
else :
    print(result + 1)
```

### 파이썬 이진 탐색 라이브러리

 - 코테를 위해 알아두면 좋은 라이브러리.

 - bisect_left(a,  x) : cpp의 lower bound와 동일. 정렬된 순서를 유지하면ㅁ서 배열 a에 x를 삽입 할 가장 왼쪽 인덱스 반환.
 - bisect_right(a, x) : cpp의 upper bound와 동일. 정렬된 순서를 유지하며 배열 a에 x를 삽입 할 가장 오른쪽 인덱스 반환.

 이러한 함수를 이용해 값이 특정 범위에 속하는 데이터 갯수를 쉽게 구할 수 있다.

 왼쪽에서 원하는 값 시작점을 찾고, 오른쪽에서 원하는 값이 끝나는 인덱스를 찾아 두 인덱스를 뺴면 해당 값의 범위에 포함되어 있는 데이터의 범위, 갯수를 알 수 있다.

```
# 값이 특정 범위에 속하는 데이터 갯수 구하기.

from bisect import bisect_left, bisect_right

# 정렬된 a 배열에서 left_value ~ right_value의 갯수
def count_by_range(a, left_value, right_valut) :
    # 우측에서부터 right_value값이 최초로 나오는 인덱스
    right_index = bisect_right(a, right_value)
    # 좌측에서부터 left_value값이 최초로 나오는 인덱스
    left_index = bisect_left(a, left_value)
    # 우측 인덱스 - 좌측 인덱스 = 배열 내 a값의 갯수
    return right_index - left_index
```

### 파라메트릭 서트 Parametric Search

 - 이진 탐색을 활용해야 하는 문제가 출제되는 경우, 많은 유형

 - 파라메트릭 서치랑 최적화 문제를 결정 문제(예 혹은 아니오)로 바꾸어 해결하는 기법. 이 때, 최적화 문제란, 어떤 함수의 값을 최대한 낮추거나 최대한 높이거나 하는 등의 문제이다. 그러한 문제를 바로 해결하기 어려운 경우 그 문제를 여러번의 결정 문제로 바꾸어서 해결 할 수 있다.
 ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제. 탐색 범위를 좁혀가며 현재 범위에서는 이 조건을 만족하는지 체크를 하며 탐색 범위를 좁혀가며 가장 알맞은 값을 찾을 수 있다.

 - 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결 할 수 있다.
 - 탐색 범위가 크다면, 이진 탐색을 떠올려야 한다.
