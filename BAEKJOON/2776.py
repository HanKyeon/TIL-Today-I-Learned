'''
암기왕

하루동안 본 정수들은 수첩1
m개 질문. x라는 정수 본 적 있는가?
대답을 수첩2에 작성
수첩 2에 있는 것들이 수첩 1에 있으면 1 업스면 0

입력
테케T 제시
수첩1 정수 갯수 n 제시
수첩1 제시
수첩2 m 제시
수첩2 제시
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, nl = int(input()), set(map(int, input().rstrip().split()))
    m, ml = int(input()), list(map(int, input().rstrip().split()))
    for i in ml: print(1 if i in nl else 0)

