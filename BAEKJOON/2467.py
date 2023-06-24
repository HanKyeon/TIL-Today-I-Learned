'''
용액

특성값을 0에 가장 가까운 용액을 만들 것 두 용액 찾아라

입력
n 제시
n개 정수 제시

출력
특성값이 0에 가장 가까운 용액을 만들어내는 경우 하나 출력
'''
import sys
input = sys.stdin.readline

n = int(input().rstrip())
nl = list(map(int, input().rstrip().split()))
if nl[0] >= 0:
    print(*nl[:2])
    exit()
if nl[-1] <= 0:
    print(*nl[-2:])
    exit()
sta, end = 0, n-1
x, y, res = 0, 0, int(10e10)
while sta < end:
    s = nl[sta] + nl[end]
    if s == 0:
        x, y = sta, end
        break
    if s < 0:
        if -s < res:
            x, y, res = sta, end, -s
        sta += 1
    else:
        if s < res:
            x, y, res = sta, end, s
        end -= 1

print(' '.join(map(str, [nl[x], nl[y]])))