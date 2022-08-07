'''
일곱 난쟁이

9개 숫자
7개 숫자 합 100

입력 : 
각각 9번의 줄로 난쟁이들 키 제시

출력
7난쟁이의 키를 오름차순 배치
'''
# 입력
hl = [int(input()) for _ in range(9)]
hl.sort()
hls = sum(hl)
# 합에서 서로 다른 두 수를 빼서 100이 되면 리무브 후 반복문 탈출
for i in hl :
    for j in hl :
        if i != j and hls - i - j == 100 :
            hl.remove(i)
            hl.remove(j)
            break
    if len(hl) == 7 :
        break
# 출력
for x in hl :
    print(x)


