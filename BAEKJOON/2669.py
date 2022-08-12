'''
직사각형 네개의 합집합의 면적 구하기

입력
4줄. x1, y1, x2, y2 * 4 & 1이상 100 이하


'''
# 그래프 칠하기
def paint(pz) :
    x1, y1, x2, y2 = pz
    for i in range(x1, x2):
        for j in range(y1, y2):
            g[i][j] = 1

# 입력
ps = [list(map(int, input().split())) for _ in range(4)]

g = [[0]*101 for _ in range(101)]
# 실행
for p in ps :
    paint(p)
h = 0
for i in range(101) :
    h = sum([h]+g[i])
# 출력
print(h)






