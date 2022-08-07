'''
참외밭

참외 밭 생김새는 기역니은 돌린 길이다.

입력
단위 면적 당 참외 갯수 제시 1~20
한 점에서 !!반시계!! 방향으로 도는 둘레 길이 제시
동서남북 1234로 제시.

출력
면적 * 단위 면적 당 참외 갯수
'''
# 입력
k = int(input())
cv = [[0, 0] for _ in range(6)]
for i in range(6) :
    cv[i][0], cv[i][1] = map(int, input().split())

# 가공
v = [cv[i][1] for i in range(6)] # 길이값만 리스트로
# 큰 네모
w, h = 0, 0
for i in range(6) :
    if cv[i][0] < 3 :
        w = max(w, cv[i][1])
    else :
        h = max(h, cv[i][1])
# 인덱스 추출. 가로 긴 변, 세로 긴 변에 각각 양옆에 붙은 변의 차이가 그시기다.
wi, hi = v.index(w), v.index(h)
# 출력
print(((w * h) - abs((v[(wi+1)%6] - v[(wi-1)%6]) * (v[(hi-1)%6] - v[(hi+1)%6]))) * k)



