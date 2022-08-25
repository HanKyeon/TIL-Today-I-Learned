'''
카드

L123 R 456 일 때

0 : 123456
1 : 124356
2 : 142536
3 : 415263
4 : 451623
5 : 456123

이 기능을 활용하여 카드 순서가 오름차순 또는 내림차순이 되도록 정렬하려 한다.

입력으로 N장의 카드와 정리되지 않은 상태의 카드 순서가 주어질 때
최소 몇 번의 셔플로 카드를 정렬 할 수 있는지 계산.
오름차순/내림차순 중 셔플 횟수의 최솟값 출력.
정렬 불가 혹은 5를 넘어가면 정답은 -1

1. 카드의 갯수는4이상 12이하 짝수.
2. 각각 카드는 1~N 숫자 표기

입력
테케T
카드갯수N
정렬되지 않은 상태의 카드 번호가 순서대로 나열.

출력
#T 정렬에 필요한 최소 셔플 횟수
'''
def shuf(li, num):
    ls, rs = li[:len(li)//2], li[len(li)//2:]
    if num == 0:
        return li



for testcase in range(1, int(input())+1):
    n = int(input())
    cz = list(map(int, input().split()))
    soc = sorted(cz)
    sorc = reversed(soc)
    if cz == soc or cz == sorc:
        print(f"#{testcase} 0")
        continue













