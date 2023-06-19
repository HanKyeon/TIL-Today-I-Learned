'''
차이를 최대로

n개 정수로 이루어진 배열 a
a0-a1 + a1-a2+...an-1-an-1 순서 바꿔서 최댓값을 구해라.

입력
n 제시
정수 제시

출력
최댓값 출력
'''
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().rstrip().split()))
ans = 0
for i in permutations(nl):
    ret = 0
    for j in range(1, n):
        ret += abs(i[j-1]-i[j])
    if ans < ret:
        ans = ret
print(ans)

'''
최대 최소 최대 최소
최소 최대 최소 최대
중앙 최소 최대 중앙
중앙 최대 최소 중앙
중앙 둘 위치도 바꿀 수 있다면 그 중 하나는 무조건 최댓값이라고 한다.
'''