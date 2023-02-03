'''
4연산

정수 s 제시. s를 t로 바꾸는ㄴ 최소 연산 횟수 구해라.

s = s + s; (출력: +)
s = s - s; (출력: -)
s = s * s; (출력: *)
s = s / s; (출력: /) (s가 0이 아닐때만 사용 가능)

입력
s, t 제시.

출력
s를 t로 바꾸는 방법 출력.
s와 t가 같으면 0
바꿀수 없으면 -1
여러개면 사전순. * + - / 순서
'''
from collections import deque

def lego(a, b):
    if a == b:
        return 0
    q = deque()
    v = {a}
    for i, ys in [(a**2, '*'), (a*2, '+'), (0, '-'), (1, '/')]:
        if i == b:
            return ys
        v.add(i)
        q.append((i,ys))
    while q:
        n, ys = q.popleft()
        np, ng = 2*n, n**2
        if ng == b:
            return ys+'*'
        if np == b:
            return ys+'+'
        if ng < b and not ng in v:
            v.add(ng)
            q.append((ng, ys+'*'))
        if np < b and not np in v:
            v.add(np)
            q.append((np, ys+'+'))
    return -1

a, b = map(int, input().split())
print(lego(a, b))


'''
s, t = map(int, input().split())

calculation = ["+", "*"]

min_list = []
min_ = [10000000001]


def calculation_f(s, t, order):
    if min_[0] < len(order):
        return
    # print(min_list)

    if s >= t:
        if s == t:
            min_list.append(order)
            if min_[0] > len(order):
                min_[0] = len(order)
        return
    for calc in calculation:
        if calc == "*":
            s1 = s * s
        elif calc == "+":
            s1 = s + s
        order += calc
        if s1 != 1:
            # print(s1, s, t, order)
            calculation_f(s1, t, order)
            order = order[:-1]


if s == t:
    print(0)
else:
    calculation_f(s, t, "")
    calculation_f(1, t, "/")
    if min_list == []:
        print(-1)
    else:
        answer_list = []
        for i in range(len(min_list)):
            if len(min_list[-(i + 1)]) == min_[0]:
                a = min_list[-(i + 1)]
                answer_list.append(a)
        answer_list2 = []
        for i in answer_list:
            answer_list2.append([])
            for j in i:
                jj = ord(j)
                answer_list2[-1].append(jj)
        answer_list2.sort()
        answer = ""
        for j in answer_list2[0]:
            jj = chr(j)
            answer += jj
        print(answer)
'''

