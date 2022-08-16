'''
괄호 짝짓기
() [] {} <>
4개가 다 유효하게 되었는가?
유효하다면 1
아니라면 0
'''

def 함수(li):
    c1, c2, c3, c4 = 0, 0, 0, 0
    for i in li:
        if i == '(' or i == ')':
            if i == '(':
                c1 += 1
            elif i == ')':
                c1 -= 1
            if c1 < 0:
                return 0
        elif i == '[' or i == ']':
            if i == '[':
                c2 += 1
            elif i == ']':
                c2 -= 1
            if c2 < 0:
                return 0
        elif i == '{' or i == '}':
            if i == '{':
                c3 += 1
            elif i == '}':
                c3 -= 1
            if c3 < 0:
                return 0
        elif i == '<' or i == '>':
            if i == '<':
                c4 += 1
            elif i == '>':
                c4 -= 1
            if c4 < 0:
                return 0
    if c1 or c2 or c3 or c4:
        return 0
    return 1

for testcase in range(1, 11):
    _, g = input(), input()
    print(f"#{testcase} {함수(g)}")
