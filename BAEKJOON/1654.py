'''
랜선 자르기

K개의 랜선을 최대길이의 N개로 잘라서 가지고 싶다!

입력:
랜선갯수1이상 만이하 K, 1이상 100만이하 N N은 항상 K 이상이다.
1이상 2^31-1 이하 길이의 랜선 K개 제시.
'''
'''
이분탐색 하면 될듯? 작으면 많고 크면 적어지도록 내림차순 정돈된.
'''
'''
아..... n이 무조건 딱 떨어지지 않는 경우를 생각하지 못했다!
'''

import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

def 갯수세기(num):
    ret = 0
    for i in cl:
        ret += i // num
    return ret

k, n = map(int, input().split())
cl = [int(input()) for _ in range(k)]

sta, end = 0, max(cl) # mid가 // 이기에 홀수는 날라간다 ㅇㅏ마도
maxl = 0
# 갯수가 11개여야 함.
while sta <= end:
    mid = (sta+end)//2 # 중앙값
    if mid == 0: # 1 1 / 1 이라는 씹 악질 테케가 있으므로
        mid += 1 # mid가 0이라면 +1 해서 본다.
    cn = 갯수세기(mid)
    if cn < n: # 갯수가 k보다 작다면
        end = mid-1 # end를 땡겨서 다시 테스트 한다.
    elif cn >= n : # 갯수가 k이상이라면
        maxl = mid # 기록하고
        sta = mid+1 # sta를 땡겨서 다시 테스트. 더 크면서 n개가 나오는 숫자를 찾자.
print(maxl)

# 1 1 500 -> 499
# 2 2 500 500 -> 무한루프
# 1 3 500 -> 165 나옴

'''
    elif cn == n: # cn == k라면
        maxl = mid # 기록하고
        sta = mid+1 # mid가 더 크면서 k개가 나올 때까지 찾으러 가자.

'''





'''
def 이분탐색(sta, end): # 시작점, 끝점, 리스트, 타겟
    global n
    if sta > end:
        return
    
    mid == (sta+end)//2
    if 갯수세기(mid) == n:
        return mid
    elif 갯수세기(mid) < n:
        return 이분탐색(sta, mid-1)
    elif 갯수세기(mid) > n:
        return 이분탐색(mid+1, end)
    else:
        return 0

def 갯수세기(num):
    ret = 0
    for i in cl:
        ret += i // num
    return ret
'''


