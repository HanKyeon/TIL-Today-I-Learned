'''
단어 정렬

길이가 짧은 것부터
길이가 같다면 사전 순으로
'''
import sys
input = sys.stdin.readline

n = int(input())
sl = set(input().rstrip() for _ in range(n))
sl = list(sl)
sl.sort()
sl.sort(key=len)
for i in sl:
    print(i)