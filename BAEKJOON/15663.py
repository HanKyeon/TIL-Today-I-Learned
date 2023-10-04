'''
n과 m 9

n개 자연수 중에서 m개를 고른 수열을 모두 구해라

입력
n, m 제시
nl 제시

출력
한 줄에 하나씩 조건을 만족하는 수열 출력. 중복 수열 여러번 출력 안되고 각 수열은 공백 구분 출력, 사전순 증가
'''
def dfs():
    global n, m
    if len(ans) == m: print(*ans); return
    fla = 0
    for i in range(n):
        if v[i] or fla==nl[i]: continue
        ans.append(nl[i]); v[i]=1; dfs(); fla=ans.pop(); v[i]=0
n, m = map(int, input().split())
nl = list(sorted(map(int, input().split())))
v, fla, ans = [0]*n, 0, []
for i in range(n):
    if fla==nl[i]: continue
    ans.append(nl[i]); v[i]=1; dfs(); fla=ans.pop(); v[i]=0

'''
# 빠른 코드
from itertools import permutations
from sys import stdin, stdout

_, M, *arr = stdin.read().split()
arr.sort(key=int)
stdout.write('\n'.join(map(' '.join, dict.fromkeys(permutations(arr, int(M))))))
'''
