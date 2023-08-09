'''
문자열 집합
n개 문자열 집합 s 제시
m개 문자열 중 s에 포함되어 있는 것이 총 몇개인지 구해라.

입력
n, m 제시
n개 줄 집합 s 포함된 문자열 제시
m개 줄 검사해야 하는 문자열 제시

출력
m개 문자열 중 총 몇개가 s에 포함되어 있는가
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
ans = 0
s = {input().rstrip() for _ in range(n)}
for _ in range(m):
    if input().rstrip() in s:
        ans += 1
print(ans)




