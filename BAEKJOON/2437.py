'''
저울

하나의 양팔 저울을 이용해 물건의 무게를 측정 할 것. 추를 올릴 거다.
n개의 저울추 무게가 주어질 때, 이 추들을 사용하여 측정 할 수 없는 양의 정수 무게 중 최솟값을 구하는 프로그램 작성.

입력
추의 갯수 n 1이상 1000이하
n개의 양의 정수. 추의 무게는 1이상 100만 이하

출력
측정 할 수 없는 양정수 무게 중 최솟값.
'''
import sys
input=sys.stdin.readline

n = int(input())
nl = list(map(int, input().rstrip().split()))
nl.sort()
t = 1
for i in nl:
    if t<i:
        break
    t += i
print(t)

# 천재들 너무 많다. 아이디어 참고하고 검증만 했다.
# 작은 수를 더해서 합을 구해준다. 그 합보다 다음 수의 값이 크면 만들 수 없다는 것이다.
