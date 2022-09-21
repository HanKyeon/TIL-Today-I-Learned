'''
1부터 12까지의 숫자 집합A
집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K개인 부분집합의 갯수를 출력하는 프로그램 작성.

입력
테케T
부분집합 원소의 수 n과 부분집합의 합 k가 여백 두고 제시.
'''
from math import factorial


def hap(li, idx):
    global n, k, nl
    a = li[:]
    if len(a) == n:
        if sum(a) == k:
            nl.append(a)
        return
    if sum(a) > k:
        return
    for i in range(idx+1, 12):
        a.append(ziphap[i])
        hap(a, i)
        a.pop()

ziphap =  [1,2,3,4,5,6,7,8,9,10,11,12]

for tc in range(1, int(input())+1):
    n, k = map(int, input().rstrip().split())
    nl = []
    inl = []
    hap(inl, -1)
    print(f"#{tc} {len(nl)}")







