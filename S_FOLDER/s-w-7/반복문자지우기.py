'''
반복문자 지우기

반복된 문자를 지워간다.
CAAABBA
CABBA
CAA
C

입력
테케T
길이 1000 이하 문자열

출력
#테케 답
'''
# 괄호랑 똑같다. 단, 괄호가 제시되지 않은.
for testcase in range(1, int(input())+1):
    s = input()
    li = []
    for i in s:
        if li == [] or i != li[-1]: # 비어있거나 가장 최근 입력 받은거랑 다르면 append
            li.append(i)
        elif i == li[-1]: # 가장 최근 입력받은거랑 같으면 pop
            li.pop()
    print(f"#{testcase} {len(li)}")
