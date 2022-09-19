'''
수 묶기

길이가 n인 수열. 수열의 합 구할 것. 그냥 수열의 합을 다 더해서 구하는 것이 아니라, 묶을 것이다. 자기 자신을 묶을 수 없다. 수열의 합을 구할 때 묶은 수는 서로 곱한 후 더한다.
수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 해라.

입력
수열 크기 n 50이하 자연수.
n개 줄에 수열의 각 수 제시. -1000이상 1000이하 정수.

출력
최대합 출력
'''
'''
음수 리스트, 양수 리스트 관리.
음수 갯수가 홀수라면 0을 곱해줘야 한다.
양수 리스트에서 둘 중 하나가 1이면 더해줘야 한다.
'''
import sys
input = sys.stdin.readline

n = int(input())
ml, pl = [], []
for _ in range(n):
    a = int(input())
    if a <= 0:
        ml.append(a)
    else:
        pl.append(a)

ml.sort()
pl.sort(reverse=True)
ans = 0
if len(ml) % 2:
    ans += ml.pop()
if len(pl) % 2:
    ans += pl.pop()
for i in range(0, len(ml), 2):
    ans += ml[i]*ml[i+1]
for i in range(0, len(pl), 2):
    if pl[i] == 1 or pl[i+1] == 1:
        ans += pl[i] + pl[i+1]
        continue
    ans += pl[i]*pl[i+1]
print(ans)












