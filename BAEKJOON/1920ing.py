'''
수 찾기

N개의 정수가 주어질 때 이 안에 X라는 정수가 존재하는지 알아내는 프로그램 작성.

입력
N은 1이상 10만이하
M도 1이상 10만이하
모든 정수의 범위는 -2**31~2**31 사이.
'''
import sys
input = sys.stdin.readline

def 이분탐색(val, li):
    sta, end = 0, len(li)-1
    while sta <= end:
        mid = (sta+end)//2
        if li[mid] == val:
            return 1
        if li[mid] < val:
            sta = mid+1
        if li[mid] > val:
            end = mid-1
    return 0

n = int(input())
nl = sorted(list(map(int, input().split())))
m = int(input())
ml = list(map(int, input().split()))
for i in ml:
    print(이분탐색(i, nl))











'''
# 시간초과
for i in ml:
    if i in nl:
        print(1)
    else:
        print(0)
'''
