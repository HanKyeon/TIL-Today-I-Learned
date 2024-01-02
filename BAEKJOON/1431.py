'''
시리얼 번호

기타 시리얼번호 정렬할 것.
1. 길이가 짧은 것이 먼저
2. 같으면 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저 온다.
3. 1,2번으로도 비교 불가능하다면 사전순으로 비교. 숫자가 알파벳보다 작다.

입력
n 제시
n개 줄 시리얼 번호 제시

출력
n개 줄에 정렬된 것 출력
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    s = input().rstrip()
    hap = 0
    for i in s:
        try: hap+= int(i)
        except: continue
    heappush(heap, (len(s), hap, s))

while heap: print(heappop(heap)[2])

'''
n = int(input())

arr = list(input() for _ in range(n))

def f(s):
    val = 0 
    for i in s:
        if i.isnumeric():
            val += int(i)
    return val

arr =sorted(arr,key =lambda x:(len(x),f(x),x))

for i in arr:
    print(i)
'''