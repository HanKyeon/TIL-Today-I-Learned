'''
왕위 계승

유토피아의 왕이 사망햇다. 원소 했다. 그러자 왕실 귀족이 왕위를 주장하기 시작했다. 혈통이 가장 가까운 사람이 유토피아를 통치한다.
나라를 세운 사람과 혈통이 가장 가까운 사람은 그의 자손이 아닌 사람과 피가 덜 섞인 사람이다.
모든 사람은 아버지 혈통과 어머니 혈통을 반 받게 된다.
나라 세운 사람 자식은 1/2 왕족, 그 아들이 왕족이 아닌 사람과 결혼 한 경우에는 아들 자식은 1/4 왕족이다.
가장 나라를 세운 사람과 혈통이 가까운 사람을 찾아라.

입력
n, m 제시.
시조 이름 제시.
n개 줄 가족 정보 제시.
정보는 이름 세개, 공백 구분. 1자식이름 부모이름1 부모이름2
m개 줄에 왕위 계승 주장하는 사람의 이름이 한 줄에 하나씩 제시.
모든 이름은 1~10글자이며, 알파벳 소문자로만 이루어져 있다.

출력
유토피아를 세운 사람과 가장 혈통이 가까운 사람의 이름 출력. 답은 항상 유일하다.
'''
# 풀다가 너무 많이 꼬여서 인터넷 통해 보면서 풀이.

# from collections import deque
# import sys
# input = sys.stdin.readline

# def ts(idx):
#     q = deque()
#     for i in reqn:
#         if reqn[i] == 0 and not ans.get(i, 0):
#             q.append(i)
#     if not q:
#         return False
#     while q:
#         na = q.popleft()
#         ans[na] = idx
#         for i in g.get(na, []):
#             reqn[i] -= 1
#     return True

# n, m = map(int, input().rstrip().split())
# sizo = input().rstrip()
# reqn = {sizo:0}
# g = {}
# ans = {}
# for _ in range(n):
#     c, p1, p2 = input().rstrip().split()
#     reqn[c] = 2
#     if g.get(p1, 0):
#         g[p1].append(c)
#     else:
#         g[p1] = [c]
#     if g.get(p2, 0):
#         g[p2].append(c)
#     else:
#         g[p2] = [c]

#     if reqn.get(p1, -1) < 0:
#         reqn[p1] = 0
#     if reqn.get(p2, -1) < 0:
#         reqn[p2] = 0

# a = ts(1)
# ix = 2
# while a:
#     a = ts(ix)
#     ix+=1
# print(reqn)
# print(ans)

# for _ in range(m):
#     k = input().rstrip()






import sys
input = sys.stdin.readline

def init():
    n, m = map(int, input().rstrip().split())
    sizo = input().rstrip()
    g = {}
    for _ in range(n):
        c, p1, p2 = input().rstrip().split()
        for i in [c, p1, p2]:
            if i not in g:
                g[i] = []
        g[c] = [p1, p2]
    qst = [input().rstrip() for _ in range(m)]
    return qst, g, sizo

def dfs(num):
    if num == sizo:
        return 1
    if num not in g:
        return 0
    if not g[num]:
        return 0
    return (dfs(g[num][0]) + dfs(g[num][1])) / 2

qst, g, sizo = init()
val = float('-inf')
nking = None
for i in qst:
    blood = dfs(i)
    if blood > val:
        val = blood
        nking = i
print(nking)




'''
빠른 코드
# 왕위 계승
# https://www.acmicpc.net/problem/5021
# https://github.com/yhs3434/Algorithms

from heapq import heappop, heappush

n, m = map(int, input().split(' '))
king = input()
kingdom = {}
kingdom[king] = 1 << 20
people = []
for _ in range(n):
    s, a, b = input().split(' ')
    people.append((s, a, b))

for i in range(n):
    for j in range(n):
        s, a, b = people[j]
        kingdom[s] = 0
        if a in kingdom:
            kingdom[s] += 0.5*kingdom[a]
        if b in kingdom:
            kingdom[s] += 0.5*kingdom[b]

maxVal = 0
maxPerson = ''
for _ in range(m):
    p = input()
    if p not in kingdom:
        continue
    else:
        if kingdom[p] > maxVal:
            maxVal = kingdom[p]
            maxPerson = p
print(maxPerson)
'''

