'''
딱지놀이

입력
라운드n 1이상 1000이하
a가 낼 딱지 갯수 / 딲지 딱지 딱지
b가 낼 딱지 갯수 / 딱지 딱지
a,b 반복
무승부 시 D

출력
승자
'''
import sys
input = sys.stdin.readline
# 리스트 받아서 승패 판정 하는 함수
def winner(a, b):
    al, bl = [0, 0, 0, 0], [0, 0, 0, 0] # a, b 딱지 갯수
    # 인덱스0을 pop해서 그만큼 돌림. pop으로 삭제와 동시에 반복 시작
    for i in range(a.pop(0)):
        al[4-a[i]] += 1
    for i in range(b.pop(0)):
        bl[4-b[i]] += 1
    # 승패 판정
    for i in range(4):
        if al[i] > bl[i] :
            return 'A'
        elif al[i] < bl[i] :
            return 'B'
    return 'D'
# 입력 실행 출력 동시 진행
n = int(input())
for i in range(n) :
    print(winner(list(map(int, input().split())), list(map(int, input().split()))))