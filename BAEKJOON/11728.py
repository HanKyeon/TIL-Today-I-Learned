'''
배열 합치기

배열 a b 합쳐서 정렬하고 출력
'''
import sys
input = sys.stdin.readline
input()
a = list(map(int,input().rstrip().split()))+list(map(int,input().rstrip().split()))
a.sort()
print(*a)

