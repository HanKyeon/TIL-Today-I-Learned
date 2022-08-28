'''
통계학

N은 홀수
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수 제시, 4가지 기본 통계값 계산

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

출력
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.
'''
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input().rstrip())
nl = [int(input().rstrip()) for _ in range(n)]
nl.sort()
num = Counter(nl).most_common(2)
# ss = round(sum(nl)/n)
ss = sum(nl) // n if sum(nl)/n < sum(nl)//n + 0.5 else sum(nl)//n +1
ja = nl[n//2]
cb = num[1][0] if len(num) > 1 and num[0][1]==num[1][1] else num[0][0]
bw = max(nl)-min(nl)

print(ss)
print(ja)
print(cb)
print(bw)

# 15 6