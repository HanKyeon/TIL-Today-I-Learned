'''
1차원 정원

수직선 정원
좌표 i에 꽃이 하나씩. 총 N개의 꽃
자동 분무기. 정수좌표 닫힌구간 x-D~ x+D 물줌
N과 D 제시 모든 꽃이 한개 이상 분무기에서 물을 받을 수 있도록 하기 위해 필요한 분무기 수

입력
테케
N과 1 제시

10 3


'''
for t in range(1, int(input())+1):
    n, d = map(int, input().split())
    if n % (2*d+1) == 0:
        num = n // (2*d+1)
    else :
        num = n // (2*d+1) + 1
    print(f"#{t} {num}")

