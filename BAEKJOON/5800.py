'''
성적 통계

최대 최소 점수차 구해라.

입력
k 제시
k개 줄 각 반 학생 수와 각 학생 수학성적 제시.

출력
Class X
Max 점수, Min 점수, Largest gap 점수차
'''
import sys
input = sys.stdin.readline

for i in range(1, int(input())+1):
    print(f"Class {i}")
    li = list(map(int, input().rstrip().split()))
    k = li.pop(0)
    li.sort()
    m, M, lg = 100, 0, 0
    for j in range(k):
        if li[j] < m:
            m = li[j]
        if li[j] > M:
            M = li[j]
        if j and abs(li[j]-li[j-1]) > lg:
            lg = abs(li[j]-li[j-1])
    print(f"Max {M}, Min {m}, Largest gap {lg}")




