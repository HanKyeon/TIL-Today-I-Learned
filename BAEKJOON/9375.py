'''
패션왕 신해빈

한 번 입었던 옷들의 조합은 절대 다시 안입음.

입력
테케T 최대100
의상 수 0이상 10이하
의상이름 종류 같은 이름 없음

출력
알몸이 아닌 상태로 입을 수 있는 경우 출력
'''
'''
각 갯수(선택 가능한 경우)를 곱해준 뒤 공집합 하나 빼주는 것.
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n == 0: # 옷 없으면 0
        print(0)
        continue
    di = {} # 종류에 받아 줄 것
    for i in range(n):
        a, b = input().rstrip().split()
        if di.get(b, 0) == 0: # 없으면
            di[b] = [a] # 리스트로 만들어라
        else: #있으면
            di[b].append(a) # 추가해라
    gob = [] # 곱해줄 숫자 정리
    for i in di: # 딕셔너리 키를 훑으면서
        gob.append(len(di[i])+1) # 그 밸류의 길이 +1을 더해줌
    ans = 1 # 곱해줄 것. 0인 경우 뺏으니 1로 해도 됨.
    if gob: # 곱이 안비었다면
        for i in gob:
            ans *= i # 곱해주고
    print(ans-1) # 안입은거 빼줌
