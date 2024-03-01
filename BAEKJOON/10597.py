'''
순열장난

1부터 n까지의 수로 이루어진 공백이 사라진 순열을 복구해라.

입력
수열 제시. 최대 50개의 수로 이루어짐.

출력
복구된 수열을 출력
'''
import sys
input = sys.stdin.readline

def dfs():
    global idx, n
    if len(stk) == n: print(*stk); exit()
    if p[idx] == '0': return

    s1= int(p[idx])
    if s1<=n and not v[s1]:
        v[s1]=1; stk.append(s1); idx+=1
        dfs()
        v[s1]=0; stk.pop(); idx-=1

    if idx+2 > len(p): return
    s2 = int(p[idx:idx+2])
    if s2<=n and not v[s2]:
        v[s2]=1; stk.append(s2); idx+=2
        dfs()
        v[s2]=0; stk.pop(); idx-=2

p = input().rstrip()
if len(p) < 10:
    for i in p: print(i, end=' ')
    exit()
n = (len(p)-9)//2+9
v = [1]+[0]*n
idx, stk = 0, []
dfs()

'''
"""
Title : 순열장난
Link : https://www.acmicpc.net/problem/10597
"""

from sys import stdin

input = stdin.readline


def search(idx: int):
    global seq, N, check
    if idx == len(seq):
        return [0]
    if not check[(x := seq[idx])]:
        check[x] = True
        if res := search(idx + 1):
            return [x] + res
        check[x] = False
    if idx < len(seq) - 1:
        num = seq[idx] * 10 + seq[idx + 1]
        if num > N or num < 10:
            return None
        if not check[num]:
            check[num] = True
            if res := search(idx + 2):
                return [num] + res
            check[num] = False
    return None


if __name__ == "__main__":
    seq = [int(x) for x in input().strip()]
    if (l := len(seq)) <= 9:
        print(*seq)
    else:
        N = (l + 9) // 2
        check = [False] * (N + 1)
        print(*search(0)[:-1])
'''