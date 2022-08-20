'''
덩치

몸무게, 키 (x, y)
순위는 자기보다 큰 덩치가 몇 명이 있느냐로 결정.
동일 순위 가능.

입력
사람 수 n 2이상 50이하
몸무게 키 n번 제시
x y는 10이상 200이하

출력
등수 연속 제시
2 2 1 2 5 이런 식으로
'''
n = int(input())
kml = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * n

for i in range(n):
    for j in range(n):
        gz, bgg = kml[i], kml[j]
        if gz[0] < bgg[0] and gz[1] < bgg[1] :
            dp[i] += 1
        else:
            continue
# sl = sorted(list(set(dp)))
# pl = list(map(lambda x:dp.count(x), sl))
rank = list(map(lambda x: x+1, dp))
print(*rank)

# 괜히 같은데 하나 크다 이런거 따르지 말고 문제 제대로 읽자!!!!
