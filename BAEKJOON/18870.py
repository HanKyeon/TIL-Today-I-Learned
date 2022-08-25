'''
좌표 압축

수직선 위에 N개의 좌표. 좌표압축 적용 예정.
좌표 압축한 결과는 Xi>Xj를 만족하는 **서로 다른 좌표의 개수**와 같아야 한다.
좌표 압축은 얘보다 더 적은 값 갯수이다.
좌표압축한 결과 출력해보자.
'''
# 서로 다른 좌표의 갯수!!!!!!!!!!!!
n = int(input())
g = list(map(int, input().split()))
d = {}
a = sorted(list(set(g)))
for i in range(len(a)):
    d[a[i]] = i
for i in g:
    print(d[i], end=' ')


