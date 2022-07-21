'''
수가 크기 상관없이 나열.
큰수부터 작은 수의 순서로 정렬.
내림차순으로 정렬하는 프로그램 작성.

처음에 갯수 n이 500까지 주어짐.
둘째줄부터는 n개의 수 입력됨. 1~10000 사이의 자연수
'''

# 갯수 입력
n = int(input())

ar = []
# 입력 받고 리스트에 추가
for i in range(n) :
    ar.append(int(input()))

# 내림차순 정렬
ar = sorted(ar, reverse = True)
# 내부 숫자 출력.
for i in ar :
    print(i, end = ' ')







