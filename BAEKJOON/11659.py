'''
구간 합 구하기 4

수 N개가 주어졌을 때 i번째 수부터 j번째 수까지 합을 구하는 프로그램 작성.

입력
수의 갯수 n 합을 구해야 하는 회ㅑㅅ수 m
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nnl = list(map(int, input().rstrip().split()))
nl = [0] * (n+1)
for i in range(1, n+1):
    a = nnl[i-1]
    nl[i] = nl[i-1] + a
for i in range(m):
    a, b = map(int, input().rstrip().split())
    print(nl[b] - nl[a-1])
