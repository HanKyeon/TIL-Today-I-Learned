'''
쇠막대기

() 쇠막대기

입력
괄호들 입력

출력
조각 총 갯수
'''
import sys

s = sys.stdin.readline().rstrip()
stk, ans = [], 0
for i in range(len(s)):
    c = s[i]
    if c == "(":
        stk.append(c)
    elif c == ")":
        stk.pop()
        if s[i-1] == "(":
            ans += len(stk)
            continue
        ans+= 1
print(ans)


















for testcase in range(1, int(input())+1):
    s = list(input()) #입력
    ans, c, clo = 0, 0, False # 정답, 카운트, 닫힘 만났는지 판별 여부
    for i in s: # 순회하면서
        if i == '(': # 여는거 만나면
            clo = False # 닫은거 안만났고
            c += 1 # 카운트 더하기
        elif i == ')' and clo == False: # 열린 상태에서 닫힘을 처음 만나면
            clo = True # 닫아주고
            c -= 1 # 하나 내려주고
            ans += c # 그걸 답에 더해줌
        elif i == ')' and clo == True: # 닫힌 상태에서 닫힌거 만나면
            c -= 1 # 1 빼주고
            ans += 1 # 1 더해줌
    print(f"#{testcase} {ans}") # 출력