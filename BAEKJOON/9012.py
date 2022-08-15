'''
괄호

잘 닫힌 괄호들인지 아닌지 확인
YES or NO
'''
for _ in range(int(input())):
    c = 0
    for i in input():
        if i == '(':
            c += 1
        if i == ')' :
            c -= 1
        if c < 0: # 중간에 하나 더 닫히면 끝
            break
    if c : # 다 돌았는데 C가 0이 아니면 NO
        print("NO")
    else :
        print("YES")
        


