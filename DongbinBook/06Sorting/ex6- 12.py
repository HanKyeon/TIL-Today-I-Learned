'''
두 배열의 원소 교체.

길이가 N인 배열 A, B를 최대 K번 바꿔치기 할 수 있다.
배열 A의 모든 원소의 합이 최대가 되도록 해야한다.
그 최댓값을 출력하는 프로그램을 작성하라.

N, K가 공백으로 구분되어 입력. N은 1에서 10만까지 K는 0에서 N까지
두번째 줄에는 배열 A
세번째 줄에는 배열 B
A,B 배열 내의 값은 천만 이내 자연수.
최댓값 출력
'''
# n, k, 배열 AB 입력
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
#A는 오름차순, B는 내림차순 정렬
a.sort
b.sort(reverse=True)
# 인덱스 1부터 두 배열의 원소를 최대 K번 비교.
for i in range(k) :
    # 비교해서 b가 더 크면 ai와ㅏ bi 인덱스 위치 변경.
    if a[i] < b[i] :
        a[i], b[i] = b[i], a[i]
    # 별거 없으면 하지 말고 ㅇㅇ
    else :
        break

print(sum(a)) # 배열 A의 합 출력