'''
이친수

이진수 중 0으로 시작하지 않고, 1이 두 번 연속 나타나지 않은 n자리 이친수 갯수 구해라.

입력
n 제시

출력
갯수 제시
'''

n = int(input())
if n < 3:
    print(1)
    exit()
bf, af = 1, 1
n-=2
while n:
    n-=1
    bf, af = af, bf+af
print(af)

