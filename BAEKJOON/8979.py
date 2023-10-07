'''
올림픽

금메달 수가 더 많은
같으면 은메달 수가 더 많은
같으면 동메달 수가 더 많은
어느 국가가 몇 등 했는지 알려주삼

입력
n, k 제시. 1부터 n 정수

출력
k의 등수 정수로 출력
'''
import sys
input= sys.stdin.readline

n, k = map(int, input().rstrip().split())
nl = [list(map(int, input().rstrip().split())) for _ in range(n)]
nl.sort(key=lambda x: (-x[1], -x[2], -x[3]))
if nl[0][0] == k: print(1); exit()
a, b = 1, 0
for i in range(1, n):
    if nl[i][1:] == nl[i-1][1:]: b+=1
    else: a+=b+1; b=0
    if nl[i][0] == k: print(a); break
