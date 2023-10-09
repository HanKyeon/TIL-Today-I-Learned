'''
중복 빼고 정렬하기

n개 정수 제시. n개 정수 오름차순 정렬. 같은 정수는 한 번만 출력

입력
n 제시
숫자들 제시

출력
오름차순 정렬한 결과 출력. 같은 수는 한 번만 출력
'''
input();print(*sorted(list(set(map(int, input().split())))))
