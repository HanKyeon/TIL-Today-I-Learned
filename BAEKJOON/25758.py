'''
유전자 조합

유전자 형질은 대문자 2개.
두 유전자를 조합하면 1유전자 1번과 2유전자 2번이 붙은 유전자가 생긴다.
두 형질 중 알파벳 사전 순으로 같거나 큰 알파벳을 유전자의 표현형이라 한다.
N개의 1세대 유전자가 주어졌을 때 이들은 서로 다른 1세대 유전자들과 조합이 가능하다. 2세대 유전자의 표현형으로 가능한 알파벳의 수와 그 알파벳을 구해보자.

입력
n 제시
n개의 유전자 제시

출력
2세대 유전자의 표현형으로 가능한 알파벳 수 출력
알파벳 순서를 정렬 후 공백 구분 출력
'''
import sys
input = sys.stdin.readline

n = int(input())
nl = list(input().rstrip().split())
ans = set()
for x in range(ord('A'), ord('Z') + 1):
    x = chr(x)
    cnt = 0
    for i in range(n):
        if nl[i][0] == x:
            cnt += 1
    if cnt > 1:
        for i in range(n):
            ans.add(max(x, nl[i][1]))
    elif cnt == 1:
        for i in range(n):
            if nl[i][0] == x:
                continue
            ans.add(max(x, nl[i][1]))
print(len(ans))
ans = list(ans)
ans.sort()
print(*ans)

'''
N = int(input())
G = input().split()

firstMap = {k: 0 for k in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
secMap = {k: 0 for k in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

for g in G:
    firstMap[g[0]] += 1
    secMap[g[1]] += 1

answer = set()
for g in G:
    f, s = g[0], g[1]
    for k, v in firstMap.items():
        if k <= s and v > 0:
            if f != k or (f == k and v > 1):
                answer.add(s)
    for k, v in secMap.items():
        if k <= f and v > 0:
            if s != k or (s == k and v > 1):
                answer.add(f)

print(len(answer))
print(" ".join(sorted(answer)))
'''

'''
ans = set()
l, r = set(), set()
for i in nl:
    l.add(ord(i[0]))
    r.add(ord(i[1]))

ans = list(ans)
ans.sort()
print(*map(lambda x: lego(x), ans))
'''
'''
l, r = [], []
for i in nl:
    l.append(ord(i[0]))
    r.append(ord(i[1]))
minl, minr = min(l), min(r)
ans = set()
for i in range(n):
    if l[i] >= minr:
        ans.add(l[i])
        continue
    if r[i] >= minl:
        ans.add(r[i])
ans = list(ans)
ans.sort()
print(*map(lego, ans))
'''
'''
# 시간 초과
def lego(num): return chr(num)

ans = set()
for i in range(n):
    for j in range(i+1, n):
        ans.add(max(ord(nl[i][0]), ord(nl[j][1])))
        ans.add(max(ord(nl[i][1]), ord(nl[j][0])))
ans = list(ans)
ans.sort()
print(*map(lambda x: lego(x), ans))
'''
