'''
숫자 야구

숫자야구 함.
가능한 답의 갯수를 구해라

입력
질문 n개
n개 줄 세자리 수, 스트라이크, 볼 제시

출력
생각하고 이씅ㄹ 답 총 갯수
'''
from itertools import permutations

num = list(permutations(list(map(str, range(1, 10))), 3))

for _ in range(int(input())):
    n, s, b = map(int, input().split())
    n = list(str(n))
    rmcnt = 0
    for i in range(len(num)):
        sc, bc = 0, 0
        i-=rmcnt # num[0] 부터 시작
        for j in range(3):
            if num[i][j] == n[j]: sc += 1
            elif n[j] in num[i]: bc+=1
        if sc!=s or bc!=b:
            num.pop(i)
            rmcnt += 1

print(len(num))
