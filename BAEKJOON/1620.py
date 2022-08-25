'''
포마 이다솜

입력
도감에 수록된 포켓몬 수 N 맞춰야 하는 문제 갯수 M 제시 1이상 10만이하
1번부터 N번까지의 포켓몬이 한 줄에 제시
맞춰야 하는 문제가 M번 제시

출력
이름에는 번호
번호에는 이름
'''
import sys
input = sys.stdin.readline
# dict[] / dict.items()
di = {}
n, m = map(int, input().split())
for i in range(1, n+1):
    s = input().rstrip()
    di[str(i)] = s
    di[s] = i
for _ in range(m):
    s = input().rstrip()
    print(di[s])



