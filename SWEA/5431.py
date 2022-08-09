'''
민석이의 과제 체크하기

교수 송민석. 수강생 N명
과제 ON
제출 한 사람 목록
1번부터 N번까지 번호 ON
과제 제출 안한 사람 번호 오름차순 출력

입력
테스트케이스 수
2이상 100이하 수강생 수 N 과제 제출한 사람 수 1이상 N이하 K.
과제 제출한 사람 번호 K개가 공백 구분 제시 1이상 N이하 정수

출력
#t 제출 안한사람 번호 오름차순

'''

for testcase in range(1, int(input())+1) :
    # 입력
    n, k = map(int, input().split())
    okdk = list(map(int, input().split()))
    # 실행
    nope = list(map(str, sorted(list(set(list(range(1, n+1)))- set(okdk)))))
    # 출력
    print(f"#{testcase} {' '.join(nope)}")

