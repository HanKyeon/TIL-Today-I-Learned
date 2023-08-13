'''
링

n개의 링. 톱니바퀴처럼 회전할 때 몇바퀴 도는지 기약분수로

입력
n 제시
링 순서 반지름 제시

출력
n-1줄 출력. 첫 링을 1바퀴 회전했을 때 얼마나 돌아가는지 기약분수 형태로.
'''
import sys
from math import gcd
input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().split()))
for i in range(1, n):
    g = gcd(nl[0], nl[i])
    print(f"{nl[0]//g}/{nl[i]//g}")