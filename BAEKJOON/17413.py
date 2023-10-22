'''
단어 뒤집기 2

알파벳 소문자, 숫자, 특문으로 이루어짐
시작과 끝은 공백이 아님
<와 >가 문자열에 있는 경우 번갈아 등장하며 <먼저 등장, 두 문자 갯수 동일

<>사이에 길이 3이상인 부분 문자열이고, 사이에는 알파벳 소문자와 공백만 있다. 태그는 단어가 아님

입력
s 제시

출력
s 뒤집기
'''
import sys
input = sys.stdin.readline

s = input().rstrip()
stk, ans = [], ''

for i in s:
    if i == '<':
        while stk: ans += stk.pop()
    stk.append(i)
    if i == '>':
        while stk: ans += stk.pop(0)
    if i == ' ' and stk and stk[0] != '<':
        stk.pop()
        while stk: ans += stk.pop()
        ans += ' '
if stk and stk[-1] == '>':
    ans += ''.join(stk)
if stk:
    while stk: ans += stk.pop()
print(ans)



