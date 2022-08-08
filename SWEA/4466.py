'''
최대 성적표 만들기

N개 과목 시험 만점 100ㅈ머
K개의 과목 선택해서 넣는다.
총점이 가장 높게.
..? 정렬해서 하면 되는데 뭐 메모리가 늦나?

입력
테케
1이상 K이상 N이상 100이하
N개의 정수가 공백 하나로 공백 구분

출력
#T 총점 최댓값
'''

for testcase in range(1, int(input()) + 1) :
    # 입력
    n, k = map(int, input().split())
    nl = list(map(int, input().split()))
    nl.sort(reverse=True)
    # 출력
    print(f"#{testcase} {sum(nl[:k])}")

