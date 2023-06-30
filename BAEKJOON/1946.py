'''
신입 사원

서류, 면접 중 적어도 다른 하나가 다른 애보다 떨어지지 않는 사람만 뽑을 것
최대 인원수 구해라.

입력
테케T
n제시
n개 줄 서류심사 면접성적 제시. 동석차 없이 결정

출력
선발할 수 있는 신입사원 최대 인원 수
'''
import sys
input = sys.stdin.readline

def lego():
    n = int(input())
    nl = [list(map(int, input().rstrip().split())) for _ in range(n)]
    nl.sort()
    ret, p = 1, 0
    for i in range(1, n):
        if nl[i][1] < nl[p][1]:
            p = i
            ret += 1
    return ret

for _ in range(int(input())):
    print(lego())















